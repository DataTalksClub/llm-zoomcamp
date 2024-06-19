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
from typing import Any, Dict, Optional, Union

try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata  # type: ignore[no-redef]

import urllib3
from urllib3.exceptions import ConnectTimeoutError, NewConnectionError, ReadTimeoutError
from urllib3.util.retry import Retry

from .._compat import warn_stacklevel
from .._exceptions import ConnectionError, ConnectionTimeout, SecurityWarning, TlsError
from .._models import ApiResponseMeta, HttpHeaders, NodeConfig
from ..client_utils import DEFAULT, DefaultType, client_meta_version
from ._base import (
    BUILTIN_EXCEPTIONS,
    DEFAULT_CA_CERTS,
    RERAISE_EXCEPTIONS,
    BaseNode,
    NodeApiResponse,
    ssl_context_from_node_config,
)

try:
    from ._urllib3_chain_certs import HTTPSConnectionPool
except (ImportError, AttributeError):
    HTTPSConnectionPool = urllib3.HTTPSConnectionPool  # type: ignore[assignment,misc]


class Urllib3HttpNode(BaseNode):
    """Default synchronous node class using the ``urllib3`` library via HTTP"""

    _CLIENT_META_HTTP_CLIENT = ("ur", client_meta_version(metadata.version("urllib3")))

    def __init__(self, config: NodeConfig):
        super().__init__(config)

        pool_class = urllib3.HTTPConnectionPool
        kw: Dict[str, Any] = {}

        if config.scheme == "https":
            pool_class = HTTPSConnectionPool
            ssl_context = ssl_context_from_node_config(config)
            kw["ssl_context"] = ssl_context

            if config.ssl_assert_hostname and config.ssl_assert_fingerprint:
                raise ValueError(
                    "Can't specify both 'ssl_assert_hostname' and 'ssl_assert_fingerprint'"
                )

            # Fingerprint verification doesn't require CA certificates being loaded.
            # We also want to disable other verification methods as we only care
            # about the fingerprint of the certificates, not whether they form
            # a verified chain to a trust anchor.
            elif config.ssl_assert_fingerprint:
                # Manually disable these in the right order on the SSLContext
                # so urllib3 won't think we want conflicting things.
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE

                kw.update(
                    {
                        "assert_fingerprint": config.ssl_assert_fingerprint,
                        "assert_hostname": False,
                        "cert_reqs": "CERT_NONE",
                    }
                )

            else:
                kw["assert_hostname"] = config.ssl_assert_hostname

                # Convert all sentinel values to their actual default
                # values if not using an SSLContext.
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

                    kw.update(
                        {
                            "cert_reqs": "CERT_REQUIRED",
                            "ca_certs": ca_certs,
                            "cert_file": config.client_cert,
                            "key_file": config.client_key,
                        }
                    )
                else:
                    kw["cert_reqs"] = "CERT_NONE"

                    if config.ssl_show_warn:
                        warnings.warn(
                            f"Connecting to {self.base_url!r} using TLS with verify_certs=False is insecure",
                            stacklevel=warn_stacklevel(),
                            category=SecurityWarning,
                        )
                    else:
                        urllib3.disable_warnings()

        self.pool = pool_class(
            config.host,
            port=config.port,
            timeout=urllib3.Timeout(total=config.request_timeout),
            maxsize=config.connections_per_node,
            block=True,
            **kw,
        )

    def perform_request(
        self,
        method: str,
        target: str,
        body: Optional[bytes] = None,
        headers: Optional[HttpHeaders] = None,
        request_timeout: Union[DefaultType, Optional[float]] = DEFAULT,
    ) -> NodeApiResponse:
        if self.path_prefix:
            target = f"{self.path_prefix}{target}"

        start = time.time()
        try:
            kw = {}
            if request_timeout is not DEFAULT:
                kw["timeout"] = request_timeout

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

            response = self.pool.urlopen(
                method,
                target,
                body=body_to_send,
                retries=Retry(False),
                headers=request_headers,
                **kw,  # type: ignore[arg-type]
            )
            response_headers = HttpHeaders(response.headers)
            data = response.data
            duration = time.time() - start

        except RERAISE_EXCEPTIONS:
            raise
        except Exception as e:
            err: Exception
            if isinstance(e, NewConnectionError):
                err = ConnectionError(str(e), errors=(e,))
            elif isinstance(e, (ConnectTimeoutError, ReadTimeoutError)):
                err = ConnectionTimeout(
                    "Connection timed out during request", errors=(e,)
                )
            elif isinstance(e, (ssl.SSLError, urllib3.exceptions.SSLError)):
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
            status=response.status,
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
        Explicitly closes connection
        """
        self.pool.close()
