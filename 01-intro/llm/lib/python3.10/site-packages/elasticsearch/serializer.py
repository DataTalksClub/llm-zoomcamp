#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Any, ClassVar, Dict, Tuple

from elastic_transport import JsonSerializer as _JsonSerializer
from elastic_transport import NdjsonSerializer as _NdjsonSerializer
from elastic_transport import Serializer as Serializer
from elastic_transport import TextSerializer as TextSerializer

from .exceptions import SerializationError

INTEGER_TYPES = ()
FLOAT_TYPES = (Decimal,)
TIME_TYPES = (date, datetime)

__all__ = [
    "Serializer",
    "JsonSerializer",
    "TextSerializer",
    "NdjsonSerializer",
    "CompatibilityModeJsonSerializer",
    "CompatibilityModeNdjsonSerializer",
    "MapboxVectorTileSerializer",
]

try:
    from elastic_transport import OrjsonSerializer as _OrjsonSerializer

    __all__.append("OrjsonSerializer")
except ImportError:
    _OrjsonSerializer = None  # type: ignore[assignment,misc]


class JsonSerializer(_JsonSerializer):
    mimetype: ClassVar[str] = "application/json"

    def default(self, data: Any) -> Any:
        if isinstance(data, TIME_TYPES):
            # Little hack to avoid importing pandas but to not
            # return 'NaT' string for pd.NaT as that's not a valid
            # Elasticsearch date.
            formatted_data = data.isoformat()
            if formatted_data != "NaT":
                return formatted_data

        if isinstance(data, uuid.UUID):
            return str(data)
        elif isinstance(data, FLOAT_TYPES):
            return float(data)

        # This is kept for backwards compatibility even
        # if 'INTEGER_TYPES' isn't used by default anymore.
        elif INTEGER_TYPES and isinstance(data, INTEGER_TYPES):
            return int(data)

        # Special cases for numpy and pandas types
        # These are expensive to import so we try them last.
        serialized, value = _attempt_serialize_numpy_or_pandas(data)
        if serialized:
            return value

        raise TypeError(f"Unable to serialize {data!r} (type: {type(data)})")


if _OrjsonSerializer is not None:

    class OrjsonSerializer(JsonSerializer, _OrjsonSerializer):
        def default(self, data: Any) -> Any:
            return JsonSerializer.default(self, data)


class NdjsonSerializer(JsonSerializer, _NdjsonSerializer):
    mimetype: ClassVar[str] = "application/x-ndjson"

    def default(self, data: Any) -> Any:
        return JsonSerializer.default(self, data)


class CompatibilityModeJsonSerializer(JsonSerializer):
    mimetype: ClassVar[str] = "application/vnd.elasticsearch+json"


class CompatibilityModeNdjsonSerializer(NdjsonSerializer):
    mimetype: ClassVar[str] = "application/vnd.elasticsearch+x-ndjson"


class MapboxVectorTileSerializer(Serializer):
    mimetype: ClassVar[str] = "application/vnd.mapbox-vector-tile"

    def loads(self, data: bytes) -> bytes:
        return data

    def dumps(self, data: bytes) -> bytes:
        if isinstance(data, bytes):
            return data
        raise SerializationError(f"Cannot serialize {data!r} into a MapBox vector tile")


DEFAULT_SERIALIZERS: Dict[str, Serializer] = {
    JsonSerializer.mimetype: JsonSerializer(),
    MapboxVectorTileSerializer.mimetype: MapboxVectorTileSerializer(),
    NdjsonSerializer.mimetype: NdjsonSerializer(),
    CompatibilityModeJsonSerializer.mimetype: CompatibilityModeJsonSerializer(),
    CompatibilityModeNdjsonSerializer.mimetype: CompatibilityModeNdjsonSerializer(),
}

# Alias for backwards compatibility
JSONSerializer = JsonSerializer


def _attempt_serialize_numpy_or_pandas(data: Any) -> Tuple[bool, Any]:
    """Attempts to serialize a value from the numpy or pandas libraries.
    This function is separate from JSONSerializer because the inner functions
    are rewritten to be no-ops if either library isn't available to avoid
    attempting to import and raising an ImportError over and over again.

    Returns a tuple of (bool, Any) where the bool corresponds to whether
    the second value contains a properly serialized value and thus
    should be returned by JSONSerializer.default().
    """
    serialized, value = _attempt_serialize_numpy(data)
    if serialized:
        return serialized, value

    serialized, value = _attempt_serialize_pandas(data)
    if serialized:
        return serialized, value

    return False, None


def _attempt_serialize_numpy(data: Any) -> Tuple[bool, Any]:
    global _attempt_serialize_numpy
    try:
        import numpy as np

        if isinstance(
            data,
            (
                np.int_,
                np.intc,
                np.int8,
                np.int16,
                np.int32,
                np.int64,
                np.uint8,
                np.uint16,
                np.uint32,
                np.uint64,
            ),
        ):
            return True, int(data)
        elif isinstance(
            data,
            (
                np.float16,
                np.float32,
                np.float64,
            ),
        ):
            return True, float(data)
        elif isinstance(data, np.bool_):
            return True, bool(data)
        elif isinstance(data, np.datetime64):
            return True, data.item().isoformat()
        elif isinstance(data, np.ndarray):
            return True, data.tolist()

    except ImportError:
        # Since we failed to import 'numpy' we don't want to try again.
        _attempt_serialize_numpy = _attempt_serialize_noop

    return False, None


def _attempt_serialize_pandas(data: Any) -> Tuple[bool, Any]:
    global _attempt_serialize_pandas
    try:
        import pandas as pd

        if isinstance(data, (pd.Series, pd.Categorical)):
            return True, data.tolist()
        elif isinstance(data, pd.Timestamp) and data is not getattr(pd, "NaT", None):
            return True, data.isoformat()
        elif data is getattr(pd, "NA", None):
            return True, None

    except ImportError:
        # Since we failed to import 'pandas' we don't want to try again.
        _attempt_serialize_pandas = _attempt_serialize_noop

    return False, None


def _attempt_serialize_noop(data: Any) -> Tuple[bool, Any]:  # noqa
    # Short-circuit if the above functions can't import
    # the corresponding library on the first attempt.
    return False, None
