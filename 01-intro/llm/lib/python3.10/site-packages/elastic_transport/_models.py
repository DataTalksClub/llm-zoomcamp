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

import dataclasses
import enum
import re
import ssl
from dataclasses import dataclass, field
from typing import (
    TYPE_CHECKING,
    Any,
    Collection,
    Dict,
    Iterator,
    KeysView,
    Mapping,
    MutableMapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
    ValuesView,
)

if TYPE_CHECKING:
    from typing_extensions import Final


class DefaultType(enum.Enum):
    """
    Sentinel used as a default value when ``None`` has special meaning like timeouts.
    The only comparisons that are supported for this type are ``is``.
    """

    value = 0

    def __repr__(self) -> str:
        return "<DEFAULT>"

    def __str__(self) -> str:
        return "<DEFAULT>"


DEFAULT: "Final[DefaultType]" = DefaultType.value

T = TypeVar("T")

try:
    from ssl import TLSVersion

    _TYPE_SSL_VERSION = Union[int, TLSVersion]
except ImportError:
    _TYPE_SSL_VERSION = int  # type: ignore[misc]


class HttpHeaders(MutableMapping[str, str]):
    """HTTP headers"""

    __slots__ = ("_internal", "_frozen")

    def __init__(
        self,
        initial: Optional[Union[Mapping[str, str], Collection[Tuple[str, str]]]] = None,
    ) -> None:
        self._internal = {}
        self._frozen = False
        if initial:
            for key, val in dict(initial).items():
                self._internal[self._normalize_key(key)] = (key, val)

    def __setitem__(self, key: str, value: str) -> None:
        if self._frozen:
            raise ValueError("Can't modify headers that have been frozen")
        self._internal[self._normalize_key(key)] = (key, value)

    def __getitem__(self, item: str) -> str:
        return self._internal[self._normalize_key(item)][1]

    def __delitem__(self, key: str) -> None:
        if self._frozen:
            raise ValueError("Can't modify headers that have been frozen")
        del self._internal[self._normalize_key(key)]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mapping):
            return NotImplemented
        if not isinstance(other, HttpHeaders):
            other = HttpHeaders(other)
        return {k: v for k, (_, v) in self._internal.items()} == {
            k: v for k, (_, v) in other._internal.items()
        }

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Mapping):
            return NotImplemented
        return not self == other

    def __iter__(self) -> Iterator[str]:
        return iter(self.keys())

    def __len__(self) -> int:
        return len(self._internal)

    def __bool__(self) -> bool:
        return bool(self._internal)

    def __contains__(self, item: object) -> bool:
        return isinstance(item, str) and self._normalize_key(item) in self._internal

    def __repr__(self) -> str:
        return repr(self._dict_hide_auth())

    def __str__(self) -> str:
        return str(self._dict_hide_auth())

    def __hash__(self) -> int:
        if not self._frozen:
            raise ValueError("Can't calculate the hash of headers that aren't frozen")
        return hash(tuple((k, v) for k, (_, v) in sorted(self._internal.items())))

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:  # type: ignore[override]
        return self._internal.get(self._normalize_key(key), (None, default))[1]

    def keys(self) -> KeysView[str]:
        return self._internal.keys()

    def values(self) -> ValuesView[str]:
        return {"": v for _, v in self._internal.values()}.values()

    def items(self) -> Collection[Tuple[str, str]]:  # type: ignore[override]
        return [(key, val) for _, (key, val) in self._internal.items()]

    def freeze(self) -> "HttpHeaders":
        """Freezes the current set of headers so they can be used in hashes.
        Returns the same instance, doesn't make a copy.
        """
        self._frozen = True
        return self

    @property
    def frozen(self) -> bool:
        return self._frozen

    def copy(self) -> "HttpHeaders":
        return HttpHeaders(self.items())

    def _normalize_key(self, key: str) -> str:
        try:
            return key.lower()
        except AttributeError:
            return key

    def _dict_hide_auth(self) -> Dict[str, str]:
        def hide_auth(val: str) -> str:
            # Hides only the authentication value, not the method.
            match = re.match(r"^(ApiKey|Basic|Bearer) ", val)
            if match:
                return f"{match.group(1)} <hidden>"
            return "<hidden>"

        return {
            key: hide_auth(val) if key.lower() == "authorization" else val
            for key, val in self.items()
        }


@dataclass
class ApiResponseMeta:
    """Metadata that is returned from Transport.perform_request()"""

    #: HTTP status code
    status: int

    #: HTTP version being used
    http_version: str

    #: HTTP headers
    headers: HttpHeaders

    #: Number of seconds from start of request to start of response
    duration: float

    #: Node which handled the request
    node: "NodeConfig"

    @property
    def mimetype(self) -> Optional[str]:
        """Mimetype to be used by the serializer to decode the raw response bytes."""
        try:
            content_type = self.headers["content-type"]
            return content_type.partition(";")[0] or None
        except KeyError:
            return None


def _empty_frozen_http_headers() -> HttpHeaders:
    """Used for the 'default_factory' of the 'NodeConfig.headers'"""
    return HttpHeaders().freeze()


