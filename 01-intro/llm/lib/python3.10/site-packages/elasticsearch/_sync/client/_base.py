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

import re
import warnings
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    Union,
)

from elastic_transport import (
    ApiResponse,
    BinaryApiResponse,
    HeadApiResponse,
    HttpHeaders,
    ListApiResponse,
    NodeConfig,
    ObjectApiResponse,
    OpenTelemetrySpan,
    SniffOptions,
    TextApiResponse,
    Transport,
)
from elastic_transport.client_utils import DEFAULT, DefaultType

from ..._otel import OpenTelemetry
from ..._version import __versionstr__
from ...compat import warn_stacklevel
from ...exceptions import (
    HTTP_EXCEPTIONS,
    ApiError,
    ConnectionError,
    ElasticsearchWarning,
    SerializationError,
    UnsupportedProductError,
)
from .utils import _TYPE_SYNC_SNIFF_CALLBACK, _base64_auth_header, _quote_query

_WARNING_RE = re.compile(r"\"([^\"]*)\"")
_COMPAT_MIMETYPE_TEMPLATE = "application/vnd.elasticsearch+%s; compatible-with=" + str(
    __versionstr__.partition(".")[0]
)
_COMPAT_MIMETYPE_RE = re.compile(r"application/(json|x-ndjson|vnd\.mapbox-vector-tile)")
_COMPAT_MIMETYPE_SUB = _COMPAT_MIMETYPE_TEMPLATE % (r"\g<1>",)


def resolve_auth_headers(
    headers: Optional[Mapping[str, str]],
    http_auth: Union[DefaultType, None, Tuple[str, str], str] = DEFAULT,
    api_key: Union[DefaultType, None, Tuple[str, str], str] = DEFAULT,
    basic_auth: Union[DefaultType, None, Tuple[str, str], str] = DEFAULT,
    bearer_auth: Union[DefaultType, None, str] = DEFAULT,
) -> HttpHeaders:
    if headers is None:
        headers = HttpHeaders()
    elif not isinstance(headers, HttpHeaders):
        headers = HttpHeaders(headers)

    resolved_http_auth = http_auth if http_auth is not DEFAULT else None
    resolved_basic_auth = basic_auth if basic_auth is not DEFAULT else None
    if resolved_http_auth is not None:
        if resolved_basic_auth is not None:
            raise ValueError(
                "Can't specify both 'http_auth' and 'basic_auth', "
                "instead only specify 'basic_auth'"
            )
        if isinstance(http_auth, str) or (
            isinstance(resolved_http_auth, (list, tuple))
            and all(isinstance(x, str) for x in resolved_http_auth)
        ):
            resolved_basic_auth = resolved_http_auth
        else:
            raise TypeError(
                "The deprecated 'http_auth' parameter must be either 'Tuple[str, str]' or 'str'. "
                "Use either the 'basic_auth' parameter instead"
            )

        warnings.warn(
            "The 'http_auth' parameter is deprecated. "
            "Use 'basic_auth' or 'bearer_auth' parameters instead",
            category=DeprecationWarning,
            stacklevel=warn_stacklevel(),
        )

    resolved_api_key = api_key if api_key is not DEFAULT else None
    resolved_bearer_auth = bearer_auth if bearer_auth is not DEFAULT else None
    if resolved_api_key or resolved_basic_auth or resolved_bearer_auth:
        if (
            sum(
                x is not None
                for x in (
                    resolved_api_key,
                    resolved_basic_auth,
                    resolved_bearer_auth,
                )
            )
            > 1
        ):
            raise ValueError(
                "Can only set one of 'api_key', 'basic_auth', and 'bearer_auth'"
            )
        if headers and headers.get("authorization", None) is not None:
            raise ValueError(
                "Can't set 'Authorization' HTTP header with other authentication options"
            )
        if resolved_api_key:
            headers["authorization"] = f"ApiKey {_base64_auth_header(resolved_api_key)}"
        if resolved_basic_auth:
            headers["authorization"] = (
                f"Basic {_base64_auth_header(resolved_basic_auth)}"
            )
        if resolved_bearer_auth:
            headers["authorization"] = f"Bearer {resolved_bearer_auth}"

    return headers


