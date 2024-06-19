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

from typing import Any, Tuple

from ._models import ApiResponseMeta


class TransportWarning(Warning):
    """Generic warning for the 'elastic-transport' package."""


class SecurityWarning(TransportWarning):
    """Warning for potentially insecure configurations."""


class TransportError(Exception):
    """Generic exception for the 'elastic-transport' package.

    For the 'errors' attribute, errors are ordered from
    most recently raised (index=0) to least recently raised (index=N)

    If an HTTP status code is available with the error it
    will be stored under 'status'. If HTTP headers are available
    they are stored under 'headers'.
    """

    def __init__(self, message: Any, errors: Tuple[Exception, ...] = ()):
        super().__init__(message)
        self.errors = tuple(errors)
        self.message = message

    def __repr__(self) -> str:
        parts = [repr(self.message)]
        if self.errors:
            parts.append(f"errors={self.errors!r}")
        return "{}({})".format(self.__class__.__name__, ", ".join(parts))

    def __str__(self) -> str:
        return str(self.message)


class SniffingError(TransportError):
    """Error that occurs during the sniffing of nodes"""


class SerializationError(TransportError):
    """Error that occurred during the serialization or
    deserialization of an HTTP message body
    """


class ConnectionError(TransportError):
    """Error raised by the HTTP connection"""

    def __str__(self) -> str:
        if self.errors:
            return f"Connection error caused by: {self.errors[0].__class__.__name__}({self.errors[0]})"
        return "Connection error"


class TlsError(ConnectionError):
    """Error raised by during the TLS handshake"""

    def __str__(self) -> str:
        if self.errors:
            return f"TLS error caused by: {self.errors[0].__class__.__name__}({self.errors[0]})"
        return "TLS error"


class ConnectionTimeout(TransportError):
    """Connection timed out during an operation"""

    def __str__(self) -> str:
        if self.errors:
            return f"Connection timeout caused by: {self.errors[0].__class__.__name__}({self.errors[0]})"
        return "Connection timed out"


class ApiError(Exception):
    """Base-class for clients that raise errors due to a response such as '404 Not Found'"""

    def __init__(
        self,
        message: str,
        meta: ApiResponseMeta,
        body: Any,
        errors: Tuple[Exception, ...] = (),
    ):
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.meta = meta
        self.body = body

    def __repr__(self) -> str:
        parts = [repr(self.message)]
        if self.meta:
            parts.append(f"meta={self.meta!r}")
        if self.errors:
            parts.append(f"errors={self.errors!r}")
        if self.body is not None:
            parts.append(f"body={self.body!r}")
        return "{}({})".format(self.__class__.__name__, ", ".join(parts))

    def __str__(self) -> str:
        return f"[{self.meta.status}] {self.message}"
