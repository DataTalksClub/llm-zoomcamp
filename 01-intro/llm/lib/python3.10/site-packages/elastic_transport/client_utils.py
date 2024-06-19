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

import base64
import binascii
import dataclasses
import re
import urllib.parse
from platform import python_version
from typing import Optional, Tuple, TypeVar, Union
from urllib.parse import quote as _quote

from urllib3.exceptions import LocationParseError
from urllib3.util import parse_url

from ._models import DEFAULT, DefaultType, NodeConfig
from ._utils import fixup_module_metadata
from ._version import __version__

__all__ = [
    "CloudId",
    "DEFAULT",
    "DefaultType",
    "basic_auth_to_header",
    "client_meta_version",
    "create_user_agent",
    "dataclasses",
    "parse_cloud_id",
    "percent_encode",
    "resolve_default",
    "to_bytes",
    "to_str",
    "url_to_node_config",
]

T = TypeVar("T")


def resolve_default(val: Union[DefaultType, T], default: T) -> T:
    """Resolves a value that could be the ``DEFAULT`` sentinel
    into either the given value or the default value.
    """
    return val if val is not DEFAULT else default


def create_user_agent(name: str, version: str) -> str:
    """Creates the 'User-Agent' header given the library name and version"""
    return (
        f"{name}/{version} (Python/{python_version()}; elastic-transport/{__version__})"
    )


def client_meta_version(version: str) -> str:
    """Converts a Python version into a version string
    compatible with the ``X-Elastic-Client-Meta`` HTTP header.
    """
    match = re.match(r"^([0-9][0-9.]*[0-9]|[0-9])(.*)$", version)
    if match is None:
        raise ValueError(
            "Version {version!r} not formatted like a Python version string"
        )
    version, version_suffix = match.groups()

    # Don't treat post-releases as pre-releases.
    if re.search(r"^\.post[0-9]*$", version_suffix):
        return version
    if version_suffix:
        version += "p"
    return version


@dataclasses.dataclass(frozen=True, repr=True)
class CloudId:
    #: Name of the cluster in Elastic Cloud
    cluster_name: str
    #: Host and port of the Elasticsearch instance
    es_address: Optional[Tuple[str, int]]
    #: Host and port of the Kibana instance
    kibana_address: Optional[Tuple[str, int]]


def parse_cloud_id(cloud_id: str) -> CloudId:
    """Parses an Elastic Cloud ID into its components"""
    try:
        cloud_id = to_str(cloud_id)
        cluster_name, _, cloud_id = cloud_id.partition(":")
        parts = to_str(binascii.a2b_base64(to_bytes(cloud_id, "ascii")), "ascii").split(
            "$"
        )
        parent_dn = parts[0]
        if not parent_dn:
            raise ValueError()  # Caught and re-raised properly below

        es_uuid: Optional[str]
        kibana_uuid: Optional[str]
        try:
            es_uuid = parts[1]
        except IndexError:
            es_uuid = None
        try:
            kibana_uuid = parts[2] or None
        except IndexError:
            kibana_uuid = None

        if ":" in parent_dn:
            parent_dn, _, parent_port = parent_dn.rpartition(":")
            port = int(parent_port)
        else:
            port = 443
    except (ValueError, IndexError, UnicodeError):
        raise ValueError("Cloud ID is not properly formatted") from None

    es_host = f"{es_uuid}.{parent_dn}" if es_uuid else None
    kibana_host = f"{kibana_uuid}.{parent_dn}" if kibana_uuid else None

    return CloudId(
        cluster_name=cluster_name,
        es_address=(es_host, port) if es_host else None,
        kibana_address=(kibana_host, port) if kibana_host else None,
    )


def to_str(
    value: Union[str, bytes], encoding: str = "utf-8", errors: str = "strict"
) -> str:
    if isinstance(value, bytes):
        return value.decode(encoding, errors)
    return value


def to_bytes(
    value: Union[str, bytes], encoding: str = "utf-8", errors: str = "strict"
) -> bytes:
    if isinstance(value, str):
        return value.encode(encoding, errors)
    return value


# Python 3.7 added '~' to the safe list for urllib.parse.quote()
_QUOTE_ALWAYS_SAFE = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-~"
)


def percent_encode(
    string: Union[bytes, str],
    safe: str = "/",
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> str:
    """Percent-encodes a string so it can be used in an HTTP request target"""
    # Redefines 'urllib.parse.quote()' to always have the '~' character
    # within the 'ALWAYS_SAFE' list. The character was added in Python 3.7
    safe = "".join(_QUOTE_ALWAYS_SAFE.union(set(safe)))
    return _quote(string, safe, encoding=encoding, errors=errors)  # type: ignore[arg-type]


def basic_auth_to_header(basic_auth: Tuple[str, str]) -> str:
    """Converts a 2-tuple into a 'Basic' HTTP Authorization header"""
    if (
        not isinstance(basic_auth, tuple)
        or len(basic_auth) != 2
        or any(not isinstance(item, (str, bytes)) for item in basic_auth)
    ):
        raise ValueError(
            "'basic_auth' must be a 2-tuple of str/bytes (username, password)"
        )
    return f"Basic {base64.b64encode((b':'.join(to_bytes(x) for x in basic_auth))).decode()}"


def url_to_node_config(
    url: str, use_default_ports_for_scheme: bool = False
) -> NodeConfig:
    """Constructs a :class:`elastic_transport.NodeConfig` instance from a URL.
    If a username/password are specified in the URL they are converted to an
    'Authorization' header. Always fills in a default port for HTTPS.

    :param url: URL to transform into a NodeConfig.
    :param use_default_ports_for_scheme: If 'True' will resolve default ports for HTTP.
    """
    try:
        parsed_url = parse_url(url)
    except LocationParseError:
        raise ValueError(f"Could not parse URL {url!r}") from None

    parsed_port: Optional[int] = parsed_url.port
    if parsed_url.port is None and parsed_url.scheme is not None:
        # Always fill in a default port for HTTPS
        if parsed_url.scheme == "https":
            parsed_port = 443
        # Only fill HTTP default port when asked to explicitly
        elif parsed_url.scheme == "http" and use_default_ports_for_scheme:
            parsed_port = 80

    if any(
        component in (None, "")
        for component in (parsed_url.scheme, parsed_url.host, parsed_port)
    ):
        raise ValueError(
            "URL must include a 'scheme', 'host', and 'port' component (ie 'https://localhost:9200')"
        )
    assert parsed_url.scheme is not None
    assert parsed_url.host is not None
    assert parsed_port is not None

    headers = {}
    if parsed_url.auth:
        # `urllib3.util.url_parse` ensures `parsed_url` is correctly
        # percent-encoded but does not percent-decode userinfo, so we have to
        # do it ourselves to build the basic auth header correctly.
        encoded_username, _, encoded_password = parsed_url.auth.partition(":")
        username = urllib.parse.unquote(encoded_username)
        password = urllib.parse.unquote(encoded_password)

        headers["authorization"] = basic_auth_to_header((username, password))

    host = parsed_url.host.strip("[]")
    if not parsed_url.path or parsed_url.path == "/":
        path_prefix = ""
    else:
        path_prefix = parsed_url.path

    return NodeConfig(
        scheme=parsed_url.scheme,
        host=host,
        port=parsed_port,
        path_prefix=path_prefix,
        headers=headers,
    )


fixup_module_metadata(__name__, globals())
del fixup_module_metadata
