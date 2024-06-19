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

import asyncio
import logging
import os
import ssl
from typing import Any, ClassVar, List, NamedTuple, Optional, Tuple, Union

from .._models import ApiResponseMeta, HttpHeaders, NodeConfig
from .._utils import is_ipaddress
from .._version import __version__
from ..client_utils import DEFAULT, DefaultType

_logger = logging.getLogger("elastic_transport.node")
_logger.propagate = False  # This logger is very verbose so disable propogation.

DEFAULT_CA_CERTS: Optional[str] = None
DEFAULT_USER_AGENT = f"elastic-transport-python/{__version__}"
RERAISE_EXCEPTIONS = (RecursionError, asyncio.CancelledError)
BUILTIN_EXCEPTIONS = (
    ValueError,
    KeyError,
    NameError,
    AttributeError,
    LookupError,
    AssertionError,
    IndexError,
    MemoryError,
    RuntimeError,
    SystemError,
    TypeError,
)
HTTP_STATUS_REASONS = {
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Content Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    429: "Too Many Requests",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}

try:
    import certifi

    DEFAULT_CA_CERTS = certifi.where()
except ImportError:  # pragma: nocover
    pass


class NodeApiResponse(NamedTuple):
    meta: ApiResponseMeta
    body: bytes


class BaseNode:
    """
    Class responsible for maintaining a connection to a node. It
    holds persistent node pool to it and it's main interface
    (``perform_request``) is thread-safe.

    :arg config: :class:`~elastic_transport.NodeConfig` instance
    """

    _CLIENT_META_HTTP_CLIENT: ClassVar[Tuple[str, str]]

    def __init__(self, config: NodeConfig):
        self._config = config
        self._headers: HttpHeaders = self.config.headers.copy()  # type: ignore[attr-defined]
        self.headers.setdefault("connection", "keep-alive")
        self.headers.setdefault("user-agent", DEFAULT_USER_AGENT)
        self._http_compress = bool(config.http_compress or False)
        if config.http_compress:
            self.headers["accept-encoding"] = "gzip"

        self._scheme = config.scheme
        self._host = config.host
        self._port = config.port
        self._path_prefix = (
            ("/" + config.path_prefix.strip("/")) if config.path_prefix else ""
        )

    @property
    def config(self) -> NodeConfig:
        return self._config

    @property
    def headers(self) -> HttpHeaders:
        return self._headers

    @property
    def scheme(self) -> str:
        return self._scheme

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def path_prefix(self) -> str:
        return self._path_prefix

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({self.base_url})>"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, BaseNode):
            return NotImplemented
        return id(self) < id(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseNode):
            return NotImplemented
        return self.__hash__() == other.__hash__()

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, BaseNode):
            return NotImplemented
        return not self == other

    def __hash__(self) -> int:
        return hash((str(type(self).__name__), self.config))

    @property
    def base_url(self) -> str:
        return "".join(
            [
                self.scheme,
                "://",
                # IPv6 must be wrapped by [...]
                "[%s]" % self.host if ":" in self.host else self.host,
                ":%s" % self.port if self.port is not None else "",
                self.path_prefix,
            ]
        )

    def perform_request(
        self,
        method: str,
        target: str,
        body: Optional[bytes] = None,
        headers: Optional[HttpHeaders] = None,
        request_timeout: Union[DefaultType, Optional[float]] = DEFAULT,
    ) -> NodeApiResponse:  # pragma: nocover
        """Constructs and sends an HTTP request and parses the HTTP response.

        :param method: HTTP method
        :param target: HTTP request target, typically path+query
        :param body: Optional HTTP request body encoded as bytes
        :param headers: Optional HTTP headers to send in addition to
            the headers already configured.
        :param request_timeout: Amount of time to wait for the first
            response bytes to arrive before raising a
            :class:`elastic_transport.ConnectionTimeout` error.
        :raises:
            :class:`elastic_transport.ConnectionError`,
            :class:`elastic_transport.ConnectionTimeout`,
            :class:`elastic_transport.TlsError`
        :rtype: Tuple[ApiResponseMeta, bytes]
        :returns: Metadata about the request+response and the raw
            decompressed bytes from the HTTP response body.
        """
        raise NotImplementedError()

    def close(self) -> None:  # pragma: nocover
        pass

    def _log_request(
        self,
        method: str,
        target: str,
        headers: Optional[HttpHeaders],
        body: Optional[bytes],
        meta: Optional[ApiResponseMeta] = None,
        response: Optional[bytes] = None,
        exception: Optional[Exception] = None,
    ) -> None:
        if _logger.hasHandlers():
            http_version = meta.http_version if meta else "?.?"
            lines = ["> %s %s HTTP/%s"]
            log_args: List[Any] = [method, target, http_version]
            if headers:
                for header, value in sorted(headers._dict_hide_auth().items()):
                    lines.append(f"> {header.title()}: {value}")
            if body is not None:
                try:
                    body_encoded = body.decode("utf-8", "surrogatepass")
                except UnicodeError:
                    body_encoded = repr(body)
                log_args.append(body_encoded)
                lines.append("> %s")

            if meta is not None:
                reason = HTTP_STATUS_REASONS.get(meta.status, None)
                if reason:
                    lines.append("< HTTP/%s %d %s")
                    log_args.extend((http_version, meta.status, reason))
                else:
                    lines.append("< HTTP/%s %d")
                    log_args.extend((http_version, meta.status))
                if meta.headers:
                    for header, value in sorted(meta.headers.items()):
                        lines.append(f"< {header.title()}: {value}")
                if response:
                    try:
                        response_decoded = response.decode("utf-8", "surrogatepass")
                    except UnicodeError:
                        response_decoded = repr(response)
                    log_args.append(response_decoded)
                    lines.append("< %s")

            if exception is not None:
                _logger.debug("\n".join(lines), *log_args, exc_info=exception)
            else:
                _logger.debug("\n".join(lines), *log_args)


