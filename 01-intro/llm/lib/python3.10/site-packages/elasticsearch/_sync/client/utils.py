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
import inspect
import urllib.parse
import warnings
from datetime import date, datetime
from functools import wraps
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Collection,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from elastic_transport import (
    AsyncTransport,
    HttpHeaders,
    NodeConfig,
    RequestsHttpNode,
    SniffOptions,
    Transport,
)
from elastic_transport.client_utils import (
    DEFAULT,
    client_meta_version,
    create_user_agent,
    parse_cloud_id,
    url_to_node_config,
)

from ..._version import __versionstr__
from ...compat import to_bytes, to_str, warn_stacklevel

if TYPE_CHECKING:
    from ._base import NamespacedClient

# parts of URL to be omitted
SKIP_IN_PATH: Collection[Any] = (None, "", b"", [], ())

# To be passed to 'client_meta_service' on the Transport
CLIENT_META_SERVICE = ("es", client_meta_version(__versionstr__))

# Default User-Agent used by the client
USER_AGENT = create_user_agent("elasticsearch-py", __versionstr__)

_TYPE_HOSTS = Union[
    str, Sequence[Union[str, Mapping[str, Union[str, int]], NodeConfig]]
]

_TYPE_BODY = Union[bytes, str, Dict[str, Any]]

_TYPE_ASYNC_SNIFF_CALLBACK = Callable[
    [AsyncTransport, SniffOptions], Awaitable[List[NodeConfig]]
]
_TYPE_SYNC_SNIFF_CALLBACK = Callable[[Transport, SniffOptions], List[NodeConfig]]

_TRANSPORT_OPTIONS = {
    "api_key",
    "http_auth",
    "request_timeout",
    "opaque_id",
    "headers",
    "ignore",
}

F = TypeVar("F", bound=Callable[..., Any])


def client_node_configs(
    hosts: Optional[_TYPE_HOSTS],
    cloud_id: Optional[str],
    requests_session_auth: Optional[Any] = None,
    **kwargs: Any,
) -> List[NodeConfig]:
    if cloud_id is not None:
        if hosts is not None:
            raise ValueError(
                "The 'cloud_id' and 'hosts' parameters are mutually exclusive"
            )
        node_configs = cloud_id_to_node_configs(cloud_id)
    else:
        assert hosts is not None
        node_configs = hosts_to_node_configs(hosts)

    # Remove all values which are 'DEFAULT' to avoid overwriting actual defaults.
    node_options = {k: v for k, v in kwargs.items() if v is not DEFAULT}

    # Set the 'User-Agent' default header.
    headers = HttpHeaders(node_options.pop("headers", ()))
    headers.setdefault("user-agent", USER_AGENT)
    node_options["headers"] = headers

    # If a custom Requests AuthBase is passed we set that via '_extras'.
    if requests_session_auth is not None:
        node_options.setdefault("_extras", {})[
            "requests.session.auth"
        ] = requests_session_auth

    def apply_node_options(node_config: NodeConfig) -> NodeConfig:
        """Needs special handling of headers since .replace() wipes out existing headers"""
        nonlocal node_options
        headers = node_config.headers.copy()  # type: ignore[attr-defined]

        headers_to_add = node_options.pop("headers", ())
        if headers_to_add:
            headers.update(headers_to_add)

        headers.setdefault("user-agent", USER_AGENT)
        headers.freeze()
        node_options["headers"] = headers
        return node_config.replace(**node_options)

    return [apply_node_options(node_config) for node_config in node_configs]


def hosts_to_node_configs(hosts: _TYPE_HOSTS) -> List[NodeConfig]:
    """Transforms the many formats of 'hosts' into NodeConfigs"""

    # To make the logic here simpler we reroute everything to be List[X]
    if isinstance(hosts, str):
        return hosts_to_node_configs([hosts])

    node_configs: List[NodeConfig] = []
    for host in hosts:
        if isinstance(host, NodeConfig):
            node_configs.append(host)

        elif isinstance(host, str):
            node_configs.append(url_to_node_config(host))

        elif isinstance(host, Mapping):
            node_configs.append(host_mapping_to_node_config(host))
        else:
            raise ValueError(
                "'hosts' must be a list of URLs, NodeConfigs, or dictionaries"
            )

    return node_configs


