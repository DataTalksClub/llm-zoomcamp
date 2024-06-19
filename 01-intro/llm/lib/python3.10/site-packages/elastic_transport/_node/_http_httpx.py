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

import gzip
import os.path
import ssl
import time
import warnings
from typing import Optional, Union

from .._compat import warn_stacklevel
from .._exceptions import ConnectionError, ConnectionTimeout, SecurityWarning, TlsError
from .._models import ApiResponseMeta, HttpHeaders, NodeConfig
from ..client_utils import DEFAULT, DefaultType, client_meta_version
from ._base import (
    BUILTIN_EXCEPTIONS,
    DEFAULT_CA_CERTS,
    RERAISE_EXCEPTIONS,
    NodeApiResponse,
    ssl_context_from_node_config,
)
from ._base_async import BaseAsyncNode

try:
    import httpx

    _HTTPX_AVAILABLE = True
    _HTTPX_META_VERSION = client_meta_version(httpx.__version__)
except ImportError:
    _HTTPX_AVAILABLE = False
    _HTTPX_META_VERSION = ""


class HttpxAsyncHttpNode(BaseAsyncNode):
    _CLIENT_META_HTTP_CLIENT = ("hx", _HTTPX_META_VERSION)

    def __init__(self, config: NodeConfig):
        if not _HTTPX_AVAILABLE:  # pragma: nocover
            raise ValueError("You must have 'httpx' installed to use HttpxNode")
        super().__init__(config)

        if config.ssl_assert_fingerprint:
            raise ValueError(
                "httpx does not support certificate pinning. https://github.com/encode/httpx/issues/761"
            )

        # TODO switch to Literal[False] when dropping Python 3.7 support
        ssl_context: Union[ssl.SSLContext, bool] = False
        if config.scheme == "https":
            if config.ssl_context is not None:
                ssl_context = ssl_context_from_node_config(config)
            else:
                ssl_context = ssl_context_from_node_config(config)

                ca_certs = (
                    DEFAULT_CA_CERTS if config.ca_certs is None else config.ca_certs
                )
                if config.verify_certs:
                    if not ca_certs:
                        raise ValueError(
                            "Root certificates are missing for certificate "
                            "validation. Either pass them in using the ca_certs parameter or "
                            "install certifi to use it automatically."
                        )
                else:
                    if config.ssl_show_warn:
                        warnings.warn(
                            f"Connecting to {self.base_url!r} using TLS with verify_certs=False is insecure",
                            stacklevel=warn_stacklevel(),
                            category=SecurityWarning,
                        )

                if ca_certs is not None:
                    if os.path.isfile(ca_certs):
                        ssl_context.load_verify_locations(cafile=ca_certs)
                    elif os.path.isdir(ca_certs):
                        ssl_context.load_verify_locations(capath=ca_certs)
                    else:
                        raise ValueError("ca_certs parameter is not a path")

                # Use client_cert and client_key variables for SSL certificate configuration.
                if config.client_cert and not os.path.isfile(config.client_cert):
                    raise ValueError("client_cert is not a path to a file")
                if config.client_key and not os.path.isfile(config.client_key):
                    raise ValueError("client_key is not a path to a file")
                if config.client_cert and config.client_key:
                    ssl_context.load_cert_chain(config.client_cert, config.client_key)
                elif config.client_cert:
                    ssl_context.load_cert_chain(config.client_cert)

        self.client = httpx.AsyncClient(
            base_url=f"{config.scheme}://{config.host}:{config.port}",
            limits=httpx.Limits(max_connections=config.connections_per_node),
            verify=ssl_context or False,
            timeout=config.request_timeout,
        )

    async def perform_request(  # type: ignore[override]
        self,
        method: str,
        target: str,
        body: Optional[bytes] = None,
        headers: Optional[HttpHeaders] = None,
        request_timeout: Union[DefaultType, Optional[float]] = DEFAULT,
    ) -> NodeApiResponse:
        resolved_headers = self._headers.copy()
        if headers:
            resolved_headers.update(headers)

        if body:
            if self._http_compress:
                resolved_body = gzip.compress(body)
                resolved_headers["content-encoding"] = "gzip"
            else:
                resolved_body = body
        else:
            resolved_body = None

        try:
            start = time.perf_counter()
            if request_timeout is DEFAULT:
                resp = await self.client.request(
                    method,
                    target,
                    content=resolved_body,
                    headers=dict(resolved_headers),
                )
            else:
                resp = await self.client.request(
                    method,
                    target,
                    content=resolved_body,
                    headers=dict(resolved_headers),
                    timeout=request_timeout,
                )
            resp.raise_for_status()
            response_body = resp.read()
            duration = time.perf_counter() - start
        except RERAISE_EXCEPTIONS + BUILTIN_EXCEPTIONS:
            raise
        except Exception as e:
            err: Exception
            if isinstance(e, (TimeoutError, httpx.TimeoutException)):
                err = ConnectionTimeout(
                    "Connection timed out during request", errors=(e,)
                )
            elif isinstance(e, ssl.SSLError):
                err = TlsError(str(e), errors=(e,))
            else:
                err = ConnectionError(str(e), errors=(e,))
            self._log_request(
                method=method,
                target=target,
                headers=resolved_headers,
                body=body,
                exception=err,
            )
            raise err from None

        meta = ApiResponseMeta(
            resp.status_code,
            resp.http_version,
            HttpHeaders(resp.headers),
            duration,
            self.config,
        )

        self._log_request(
            method=method,
            target=target,
            headers=resolved_headers,
            body=body,
            meta=meta,
            response=response_body,
        )

        return NodeApiResponse(meta, response_body)

    async def close(self) -> None:  # type: ignore[override]
        await self.client.aclose()
