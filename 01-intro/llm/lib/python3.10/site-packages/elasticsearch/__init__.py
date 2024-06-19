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

# flake8: noqa

import logging
import re
import warnings

from elastic_transport import __version__ as _elastic_transport_version

from ._utils import fixup_module_metadata
from ._version import __versionstr__

# Ensure that a compatible version of elastic-transport is installed.
_version_groups = tuple(int(x) for x in re.search(r"^(\d+)\.(\d+)\.(\d+)", _elastic_transport_version).groups())  # type: ignore
if _version_groups < (8, 0, 0) or _version_groups > (9, 0, 0):
    raise ImportError(
        "An incompatible version of elastic-transport is installed. Must be between "
        "v8.0.0 and v9.0.0. Install the correct version with the following command: "
        "$ python -m pip install 'elastic-transport>=8, <9'"
    )

_version_groups = re.search(r"^(\d+)\.(\d+)\.(\d+)", __versionstr__).groups()  # type: ignore
_major, _minor, _patch = (int(x) for x in _version_groups)
VERSION = __version__ = (_major, _minor, _patch)

logger = logging.getLogger("elasticsearch")
logger.addHandler(logging.NullHandler())

from ._async.client import AsyncElasticsearch as AsyncElasticsearch
from ._sync.client import Elasticsearch as Elasticsearch
from .exceptions import ElasticsearchDeprecationWarning  # noqa: F401
from .exceptions import (
    ApiError,
    AuthenticationException,
    AuthorizationException,
    BadRequestError,
    ConflictError,
    ConnectionError,
    ConnectionTimeout,
    ElasticsearchWarning,
    NotFoundError,
    RequestError,
    SerializationError,
    SSLError,
    TransportError,
    UnsupportedProductError,
)
from .serializer import JSONSerializer, JsonSerializer

try:
    from .serializer import OrjsonSerializer
except ImportError:
    OrjsonSerializer = None  # type: ignore[assignment,misc]

# Only raise one warning per deprecation message so as not
# to spam up the user if the same action is done multiple times.
warnings.simplefilter("default", category=ElasticsearchWarning, append=True)

__all__ = [
    "ApiError",
    "AsyncElasticsearch",
    "BadRequestError",
    "Elasticsearch",
    "JsonSerializer",
    "SerializationError",
    "TransportError",
    "NotFoundError",
    "ConflictError",
    "RequestError",
    "ConnectionError",
    "SSLError",
    "ConnectionTimeout",
    "AuthenticationException",
    "AuthorizationException",
    "UnsupportedProductError",
    "ElasticsearchWarning",
]
if OrjsonSerializer is not None:
    __all__.append("OrjsonSerializer")

fixup_module_metadata(__name__, globals())
del fixup_module_metadata
