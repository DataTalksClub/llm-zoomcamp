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

import json
import re
import uuid
from datetime import date
from decimal import Decimal
from typing import Any, ClassVar, Mapping, Optional

from ._exceptions import SerializationError

try:
    import orjson
except ModuleNotFoundError:
    orjson = None  # type: ignore[assignment]


class Serializer:
    """Serializer interface."""

    mimetype: ClassVar[str]

    def loads(self, data: bytes) -> Any:  # pragma: nocover
        raise NotImplementedError()

    def dumps(self, data: Any) -> bytes:  # pragma: nocover
        raise NotImplementedError()


class TextSerializer(Serializer):
    """Text serializer to and from UTF-8."""

    mimetype: ClassVar[str] = "text/*"

    def loads(self, data: bytes) -> str:
        if isinstance(data, str):
            return data
        try:
            return data.decode("utf-8", "surrogatepass")
        except UnicodeError as e:
            raise SerializationError(
                f"Unable to deserialize as text: {data!r}", errors=(e,)
            )

    def dumps(self, data: str) -> bytes:
        # The body is already encoded to bytes
        # so we forward the request body along.
        if isinstance(data, bytes):
            return data
        try:
            return data.encode("utf-8", "surrogatepass")
        except (AttributeError, UnicodeError, TypeError) as e:
            raise SerializationError(
                f"Unable to serialize to text: {data!r}", errors=(e,)
            )


class JsonSerializer(Serializer):
    """JSON serializer relying on the standard library json module."""

    mimetype: ClassVar[str] = "application/json"

    def default(self, data: Any) -> Any:
        if isinstance(data, date):
            return data.isoformat()
        elif isinstance(data, uuid.UUID):
            return str(data)
        elif isinstance(data, Decimal):
            return float(data)
        raise SerializationError(
            message=f"Unable to serialize to JSON: {data!r} (type: {type(data).__name__})",
        )

    def json_dumps(self, data: Any) -> bytes:
        return json.dumps(
            data, default=self.default, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8", "surrogatepass")

    def json_loads(self, data: bytes) -> Any:
        return json.loads(data)

    def loads(self, data: bytes) -> Any:
        # Sometimes responses use Content-Type: json but actually
        # don't contain any data. We should return something instead
        # of erroring in these cases.
        if data == b"":
            return None

        try:
            return self.json_loads(data)
        except (ValueError, TypeError) as e:
            raise SerializationError(
                message=f"Unable to deserialize as JSON: {data!r}", errors=(e,)
            )

    def dumps(self, data: Any) -> bytes:
        # The body is already encoded to bytes
        # so we forward the request body along.
        if isinstance(data, str):
            return data.encode("utf-8", "surrogatepass")
        elif isinstance(data, bytes):
            return data

        try:
            return self.json_dumps(data)
        # This should be captured by the .default()
        # call but just in case we also wrap these.
        except (ValueError, UnicodeError, TypeError) as e:  # pragma: nocover
            raise SerializationError(
                message=f"Unable to serialize to JSON: {data!r} (type: {type(data).__name__})",
                errors=(e,),
            )


if orjson is not None:

    class OrjsonSerializer(JsonSerializer):
        """JSON serializer relying on the orjson package.

        Only available if orjson if installed. It is faster, especially for vectors, but is also stricter.
        """

        def json_dumps(self, data: Any) -> bytes:
            return orjson.dumps(
                data, default=self.default, option=orjson.OPT_SERIALIZE_NUMPY
            )

        def json_loads(self, data: bytes) -> Any:
            return orjson.loads(data)


class NdjsonSerializer(JsonSerializer):
    """Newline delimited JSON (NDJSON) serializer relying on the standard library json module."""

    mimetype: ClassVar[str] = "application/x-ndjson"

    def loads(self, data: bytes) -> Any:
        ndjson = []
        for line in re.split(b"[\n\r]", data):
            if not line:
                continue
            try:
                ndjson.append(self.json_loads(line))
            except (ValueError, TypeError) as e:
                raise SerializationError(
                    message=f"Unable to deserialize as NDJSON: {data!r}", errors=(e,)
                )
        return ndjson

    def dumps(self, data: Any) -> bytes:
        # The body is already encoded to bytes
        # so we forward the request body along.
        if isinstance(data, (bytes, str)):
            data = (data,)

        buffer = bytearray()
        for line in data:
            if isinstance(line, str):
                line = line.encode("utf-8", "surrogatepass")
            if isinstance(line, bytes):
                buffer += line
                # Ensure that there is always a final newline
                if not line.endswith(b"\n"):
                    buffer += b"\n"
            else:
                try:
                    buffer += self.json_dumps(line)
                    buffer += b"\n"
                # This should be captured by the .default()
                # call but just in case we also wrap these.
                except (ValueError, UnicodeError, TypeError) as e:  # pragma: nocover
                    raise SerializationError(
                        message=f"Unable to serialize to NDJSON: {data!r} (type: {type(data).__name__})",
                        errors=(e,),
                    )

        return bytes(buffer)


DEFAULT_SERIALIZERS = {
    JsonSerializer.mimetype: JsonSerializer(),
    TextSerializer.mimetype: TextSerializer(),
    NdjsonSerializer.mimetype: NdjsonSerializer(),
}


class SerializerCollection:
    """Collection of serializers that can be fetched by mimetype. Used by
    :class:`elastic_transport.Transport` to serialize and deserialize native
    Python types into bytes before passing to a node.
    """

    def __init__(
        self,
        serializers: Optional[Mapping[str, Serializer]] = None,
        default_mimetype: str = "application/json",
    ):
        if serializers is None:
            serializers = DEFAULT_SERIALIZERS
        try:
            self.default_serializer = serializers[default_mimetype]
        except KeyError:
            raise ValueError(
                f"Must configure a serializer for the default mimetype {default_mimetype!r}"
            ) from None
        self.serializers = dict(serializers)

    def dumps(self, data: Any, mimetype: Optional[str] = None) -> bytes:
        return self.get_serializer(mimetype).dumps(data)

    def loads(self, data: bytes, mimetype: Optional[str] = None) -> Any:
        return self.get_serializer(mimetype).loads(data)

    def get_serializer(self, mimetype: Optional[str]) -> Serializer:
        # split out charset
        if mimetype is None:
            serializer = self.default_serializer
        else:
            mimetype, _, _ = mimetype.partition(";")
            try:
                serializer = self.serializers[mimetype]
            except KeyError:
                # Try for '<mimetype-supertype>/*' types after the specific type fails.
                try:
                    mimetype_supertype = mimetype.partition("/")[0]
                    serializer = self.serializers[f"{mimetype_supertype}/*"]
                except KeyError:
                    raise SerializationError(
                        f"Unknown mimetype, not able to serialize or deserialize: {mimetype}"
                    ) from None
        return serializer
