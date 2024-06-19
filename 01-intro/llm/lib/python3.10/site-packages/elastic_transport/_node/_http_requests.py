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
import ssl
import time
import warnings
from typing import Any, Optional, Union

import urllib3

from .._compat import warn_stacklevel
from .._exceptions import ConnectionError, ConnectionTimeout, SecurityWarning, TlsError
from .._models import ApiResponseMeta, HttpHeaders, NodeConfig
from ..client_utils import DEFAULT, DefaultType, client_meta_version
from ._base import (
    BUILTIN_EXCEPTIONS,
    RERAISE_EXCEPTIONS,
    BaseNode,
    NodeApiResponse,
    ssl_context_from_node_config,
)

try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.auth import AuthBase

    _REQUESTS_AVAILABLE = True
    _REQUESTS_META_VERSION = client_meta_version(requests.__version__)

    # Use our custom HTTPSConnectionPool for chain cert fingerprint support.
    try:
        from ._urllib3_chain_certs import HTTPSConnectionPool
    except (ImportError, AttributeError):
        HTTPSConnectionPool = urllib3.HTTPSConnectionPool  # type: ignore[assignment,misc]

    class _ElasticHTTPAdapter(HTTPAdapter):
        def __init__(self, node_config: NodeConfig, **kwargs: Any) -> None:
            self._node_config = node_config
            super().__init__(**kwargs)

        def init_poolmanager(
            self,
            connections: Any,
            maxsize: int,
            block: bool = False,
            **pool_kwargs: Any,
        ) -> None:
            if self._node_config.scheme == "https":
                ssl_context = ssl_context_from_node_config(self._node_config)
                pool_kwargs.setdefault("ssl_context", ssl_context)

                # Fingerprint verification doesn't require CA certificates being loaded.
                # We also want to disable other verification methods as we only care
                # about the fingerprint of the certificates, not whether they form
                # a verified chain to a trust anchor.
                if self._node_config.ssl_assert_fingerprint:
                    # Manually disable these in the right order on the SSLContext
                    # so urllib3 won't think we want conflicting things.
                    ssl_context.check_hostname = False
                    ssl_context.verify_mode = ssl.CERT_NONE

                    pool_kwargs["assert_fingerprint"] = (
                        self._node_config.ssl_assert_fingerprint
                    )
                    pool_kwargs["cert_reqs"] = "CERT_NONE"
                    pool_kwargs["assert_hostname"] = False

            super().init_poolmanager(connections, maxsize, block=block, **pool_kwargs)  # type: ignore [no-untyped-call]
            self.poolmanager.pool_classes_by_scheme["https"] = HTTPSConnectionPool

except ImportError:  # pragma: nocover
    _REQUESTS_AVAILABLE = False
    _REQUESTS_META_VERSION = ""