_HAS_TLS_VERSION = hasattr(ssl, "TLSVersion")
_SSL_PROTOCOL_VERSION_ATTRS = ("TLSv1", "TLSv1_1", "TLSv1_2")
_SSL_PROTOCOL_VERSION_DEFAULT = getattr(ssl, "OP_NO_SSLv2", 0) | getattr(
    ssl, "OP_NO_SSLv3", 0
)
_SSL_PROTOCOL_VERSION_TO_OPTIONS = {}
_SSL_PROTOCOL_VERSION_TO_TLS_VERSION = {}
for i, _protocol_attr in enumerate(_SSL_PROTOCOL_VERSION_ATTRS):
    try:
        _protocol_value = getattr(ssl, f"PROTOCOL_{_protocol_attr}")
    except AttributeError:
        continue

    if _HAS_TLS_VERSION:
        _tls_version_value = getattr(ssl.TLSVersion, _protocol_attr)
        _SSL_PROTOCOL_VERSION_TO_TLS_VERSION[_protocol_value] = _tls_version_value
        _SSL_PROTOCOL_VERSION_TO_TLS_VERSION[_tls_version_value] = _tls_version_value

    # Because we're setting a minimum version we binary OR all the options together.
    _SSL_PROTOCOL_VERSION_TO_OPTIONS[_protocol_value] = (
        _SSL_PROTOCOL_VERSION_DEFAULT
        | sum(
            getattr(ssl, f"OP_NO_{_attr}", 0)
            for _attr in _SSL_PROTOCOL_VERSION_ATTRS[:i]
        )
    )

# TLSv1.3 is unique, doesn't have a PROTOCOL_TLSvX counterpart. So we have to set it manually.
if _HAS_TLS_VERSION:
    try:
        _SSL_PROTOCOL_VERSION_TO_TLS_VERSION[ssl.TLSVersion.TLSv1_3] = (
            ssl.TLSVersion.TLSv1_3
        )
    except AttributeError:  # pragma: nocover
        pass


def ssl_context_from_node_config(node_config: NodeConfig) -> ssl.SSLContext:
    if node_config.ssl_context:
        ctx = node_config.ssl_context
    else:
        ctx = ssl.create_default_context()

        # Enable/disable certificate verification in these orders
        # to avoid 'ValueErrors' from SSLContext. We only do this
        # step if the user doesn't pass a preconfigured SSLContext.
        if node_config.verify_certs:
            ctx.verify_mode = ssl.CERT_REQUIRED
            ctx.check_hostname = not is_ipaddress(node_config.host)
        else:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

    # Enable logging of TLS session keys for use with Wireshark.
    if hasattr(ctx, "keylog_filename"):
        sslkeylogfile = os.environ.get("SSLKEYLOGFILE", "")
        if sslkeylogfile:
            ctx.keylog_filename = sslkeylogfile

    # Apply the 'ssl_version' if given, otherwise default to TLSv1.2+
    ssl_version = node_config.ssl_version
    if ssl_version is None:
        if _HAS_TLS_VERSION:
            ssl_version = ssl.TLSVersion.TLSv1_2
        else:
            ssl_version = ssl.PROTOCOL_TLSv1_2

    try:
        if _HAS_TLS_VERSION:
            ctx.minimum_version = _SSL_PROTOCOL_VERSION_TO_TLS_VERSION[ssl_version]
        else:
            ctx.options |= _SSL_PROTOCOL_VERSION_TO_OPTIONS[ssl_version]
    except KeyError:
        raise ValueError(
            f"Unsupported value for 'ssl_version': {ssl_version!r}. Must be "
            "either 'ssl.PROTOCOL_TLSvX' or 'ssl.TLSVersion.TLSvX'"
        ) from None

    return ctx
