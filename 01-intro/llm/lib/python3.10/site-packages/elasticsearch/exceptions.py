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

from typing import Any, Dict, Type

from elastic_transport import ApiError as _ApiError
from elastic_transport import ConnectionError as ConnectionError
from elastic_transport import ConnectionTimeout as ConnectionTimeout
from elastic_transport import SerializationError as SerializationError
from elastic_transport import TlsError as SSLError
from elastic_transport import TransportError as TransportError
from elastic_transport import TransportWarning

__all__ = [
    "SerializationError",
    "TransportError",
    "ConnectionError",
    "SSLError",
    "ConnectionTimeout",
    "AuthorizationException",
    "AuthenticationException",
    "NotFoundError",
    "ConflictError",
    "BadRequestError",
]


class ApiError(_ApiError):
    @property
    def status_code(self) -> int:
        """Backwards-compatible way to access ``self.meta.status``"""
        return self.meta.status

    @property
    def error(self) -> str:
        """Backwards-compatible way to access ``self.message``"""
        return self.message

    @property
    def info(self) -> Any:
        """Backwards-compatible way to access ``self.body``"""
        return self.body

    def __str__(self) -> str:
        cause = ""
        try:
            if self.body and isinstance(self.body, dict) and "error" in self.body:
                if isinstance(self.body["error"], dict):
                    root_cause = self.body["error"]["root_cause"][0]
                    cause = ", ".join(
                        filter(
                            None,
                            [
                                repr(root_cause["reason"]),
                                root_cause.get("resource.id"),
                                root_cause.get("resource.type"),
                            ],
                        )
                    )

                else:
                    cause = repr(self.body["error"])
        except LookupError:
            pass
        msg = ", ".join(filter(None, [str(self.status_code), repr(self.error), cause]))
        return f"{self.__class__.__name__}({msg})"


class UnsupportedProductError(ApiError):
    """Error which is raised when the client detects
    it's not connected to a supported product.
    """

    def __str__(self) -> str:
        return self.message


class NotFoundError(ApiError):
    """Exception representing a 404 status code."""


class ConflictError(ApiError):
    """Exception representing a 409 status code."""


class BadRequestError(ApiError):
    """Exception representing a 400 status code."""


class AuthenticationException(ApiError):
    """Exception representing a 401 status code."""


class AuthorizationException(ApiError):
    """Exception representing a 403 status code."""


class ElasticsearchWarning(TransportWarning):
    """Warning that is raised when a deprecated option
    or incorrect usage is flagged via the 'Warning' HTTP header.
    """


# Aliases for backwards compatibility
ElasticsearchDeprecationWarning = ElasticsearchWarning
RequestError = BadRequestError


HTTP_EXCEPTIONS: Dict[int, Type[ApiError]] = {
    400: BadRequestError,
    401: AuthenticationException,
    403: AuthorizationException,
    404: NotFoundError,
    409: ConflictError,
}