def host_mapping_to_node_config(host: Mapping[str, Union[str, int]]) -> NodeConfig:
    """Converts an old-style dictionary host specification to a NodeConfig"""

    allow_hosts_keys = {
        "scheme",
        "host",
        "port",
        "path_prefix",
        "url_prefix",
        "use_ssl",
    }
    disallowed_keys = set(host.keys()).difference(allow_hosts_keys)
    if disallowed_keys:
        bad_keys_used = "', '".join(sorted(disallowed_keys))
        allowed_keys = "', '".join(sorted(allow_hosts_keys))
        raise ValueError(
            f"Can't specify the options '{bad_keys_used}' via a "
            f"dictionary in 'hosts', only '{allowed_keys}' options "
            "are allowed"
        )

    options = dict(host)

    # Handle the deprecated option 'use_ssl'
    if "use_ssl" in options:
        use_ssl = options.pop("use_ssl")
        if not isinstance(use_ssl, bool):
            raise TypeError("'use_ssl' must be of type 'bool'")

        # Ensure the user isn't specifying scheme=http use_ssl=True or vice-versa
        if "scheme" in options and (options["scheme"] == "https") != use_ssl:
            raise ValueError(
                f"Cannot specify conflicting options 'scheme={options['scheme']}' "
                f"and 'use_ssl={use_ssl}'. Use 'scheme' only instead"
            )

        warnings.warn(
            "The 'use_ssl' option is no longer needed as specifying a 'scheme' is now required",
            category=DeprecationWarning,
            stacklevel=warn_stacklevel(),
        )
        options.setdefault("scheme", "https" if use_ssl else "http")

    # Handle the deprecated option 'url_prefix'
    if "url_prefix" in options:
        if "path_prefix" in options:
            raise ValueError(
                "Cannot specify conflicting options 'url_prefix' and "
                "'path_prefix'. Use 'path_prefix' only instead"
            )

        warnings.warn(
            "The 'url_prefix' option is deprecated in favor of 'path_prefix'",
            category=DeprecationWarning,
            stacklevel=warn_stacklevel(),
        )
        options["path_prefix"] = options.pop("url_prefix")

    return NodeConfig(**options)  # type: ignore


def cloud_id_to_node_configs(cloud_id: str) -> List[NodeConfig]:
    """Transforms an Elastic Cloud ID into a NodeConfig"""
    es_addr = parse_cloud_id(cloud_id).es_address
    if es_addr is None or not all(es_addr):
        raise ValueError("Cloud ID missing host and port information for Elasticsearch")
    host, port = es_addr
    return [
        NodeConfig(
            scheme="https",
            host=host,
            port=port,
            http_compress=True,
        )
    ]


def _base64_auth_header(auth_value: Union[str, List[str], Tuple[str, str]]) -> str:
    """Takes either a 2-tuple or a base64-encoded string
    and returns a base64-encoded string to be used
    as an HTTP authorization header.
    """
    if isinstance(auth_value, (list, tuple)):
        return base64.b64encode(to_bytes(":".join(auth_value))).decode("ascii")
    return to_str(auth_value)


def _escape(value: Any) -> str:
    """
    Escape a single value of a URL string or a query parameter. If it is a list
    or tuple, turn it into a comma-separated string first.
    """

    # make sequences into comma-separated stings
    if isinstance(value, (list, tuple)):
        value = ",".join([_escape(item) for item in value])

    # dates and datetimes into isoformat
    elif isinstance(value, (date, datetime)):
        value = value.isoformat()

    # make bools into true/false strings
    elif isinstance(value, bool):
        value = str(value).lower()

    elif isinstance(value, bytes):
        return value.decode("utf-8", "surrogatepass")

    if not isinstance(value, str):
        return str(value)
    return value


def _quote(value: Any) -> str:
    return urllib.parse.quote(_escape(value), ",*")


def _quote_query(query: Mapping[str, Any]) -> str:
    return "&".join([f"{k}={_quote(v)}" for k, v in query.items()])


def _merge_kwargs_no_duplicates(kwargs: Dict[str, Any], values: Dict[str, Any]) -> None:
    for key, val in values.items():
        if key in kwargs:
            raise ValueError(
                f"Received multiple values for '{key}', specify parameters "
                "directly instead of using 'params'"
            )
        kwargs[key] = val


def _merge_body_fields_no_duplicates(
    body: _TYPE_BODY, kwargs: Dict[str, Any], body_fields: Tuple[str, ...]
) -> bool:
    mixed_body_and_params = False
    for key in list(kwargs.keys()):
        if key in body_fields:
            if isinstance(body, (str, bytes)):
                raise ValueError(
                    "Couldn't merge 'body' with other parameters as it wasn't a mapping."
                )

            if key in body:
                raise ValueError(
                    f"Received multiple values for '{key}', specify parameters "
                    "using either body or parameters, not both."
                )

            warnings.warn(
                f"Received '{key}' via a specific parameter in the presence of a "
                "'body' parameter, which is deprecated and will be removed in a future "
                "version. Instead, use only 'body' or only specific parameters.",
                category=DeprecationWarning,
                stacklevel=warn_stacklevel(),
            )
            body[key] = kwargs.pop(key)
            mixed_body_and_params = True
    return mixed_body_and_params