class RequestsHttpNode(BaseNode):
    """Synchronous node using the ``requests`` library communicating via HTTP.

    Supports setting :attr:`requests.Session.auth` via the
    :attr:`elastic_transport.NodeConfig._extras`
    using the ``requests.session.auth`` key.
    """

    _CLIENT_META_HTTP_CLIENT = ("rq", _REQUESTS_META_VERSION)

    def __init__(self, config: NodeConfig):
        if not _REQUESTS_AVAILABLE:  # pragma: nocover
            raise ValueError(
                "You must have 'requests' installed to use RequestsHttpNode"
            )

        super().__init__(config)

        # Initialize Session so .headers works before calling super().__init__().
        self.session = requests.Session()
        self.session.headers.clear()  # Empty out all the default session headers

        if config.scheme == "https":
            # If we're using ssl_assert_fingerprint we don't want
            # to verify certificates the typical way. Instead we
            # rely on the custom ElasticHTTPAdapter and urllib3.
            if config.ssl_assert_fingerprint:
                self.session.verify = False

            # Otherwise we go the traditional route of verifying certs.
            else:
                if config.ca_certs:
                    if not config.verify_certs:
                        raise ValueError(
                            "You cannot use 'ca_certs' when 'verify_certs=False'"
                        )
                    self.session.verify = config.ca_certs
                else:
                    self.session.verify = config.verify_certs

                if not config.ssl_show_warn:
                    urllib3.disable_warnings()

                if (
                    config.scheme == "https"
                    and not config.verify_certs
                    and config.ssl_show_warn
                ):
                    warnings.warn(
                        f"Connecting to {self.base_url!r} using TLS with verify_certs=False is insecure",
                        stacklevel=warn_stacklevel(),
                        category=SecurityWarning,
                    )

        # Requests supports setting 'session.auth' via _extras['requests.session.auth'] = ...
        try:
            requests_session_auth: Optional[AuthBase] = config._extras.pop(
                "requests.session.auth", None
            )
        except AttributeError:
            requests_session_auth = None
        if requests_session_auth is not None:
            self.session.auth = requests_session_auth

        # Client certificates
        if config.client_cert:
            if config.client_key:
                self.session.cert = (config.client_cert, config.client_key)
            else:
                self.session.cert = config.client_cert

        # Create and mount custom adapter for constraining number of connections
        adapter = _ElasticHTTPAdapter(
            node_config=config,
            pool_connections=config.connections_per_node,
            pool_maxsize=config.connections_per_node,
            pool_block=True,
        )
        # Preload the HTTPConnectionPool so initialization issues
        # are raised here instead of in perform_request()
        if hasattr(adapter, "get_connection_with_tls_context"):
            request = requests.Request(method="GET", url=self.base_url)
            prepared_request = self.session.prepare_request(request)
            adapter.get_connection_with_tls_context(
                prepared_request, verify=self.session.verify
            )
        else:
            # elastic-transport is not vulnerable to CVE-2024-35195 because it uses
            # requests.Session and an SSLContext without using the verify parameter.
            # We should remove this branch when requiring requests 2.32 or later.
            adapter.get_connection(self.base_url)

        self.session.mount(prefix=f"{self.scheme}://", adapter=adapter)

    def perform_request(
        self,
        method: str,
        target: str,
        body: Optional[bytes] = None,
        headers: Optional[HttpHeaders] = None,
        request_timeout: Union[DefaultType, Optional[float]] = DEFAULT,
    ) -> NodeApiResponse:
        url = self.base_url + target
        headers = HttpHeaders(headers or ())

        request_headers = self._headers.copy()
        if headers:
            request_headers.update(headers)

        body_to_send: Optional[bytes]
        if body:
            if self._http_compress:
                body_to_send = gzip.compress(body)
                request_headers["content-encoding"] = "gzip"
            else:
                body_to_send = body
        else:
            body_to_send = None

        start = time.time()
        request = requests.Request(
            method=method, headers=request_headers, url=url, data=body_to_send
        )
        prepared_request = self.session.prepare_request(request)
        send_kwargs = {
            "timeout": (
                request_timeout
                if request_timeout is not DEFAULT
                else self.config.request_timeout
            )
        }
        send_kwargs.update(
            self.session.merge_environment_settings(  # type: ignore[arg-type]
                prepared_request.url, {}, None, None, None
            )
        )
        try:
            response = self.session.send(prepared_request, **send_kwargs)  # type: ignore[arg-type]
            data = response.content
            duration = time.time() - start
            response_headers = HttpHeaders(response.headers)

        except RERAISE_EXCEPTIONS:
            raise
        except Exception as e:
            err: Exception
            if isinstance(e, requests.Timeout):
                err = ConnectionTimeout(
                    "Connection timed out during request", errors=(e,)
                )
            elif isinstance(e, (ssl.SSLError, requests.exceptions.SSLError)):
                err = TlsError(str(e), errors=(e,))
            elif isinstance(e, BUILTIN_EXCEPTIONS):
                raise
            else:
                err = ConnectionError(str(e), errors=(e,))
            self._log_request(
                method=method,
                target=target,
                headers=request_headers,
                body=body,
                exception=err,
            )
            raise err from None

        meta = ApiResponseMeta(
            node=self.config,
            duration=duration,
            http_version="1.1",
            status=response.status_code,
            headers=response_headers,
        )
        self._log_request(
            method=method,
            target=target,
            headers=request_headers,
            body=body,
            meta=meta,
            response=data,
        )
        return NodeApiResponse(
            meta,
            data,
        )

    def close(self) -> None:
        """
        Explicitly closes connections
        """
        self.session.close()
