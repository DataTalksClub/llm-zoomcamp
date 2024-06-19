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
import base64
import functools
import gzip
import os
import re
import ssl
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
    import aiohttp
    import aiohttp.client_exceptions as aiohttp_exceptions

    _AIOHTTP_AVAILABLE = True
    _AIOHTTP_META_VERSION = client_meta_version(aiohttp.__version__)

    _version_parts = []
    for _version_part in aiohttp.__version__.split(".")[:3]:
        try:
            _version_parts.append(int(re.search(r"^([0-9]+)", _version_part).group(1)))  # type: ignore[union-attr]
        except (AttributeError, ValueError):
            break
    _AIOHTTP_SEMVER_VERSION = tuple(_version_parts)

    # See aio-libs/aiohttp#1769 and #5012
    _AIOHTTP_FIXED_HEAD_BUG = _AIOHTTP_SEMVER_VERSION >= (3, 7, 0)
except ImportError:  # pragma: nocover
    _AIOHTTP_AVAILABLE = False
    _AIOHTTP_META_VERSION = ""
    _AIOHTTP_FIXED_HEAD_BUG = False


class AiohttpHttpNode(BaseAsyncNode):
    """Default asynchronous node class using the ``aiohttp`` library via HTTP"""

    _CLIENT_META_HTTP_CLIENT = ("ai", _AIOHTTP_META_VERSION)

    def __init__(self, config: NodeConfig):
        if not _AIOHTTP_AVAILABLE:  # pragma: nocover
            raise ValueError("You must have 'aiohttp' installed to use AiohttpHttpNode")

        super().__init__(config)

        self._ssl_assert_fingerprint = config.ssl_assert_fingerprint
        ssl_context: Optional[ssl.SSLContext] = None
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

        self._loop: asyncio.AbstractEventLoop = None  # type: ignore[assignment]
        self.session: Optional[aiohttp.ClientSession] = None

        # Parameters for creating an aiohttp.ClientSession later.
        self._connections_per_node = config.connections_per_node
        self._ssl_context = ssl_context

    async def perform_request(  # type: ignore[override]
        self,
        method: str,
        target: str,
        body: Optional[bytes] = None,
        headers: Optional[HttpHeaders] = None,
        request_timeout: Union[DefaultType, Optional[float]] = DEFAULT,
    ) -> NodeApiResponse:
        global _AIOHTTP_FIXED_HEAD_BUG
        if self.session is None:
            self._create_aiohttp_session()
        assert self.session is not None

        url = self.base_url + target

        is_head = False
        # There is a bug in aiohttp<3.7 that disables the re-use
        # of the connection in the pool when method=HEAD.
        # See: aio-libs/aiohttp#1769
        if method == "HEAD" and not _AIOHTTP_FIXED_HEAD_BUG:
            method = "GET"
            is_head = True

        # total=0 means no timeout for aiohttp
        resolved_timeout: Optional[float] = (
            self.config.request_timeout
            if request_timeout is DEFAULT
            else request_timeout
        )
        aiohttp_timeout = aiohttp.ClientTimeout(
            total=resolved_timeout if resolved_timeout is not None else 0
        )

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

        kwargs = {}
        if self._ssl_assert_fingerprint:
            kwargs["ssl"] = aiohttp_fingerprint(self._ssl_assert_fingerprint)

        try:
            start = self._loop.time()
            async with self.session.request(
                method,
                url,
                data=body_to_send,
                headers=request_headers,
                timeout=aiohttp_timeout,
                **kwargs,
            ) as response:
                if is_head:  # We actually called 'GET' so throw away the data.
                    await response.release()
                    raw_data = b""
                else:
                    raw_data = await response.read()
                duration = self._loop.time() - start

        # We want to reraise a cancellation or recursion error.
        except RERAISE_EXCEPTIONS:
            raise
        except Exception as e:
            err: Exception
            if isinstance(
                e, (asyncio.TimeoutError, aiohttp_exceptions.ServerTimeoutError)
            ):
                err = ConnectionTimeout(
                    "Connection timed out during request", errors=(e,)
                )
            elif isinstance(e, (ssl.SSLError, aiohttp_exceptions.ClientSSLError)):
                err = TlsError(str(e), errors=(e,))
            elif isinstance(e, BUILTIN_EXCEPTIONS):
                raise
            else:
                err = ConnectionError(str(e), errors=(e,))
            self._log_request(
                method="HEAD" if is_head else method,
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
            headers=HttpHeaders(response.headers),
        )
        self._log_request(
            method="HEAD" if is_head else method,
            target=target,
            headers=request_headers,
            body=body,
            meta=meta,
            response=raw_data,
        )
        return NodeApiResponse(
            meta,
            raw_data,
        )

    async def close(self) -> None:  # type: ignore[override]
        if self.session:
            await self.session.close()
            self.session = None

    def _create_aiohttp_session(self) -> None:
        """Creates an aiohttp.ClientSession(). This is delayed until
        the first call to perform_request() so that AsyncTransport has
        a chance to set AiohttpHttpNode.loop
        """
        if self._loop is None:
            self._loop = asyncio.get_running_loop()
        self.session = aiohttp.ClientSession(
            headers=self.headers,
            skip_auto_headers=("accept", "accept-encoding", "user-agent"),
            auto_decompress=True,
            loop=self._loop,
            cookie_jar=aiohttp.DummyCookieJar(),
            connector=aiohttp.TCPConnector(
                limit_per_host=self._connections_per_node,
                use_dns_cache=True,
                enable_cleanup_closed=True,
                ssl=self._ssl_context or False,
            ),
        )


@functools.lru_cache(maxsize=64, typed=True)
def aiohttp_fingerprint(ssl_assert_fingerprint: str) -> "aiohttp.Fingerprint":
    """Changes 'ssl_assert_fingerprint' into a configured 'aiohttp.Fingerprint' instance.
    Uses a cache to prevent creating tons of objects needlessly.
    """
    return aiohttp.Fingerprint(
        base64.b16decode(ssl_assert_fingerprint.replace(":", ""), casefold=True)
    )