def create_sniff_callback(
    host_info_callback: Optional[
        Callable[[Dict[str, Any], Dict[str, Any]], Optional[Dict[str, Any]]]
    ] = None,
    sniffed_node_callback: Optional[
        Callable[[Dict[str, Any], NodeConfig], Optional[NodeConfig]]
    ] = None,
) -> _TYPE_SYNC_SNIFF_CALLBACK:
    assert (host_info_callback is None) != (sniffed_node_callback is None)

    # Wrap the deprecated 'host_info_callback' into 'sniffed_node_callback'
    if host_info_callback is not None:

        def _sniffed_node_callback(
            node_info: Dict[str, Any], node_config: NodeConfig
        ) -> Optional[NodeConfig]:
            assert host_info_callback is not None
            if (
                host_info_callback(  # type ignore[misc]
                    node_info, {"host": node_config.host, "port": node_config.port}
                )
                is None
            ):
                return None
            return node_config

        sniffed_node_callback = _sniffed_node_callback

    def sniff_callback(
        transport: Transport, sniff_options: SniffOptions
    ) -> List[NodeConfig]:
        for _ in transport.node_pool.all():
            try:
                meta, node_infos = transport.perform_request(
                    "GET",
                    "/_nodes/_all/http",
                    headers={
                        "accept": "application/vnd.elasticsearch+json; compatible-with=8"
                    },
                    request_timeout=(
                        sniff_options.sniff_timeout
                        if not sniff_options.is_initial_sniff
                        else None
                    ),
                )
            except (SerializationError, ConnectionError):
                continue

            if not 200 <= meta.status <= 299:
                continue

            node_configs = []
            for node_info in node_infos.get("nodes", {}).values():
                address = node_info.get("http", {}).get("publish_address")
                if not address or ":" not in address:
                    continue

                if "/" in address:
                    # Support 7.x host/ip:port behavior where http.publish_host has been set.
                    fqdn, ipaddress = address.split("/", 1)
                    host = fqdn
                    _, port_str = ipaddress.rsplit(":", 1)
                    port = int(port_str)
                else:
                    host, port_str = address.rsplit(":", 1)
                    port = int(port_str)

                assert sniffed_node_callback is not None
                sniffed_node = sniffed_node_callback(
                    node_info, meta.node.replace(host=host, port=port)
                )
                if sniffed_node is None:
                    continue

                # Use the node which was able to make the request as a base.
                node_configs.append(sniffed_node)

            if node_configs:
                return node_configs

        return []

    return sniff_callback


def _default_sniffed_node_callback(
    node_info: Dict[str, Any], node_config: NodeConfig
) -> Optional[NodeConfig]:
    if node_info.get("roles", []) == ["master"]:
        return None
    return node_config


default_sniff_callback = create_sniff_callback(
    sniffed_node_callback=_default_sniffed_node_callback
)