@dataclass(repr=True)
class NodeConfig:
    """Configuration options available for every node."""

    #: Protocol in use to connect to the node
    scheme: str
    #: IP address or hostname to connect to
    host: str
    #: IP port to connect to
    port: int
    #: Prefix to add to the path of every request
    path_prefix: str = ""

    #: Default HTTP headers to add to every request
    headers: Union[HttpHeaders, Mapping[str, str]] = field(
        default_factory=_empty_frozen_http_headers
    )

    #: Number of concurrent connections that are
    #: able to be open at one time for this node.
    #: Having multiple connections per node allows
    #: for higher concurrency of requests.
    connections_per_node: int = 10

    #: Number of seconds to wait before a request should timeout.
    request_timeout: Optional[float] = 10.0

    #: Set to ``True`` to enable HTTP compression
    #: of request and response bodies via gzip.
    http_compress: Optional[bool] = False

    #: Set to ``True`` to verify the node's TLS certificate against 'ca_certs'
    #: Setting to ``False`` will disable verifying the node's certificate.
    verify_certs: Optional[bool] = True

    #: Path to a CA bundle or directory containing bundles. By default
    #: If the ``certifi`` package is installed and ``verify_certs`` is
    #: set to ``True`` this value will be set to ``certifi.where()``.
    ca_certs: Optional[str] = None

    #: Path to a client certificate for TLS client authentication.
    client_cert: Optional[str] = None
    #: Path to a client private key for TLS client authentication.
    client_key: Optional[str] = None
    #: Hostname or IP address to verify on the node's certificate.
    #: This is useful if the certificate contains a different value
    #: than the one supplied in ``host``. An example of this situation
    #: is connecting to an IP address instead of a hostname.
    #: Set to ``False`` to disable certificate hostname verification.
    ssl_assert_hostname: Optional[str] = None
    #: SHA-256 fingerprint of the node's certificate. If this value is
    #: given then root-of-trust verification isn't done and only the
    #: node's certificate fingerprint is verified.
    #:
    #: On CPython 3.10+ this also verifies if any certificate in the
    #: chain including the Root CA matches this fingerprint. However
    #: because this requires using private APIs support for this is
    #: **experimental**.
    ssl_assert_fingerprint: Optional[str] = None
    #: Minimum TLS version to use to connect to the node. Can be either
    #: :class:`ssl.TLSVersion` on Python 3.7+ or one of the
    #: ``ssl.PROTOCOL_TLSvX`` instances.
    ssl_version: Optional[_TYPE_SSL_VERSION] = None
    #: Pre-configured :class:`ssl.SSLContext` object. If this value
    #: is given then no other TLS options (besides ``ssl_assert_fingerprint``)
    #: can be set on the :class:`elastic_transport.NodeConfig`.
    ssl_context: Optional[ssl.SSLContext] = field(default=None, hash=False)
    #: Set to ``False`` to disable the :class:`elastic_transport.SecurityWarning`
    #: issued when using ``verify_certs=False``.
    ssl_show_warn: bool = True

    #: Extras that can be set to anything, typically used
    #: for annotating this node with additional information for
    #: future decisions like sniffing, instance roles, etc.
    #: Third-party keys should start with an underscore and prefix.
    _extras: Dict[str, Any] = field(default_factory=dict, hash=False)

    def replace(self, **kwargs: Any) -> "NodeConfig":
        if not kwargs:
            return self
        return dataclasses.replace(self, **kwargs)

    def __post_init__(self) -> None:
        if not isinstance(self.headers, HttpHeaders) or not self.headers.frozen:
            self.headers = HttpHeaders(self.headers).freeze()

        if self.scheme != self.scheme.lower():
            raise ValueError("'scheme' must be lowercase")
        if "[" in self.host or "]" in self.host:
            raise ValueError("'host' must not have square braces")
        if self.port < 0:
            raise ValueError("'port' must be a positive integer")
        if self.connections_per_node <= 0:
            raise ValueError("'connections_per_node' must be a positive integer")
        if self.path_prefix:
            self.path_prefix = (
                ("/" + self.path_prefix.strip("/")) if self.path_prefix else ""
            )

        tls_options = [
            "ca_certs",
            "client_cert",
            "client_key",
            "ssl_assert_hostname",
            "ssl_assert_fingerprint",
            "ssl_context",
        ]

        # Disallow setting TLS options on non-HTTPS connections.
        if self.scheme != "https":
            if any(getattr(self, attr) is not None for attr in tls_options):
                raise ValueError("TLS options require scheme to be 'https'")

        elif self.scheme == "https":
            # It's not valid to set 'ssl_context' and any other
            # TLS option, the SSLContext object must be configured
            # the way the user wants already.
            def tls_option_filter(attr: object) -> bool:
                return (
                    isinstance(attr, str)
                    and attr not in ("ssl_context", "ssl_assert_fingerprint")
                    and getattr(self, attr) is not None
                )

            if self.ssl_context is not None and any(
                filter(
                    tls_option_filter,
                    tls_options,
                )
            ):
                raise ValueError(
                    "The 'ssl_context' option can't be combined with other TLS options"
                )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NodeConfig):
            return NotImplemented
        return (
            self.scheme == other.scheme
            and self.host == other.host
            and self.port == other.port
            and self.path_prefix == other.path_prefix
        )

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, NodeConfig):
            return NotImplemented
        return not self == other

    def __hash__(self) -> int:
        return hash(
            (
                self.scheme,
                self.host,
                self.port,
                self.path_prefix,
            )
        )


@dataclass()
class SniffOptions:
    """Options which are passed to Transport.sniff_callback"""

    is_initial_sniff: bool
    sniff_timeout: Optional[float]