def _rewrite_parameters(
    body_name: Optional[str] = None,
    body_fields: Optional[Tuple[str, ...]] = None,
    parameter_aliases: Optional[Dict[str, str]] = None,
    ignore_deprecated_options: Optional[Set[str]] = None,
) -> Callable[[F], F]:
    def wrapper(api: F) -> F:
        @wraps(api)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            nonlocal api, body_name, body_fields

            # Let's give a nicer error message when users pass positional arguments.
            if len(args) >= 2:
                raise TypeError(
                    "Positional arguments can't be used with Elasticsearch API methods. "
                    "Instead only use keyword arguments."
                )

            # We merge 'params' first as transport options can be specified using params.
            if "params" in kwargs and (
                not ignore_deprecated_options
                or "params" not in ignore_deprecated_options
            ):
                params = kwargs.pop("params")
                if params:
                    if not hasattr(params, "items"):
                        raise ValueError(
                            "Couldn't merge 'params' with other parameters as it wasn't a mapping. "
                            "Instead of using 'params' use individual API parameters"
                        )
                    warnings.warn(
                        "The 'params' parameter is deprecated and will be removed "
                        "in a future version. Instead use individual parameters.",
                        category=DeprecationWarning,
                        stacklevel=warn_stacklevel(),
                    )
                    _merge_kwargs_no_duplicates(kwargs, params)

            maybe_transport_options = _TRANSPORT_OPTIONS.intersection(kwargs)
            if maybe_transport_options:
                transport_options = {}
                for option in maybe_transport_options:
                    if (
                        ignore_deprecated_options
                        and option in ignore_deprecated_options
                    ):
                        continue
                    try:
                        option_rename = option
                        if option == "ignore":
                            option_rename = "ignore_status"
                        transport_options[option_rename] = kwargs.pop(option)
                    except KeyError:
                        pass
                if transport_options:
                    warnings.warn(
                        "Passing transport options in the API method is deprecated. Use 'Elasticsearch.options()' instead.",
                        category=DeprecationWarning,
                        stacklevel=warn_stacklevel(),
                    )
                    client = args[0]

                    # Namespaced clients need to unwrapped.
                    namespaced_client: Optional[Type["NamespacedClient"]] = None
                    if hasattr(client, "_client"):
                        namespaced_client = type(client)
                        client = client._client

                    client = client.options(**transport_options)

                    # Re-wrap the client if we unwrapped due to being namespaced.
                    if namespaced_client is not None:
                        client = namespaced_client(client)
                    args = (client,) + args[1:]

            if "body" in kwargs and (
                not ignore_deprecated_options or "body" not in ignore_deprecated_options
            ):
                body: Optional[_TYPE_BODY] = kwargs.pop("body")
                mixed_body_and_params = False
                if body is not None:
                    if body_name:
                        if body_name in kwargs:
                            raise TypeError(
                                f"Can't use '{body_name}' and 'body' parameters together because '{body_name}' "
                                "is an alias for 'body'. Instead you should only use the "
                                f"'{body_name}' parameter. See https://github.com/elastic/elasticsearch-py/"
                                "issues/1698 for more information"
                            )
                        kwargs[body_name] = body
                    elif body_fields is not None:
                        mixed_body_and_params = _merge_body_fields_no_duplicates(
                            body, kwargs, body_fields
                        )
                        kwargs["body"] = body

                    if parameter_aliases and not isinstance(body, (str, bytes)):
                        for alias, rename_to in parameter_aliases.items():
                            if rename_to in body:
                                body[alias] = body.pop(rename_to)
                                # If body and params are mixed, the alias may come from a param,
                                # in which case the warning below will not make sense.
                                if not mixed_body_and_params:
                                    warnings.warn(
                                        f"Using '{rename_to}' alias in 'body' is deprecated and will be removed "
                                        f"in a future version of elasticsearch-py. Use '{alias}' directly instead. "
                                        "See https://github.com/elastic/elasticsearch-py/issues/1698 for more information",
                                        category=DeprecationWarning,
                                        stacklevel=2,
                                    )

            if parameter_aliases:
                for alias, rename_to in parameter_aliases.items():
                    try:
                        kwargs[rename_to] = kwargs.pop(alias)
                    except KeyError:
                        pass

            return api(*args, **kwargs)

        return wrapped  # type: ignore[return-value]

    return wrapper


def is_requests_http_auth(http_auth: Any) -> bool:
    """Detect if an http_auth value is a custom Requests auth object"""
    try:
        from requests.auth import AuthBase

        return isinstance(http_auth, AuthBase)
    except ImportError:
        pass
    return False


def is_requests_node_class(node_class: Any) -> bool:
    """Detect if 'RequestsHttpNode' would be used given the setting of 'node_class'"""
    return (
        node_class is not None
        and node_class is not DEFAULT
        and (
            node_class == "requests"
            or (
                inspect.isclass(node_class) and issubclass(node_class, RequestsHttpNode)
            )
        )
    )