class BaseClient:
    def __init__(self, _transport: Transport) -> None:
        self._transport = _transport
        self._client_meta: Union[DefaultType, Tuple[Tuple[str, str], ...]] = DEFAULT
        self._headers = HttpHeaders()
        self._request_timeout: Union[DefaultType, Optional[float]] = DEFAULT
        self._ignore_status: Union[DefaultType, Collection[int]] = DEFAULT
        self._max_retries: Union[DefaultType, int] = DEFAULT
        self._retry_on_timeout: Union[DefaultType, bool] = DEFAULT
        self._retry_on_status: Union[DefaultType, Collection[int]] = DEFAULT
        self._verified_elasticsearch = False
        self._otel = OpenTelemetry()

    @property
    def transport(self) -> Transport:
        return self._transport

    def perform_request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        body: Optional[Any] = None,
        endpoint_id: Optional[str] = None,
        path_parts: Optional[Mapping[str, Any]] = None,
    ) -> ApiResponse[Any]:
        with self._otel.span(
            method,
            endpoint_id=endpoint_id,
            path_parts=path_parts or {},
        ) as otel_span:
            response = self._perform_request(
                method,
                path,
                params=params,
                headers=headers,
                body=body,
                otel_span=otel_span,
            )
            otel_span.set_elastic_cloud_metadata(response.meta.headers)
            return response

    def _perform_request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        body: Optional[Any] = None,
        otel_span: OpenTelemetrySpan,
    ) -> ApiResponse[Any]:
        if headers:
            request_headers = self._headers.copy()
            request_headers.update(headers)
        else:
            request_headers = self._headers

        def mimetype_header_to_compat(header: str) -> None:
            # Converts all parts of a Accept/Content-Type headers
            # from application/X -> application/vnd.elasticsearch+X
            nonlocal request_headers
            mimetype = request_headers.get(header, None)
            if mimetype:
                request_headers[header] = _COMPAT_MIMETYPE_RE.sub(
                    _COMPAT_MIMETYPE_SUB, mimetype
                )

        mimetype_header_to_compat("Accept")
        mimetype_header_to_compat("Content-Type")

        if params:
            target = f"{path}?{_quote_query(params)}"
        else:
            target = path

        meta, resp_body = self.transport.perform_request(
            method,
            target,
            headers=request_headers,
            body=body,
            request_timeout=self._request_timeout,
            max_retries=self._max_retries,
            retry_on_status=self._retry_on_status,
            retry_on_timeout=self._retry_on_timeout,
            client_meta=self._client_meta,
            otel_span=otel_span,
        )

        # HEAD with a 404 is returned as a normal response
        # since this is used as an 'exists' functionality.
        if not (method == "HEAD" and meta.status == 404) and (
            not 200 <= meta.status < 299
            and (
                self._ignore_status is DEFAULT
                or self._ignore_status is None
                or meta.status not in self._ignore_status
            )
        ):
            message = str(resp_body)

            # If the response is an error response try parsing
            # the raw Elasticsearch error before raising.
            if isinstance(resp_body, dict):
                try:
                    error = resp_body.get("error", message)
                    if isinstance(error, dict) and "type" in error:
                        error = error["type"]
                    message = error
                except (ValueError, KeyError, TypeError):
                    pass

            raise HTTP_EXCEPTIONS.get(meta.status, ApiError)(
                message=message, meta=meta, body=resp_body
            )

        # 'X-Elastic-Product: Elasticsearch' should be on every 2XX response.
        if not self._verified_elasticsearch:
            # If the header is set we mark the server as verified.
            if meta.headers.get("x-elastic-product", "") == "Elasticsearch":
                self._verified_elasticsearch = True
            # Otherwise we only raise an error on 2XX responses.
            elif meta.status >= 200 and meta.status < 300:
                raise UnsupportedProductError(
                    message=(
                        "The client noticed that the server is not Elasticsearch "
                        "and we do not support this unknown product"
                    ),
                    meta=meta,
                    body=resp_body,
                )

        # 'Warning' headers should be reraised as 'ElasticsearchWarning'
        if "warning" in meta.headers:
            warning_header = (meta.headers.get("warning") or "").strip()
            warning_messages: Iterable[str] = _WARNING_RE.findall(warning_header) or (
                warning_header,
            )
            stacklevel = warn_stacklevel()
            for warning_message in warning_messages:
                warnings.warn(
                    warning_message,
                    category=ElasticsearchWarning,
                    stacklevel=stacklevel,
                )

        if method == "HEAD":
            response = HeadApiResponse(meta=meta)
        elif isinstance(resp_body, dict):
            response = ObjectApiResponse(body=resp_body, meta=meta)  # type: ignore[assignment]
        elif isinstance(resp_body, list):
            response = ListApiResponse(body=resp_body, meta=meta)  # type: ignore[assignment]
        elif isinstance(resp_body, str):
            response = TextApiResponse(  # type: ignore[assignment]
                body=resp_body,
                meta=meta,
            )
        elif isinstance(resp_body, bytes):
            response = BinaryApiResponse(body=resp_body, meta=meta)  # type: ignore[assignment]
        else:
            response = ApiResponse(body=resp_body, meta=meta)  # type: ignore[assignment]

        return response


class NamespacedClient(BaseClient):
    def __init__(self, client: "BaseClient") -> None:
        self._client = client
        super().__init__(self._client.transport)

    def perform_request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        body: Optional[Any] = None,
        endpoint_id: Optional[str] = None,
        path_parts: Optional[Mapping[str, Any]] = None,
    ) -> ApiResponse[Any]:
        # Use the internal clients .perform_request() implementation
        # so we take advantage of their transport options.
        return self._client.perform_request(
            method,
            path,
            params=params,
            headers=headers,
            body=body,
            endpoint_id=endpoint_id,
            path_parts=path_parts,
        )
