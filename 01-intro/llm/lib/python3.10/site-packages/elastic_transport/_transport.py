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
import inspect
import logging
import time
import warnings
from platform import python_version
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    List,
    Mapping,
    NamedTuple,
    Optional,
    Tuple,
    Type,
    Union,
    cast,
)

from ._compat import Lock, warn_stacklevel
from ._exceptions import (
    ConnectionError,
    ConnectionTimeout,
    SniffingError,
    TransportError,
    TransportWarning,
)
from ._models import (
    DEFAULT,
    ApiResponseMeta,
    DefaultType,
    HttpHeaders,
    NodeConfig,
    SniffOptions,
)
from ._node import (
    AiohttpHttpNode,
    BaseNode,
    HttpxAsyncHttpNode,
    RequestsHttpNode,
    Urllib3HttpNode,
)
from ._node_pool import NodePool, NodeSelector
from ._otel import OpenTelemetrySpan
from ._serializer import DEFAULT_SERIALIZERS, Serializer, SerializerCollection
from ._version import __version__
from .client_utils import client_meta_version, resolve_default

# Allows for using a node_class by name rather than import.
NODE_CLASS_NAMES: Dict[str, Type[BaseNode]] = {
    "urllib3": Urllib3HttpNode,
    "requests": RequestsHttpNode,
    "aiohttp": AiohttpHttpNode,
    "httpxasync": HttpxAsyncHttpNode,
}
# These are HTTP status errors that shouldn't be considered
# 'errors' for marking a node as dead. These errors typically
# mean everything is fine server-wise and instead the API call
# in question responded successfully.
NOT_DEAD_NODE_HTTP_STATUSES = {None, 400, 401, 402, 403, 404, 409}
DEFAULT_CLIENT_META_SERVICE = ("et", client_meta_version(__version__))

_logger = logging.getLogger("elastic_transport.transport")


class TransportApiResponse(NamedTuple):
    meta: ApiResponseMeta
    body: Any


class Transport:
    """
    Encapsulation of transport-related to logic. Handles instantiation of the
    individual nodes as well as creating a node pool to hold them.

    Main interface is the :meth:`elastic_transport.Transport.perform_request` method.
    """

    def __init__(
        self,
        node_configs: List[NodeConfig],
        node_class: Union[str, Type[BaseNode]] = Urllib3HttpNode,
        node_pool_class: Type[NodePool] = NodePool,
        randomize_nodes_in_pool: bool = True,
        node_selector_class: Optional[Union[str, Type[NodeSelector]]] = None,
        dead_node_backoff_factor: Optional[float] = None,
        max_dead_node_backoff: Optional[float] = None,
        serializers: Optional[Mapping[str, Serializer]] = None,
        default_mimetype: str = "application/json",
        max_retries: int = 3,
        retry_on_status: Collection[int] = (429, 502, 503, 504),
        retry_on_timeout: bool = False,
        sniff_on_start: bool = False,
        sniff_before_requests: bool = False,
        sniff_on_node_failure: bool = False,
        sniff_timeout: Optional[float] = 0.5,
        min_delay_between_sniffing: float = 10.0,
        sniff_callback: Optional[
            Callable[
                ["Transport", "SniffOptions"],
                Union[List[NodeConfig], List[NodeConfig]],
            ]
        ] = None,
        meta_header: bool = True,
        client_meta_service: Tuple[str, str] = DEFAULT_CLIENT_META_SERVICE,
    ):
        """
        :arg node_configs: List of 'NodeConfig' instances to create initial set of nodes.
        :arg node_class: subclass of :class:`~elastic_transport.BaseNode` to use
            or the name of the Connection (ie 'urllib3', 'requests')
        :arg node_pool_class: subclass of :class:`~elastic_transport.NodePool` to use
        :arg randomize_nodes_in_pool: Set to false to not randomize nodes within the pool.
            Defaults to true.
        :arg node_selector_class: Class to be used to select nodes within
            the :class:`~elastic_transport.NodePool`.
        :arg dead_node_backoff_factor: Exponential backoff factor to calculate the amount
            of time to timeout a node after an unsuccessful API call.
        :arg max_dead_node_backoff: Maximum amount of time to timeout a node after an
            unsuccessful API call.
        :arg serializers: optional dict of serializer instances that will be
            used for deserializing data coming from the server. (key is the mimetype)
        :arg max_retries: Maximum number of retries for an API call.
            Set to 0 to disable retries. Defaults to ``0``.
        :arg retry_on_status: set of HTTP status codes on which we should retry
            on a different node. defaults to ``(429, 502, 503, 504)``
        :arg retry_on_timeout: should timeout trigger a retry on different
            node? (default ``False``)
        :arg sniff_on_start: If ``True`` will sniff for additional nodes as soon
            as possible, guaranteed before the first request.
        :arg sniff_on_node_failure: If ``True`` will sniff for additional nodees
            after a node is marked as dead in the pool.
        :arg sniff_before_requests: If ``True`` will occasionally sniff for additional
            nodes as requests are sent.
        :arg sniff_timeout: Timeout value in seconds to use for sniffing requests.
            Defaults to 1 second.
        :arg min_delay_between_sniffing: Number of seconds to wait between calls to
            :meth:`elastic_transport.Transport.sniff` to avoid sniffing too frequently.
            Defaults to 10 seconds.
        :arg sniff_callback: Function that is passed a :class:`elastic_transport.Transport` and
            :class:`elastic_transport.SniffOptions` and should do node discovery and
            return a list of :class:`elastic_transport.NodeConfig` instances.
        :arg meta_header: If set to False the ``X-Elastic-Client-Meta`` HTTP header won't be sent.
            Defaults to True.
        :arg client_meta_service: Key-value pair for the service field of the client metadata header.
            Defaults to the service key-value for Elastic Transport.
        """
        if isinstance(node_class, str):
            if node_class not in NODE_CLASS_NAMES:
                options = "', '".join(sorted(NODE_CLASS_NAMES.keys()))
                raise ValueError(
                    f"Unknown option for node_class: '{node_class}'. "
                    f"Available options are: '{options}'"
                )
            node_class = NODE_CLASS_NAMES[node_class]

        # Verify that the node_class we're passed is
        # async/sync the same as the transport is.
        is_transport_async = inspect.iscoroutinefunction(self.perform_request)
        is_node_async = inspect.iscoroutinefunction(node_class.perform_request)
        if is_transport_async != is_node_async:
            raise ValueError(
                f"Specified 'node_class' {'is' if is_node_async else 'is not'} async, "
                f"should be {'async' if is_transport_async else 'sync'} instead"
            )

        validate_sniffing_options(
            node_configs=node_configs,
            sniff_on_start=sniff_on_start,
            sniff_before_requests=sniff_before_requests,
            sniff_on_node_failure=sniff_on_node_failure,
            sniff_callback=sniff_callback,
        )

        # Create the default metadata for the x-elastic-client-meta
        # HTTP header. Only requires adding the (service, service_version)
        # tuple to the beginning of the client_meta
        self._transport_client_meta: Tuple[Tuple[str, str], ...] = (
            client_meta_service,
            ("py", client_meta_version(python_version())),
            ("t", client_meta_version(__version__)),
        )

        # Grab the 'HTTP_CLIENT_META' property from the node class
        http_client_meta = cast(
            Optional[Tuple[str, str]],
            getattr(node_class, "_CLIENT_META_HTTP_CLIENT", None),
        )
        if http_client_meta:
            self._transport_client_meta += (http_client_meta,)

        if not isinstance(meta_header, bool):
            raise TypeError("'meta_header' must be of type bool")
        self.meta_header = meta_header

        # serialization config
        _serializers = DEFAULT_SERIALIZERS.copy()
        # if custom serializers map has been supplied, override the defaults with it
        if serializers:
            _serializers.update(serializers)
        # Create our collection of serializers
        self.serializers = SerializerCollection(
            _serializers, default_mimetype=default_mimetype
        )

        # Set of default request options
        self.max_retries = max_retries
        self.retry_on_status = retry_on_status
        self.retry_on_timeout = retry_on_timeout

        # Build the NodePool from all the options
        node_pool_kwargs: Dict[str, Any] = {}
        if node_selector_class is not None:
            node_pool_kwargs["node_selector_class"] = node_selector_class
        if dead_node_backoff_factor is not None:
            node_pool_kwargs["dead_node_backoff_factor"] = dead_node_backoff_factor
        if max_dead_node_backoff is not None:
            node_pool_kwargs["max_dead_node_backoff"] = max_dead_node_backoff
        self.node_pool: NodePool = node_pool_class(
            node_configs,
            node_class=node_class,
            randomize_nodes=randomize_nodes_in_pool,
            **node_pool_kwargs,
        )

        self._sniff_on_start = sniff_on_start
        self._sniff_before_requests = sniff_before_requests
        self._sniff_on_node_failure = sniff_on_node_failure
        self._sniff_timeout = sniff_timeout
        self._sniff_callback = sniff_callback
        self._sniffing_lock = Lock()  # Used to track whether we're currently sniffing.
        self._min_delay_between_sniffing = min_delay_between_sniffing
        self._last_sniffed_at = 0.0

        if sniff_on_start:
            self.sniff(True)

    def perform_request(  # type: ignore[return]
        self,
        method: str,
        target: str,
        *,
        body: Optional[Any] = None,
        headers: Union[Mapping[str, Any], DefaultType] = DEFAULT,
        max_retries: Union[int, DefaultType] = DEFAULT,
        retry_on_status: Union[Collection[int], DefaultType] = DEFAULT,
        retry_on_timeout: Union[bool, DefaultType] = DEFAULT,
        request_timeout: Union[Optional[float], DefaultType] = DEFAULT,
        client_meta: Union[Tuple[Tuple[str, str], ...], DefaultType] = DEFAULT,
        otel_span: Union[OpenTelemetrySpan, DefaultType] = DEFAULT,
    ) -> TransportApiResponse:
        """
        Perform the actual request. Retrieve a node from the node
        pool, pass all the information to it's perform_request method and
        return the data.

        If an exception was raised, mark the node as failed and retry (up
        to ``max_retries`` times).

        If the operation was successful and the node used was previously
        marked as dead, mark it as live, resetting it's failure count.

        :arg method: HTTP method to use
        :arg target: HTTP request target
        :arg body: body of the request, will be serialized using serializer and
            passed to the node
        :arg headers: Additional headers to send with the request.
        :arg max_retries: Maximum number of retries before giving up on a request.
            Set to ``0`` to disable retries.
        :arg retry_on_status: Collection of HTTP status codes to retry.
        :arg retry_on_timeout: Set to true to retry after timeout errors.
        :arg request_timeout: Amount of time to wait for a response to fail with a timeout error.
        :arg client_meta: Extra client metadata key-value pairs to send in the client meta header.
        :arg otel_span: OpenTelemetry span used to add metadata to the span.

        :returns: Tuple of the :class:`elastic_transport.ApiResponseMeta` with the deserialized response.
        """
        if headers is DEFAULT:
            request_headers = HttpHeaders()
        else:
            request_headers = HttpHeaders(headers)
        max_retries = resolve_default(max_retries, self.max_retries)
        retry_on_timeout = resolve_default(retry_on_timeout, self.retry_on_timeout)
        retry_on_status = resolve_default(retry_on_status, self.retry_on_status)
        otel_span = resolve_default(otel_span, OpenTelemetrySpan(None))

        if self.meta_header:
            request_headers["x-elastic-client-meta"] = ",".join(
                f"{k}={v}"
                for k, v in self._transport_client_meta
                + resolve_default(client_meta, ())
            )

        # Serialize the request body to bytes based on the given mimetype.
        request_body: Optional[bytes]
        if body is not None:
            if "content-type" not in request_headers:
                raise ValueError(
                    "Must provide a 'Content-Type' header to requests with bodies"
                )
            request_body = self.serializers.dumps(
                body, mimetype=request_headers["content-type"]
            )
            otel_span.set_db_statement(request_body)
        else:
            request_body = None

        # Errors are stored from (oldest->newest)
        errors: List[Exception] = []

        for attempt in range(max_retries + 1):
            # If we sniff before requests are made we want to do so before
            # 'node_pool.get()' is called so our sniffed nodes show up in the pool.
            if self._sniff_before_requests:
                self.sniff(False)

            retry = False
            node_failure = False
            last_response: Optional[TransportApiResponse] = None
            node = self.node_pool.get()
            start_time = time.time()
            try:
                otel_span.set_node_metadata(node.host, node.port, node.base_url, target)
                resp = node.perform_request(
                    method,
                    target,
                    body=request_body,
                    headers=request_headers,
                    request_timeout=request_timeout,
                )
                _logger.info(
                    "%s %s%s [status:%s duration:%.3fs]"
                    % (
                        method,
                        node.base_url,
                        target,
                        resp.meta.status,
                        time.time() - start_time,
                    )
                )

                if method != "HEAD":
                    body = self.serializers.loads(resp.body, resp.meta.mimetype)
                else:
                    body = None

                if resp.meta.status in retry_on_status:
                    retry = True
                    # Keep track of the last response we see so we can return
                    # it in case the retried request returns with a transport error.
                    last_response = TransportApiResponse(resp.meta, body)

            except TransportError as e:
                _logger.info(
                    "%s %s%s [status:%s duration:%.3fs]"
                    % (
                        method,
                        node.base_url,
                        target,
                        "N/A",
                        time.time() - start_time,
                    )
                )

                if isinstance(e, ConnectionTimeout):
                    retry = retry_on_timeout
                    node_failure = True
                elif isinstance(e, ConnectionError):
                    retry = True
                    node_failure = True

                # If the error was determined to be a node failure
                # we mark it dead in the node pool to allow for
                # other nodes to be retried.
                if node_failure:
                    self.node_pool.mark_dead(node)

                    if self._sniff_on_node_failure:
                        try:
                            self.sniff(False)
                        except TransportError:
                            # If sniffing on failure, it could fail too. Catch the
                            # exception not to interrupt the retries.
                            pass

                if not retry or attempt >= max_retries:
                    # Since we're exhausted but we have previously
                    # received some sort of response from the API
                    # we should forward that along instead of the
                    # transport error. Likely to be more actionable.
                    if last_response is not None:
                        return last_response

                    e.errors = tuple(errors)
                    raise
                else:
                    _logger.warning(
                        "Retrying request after failure (attempt %d of %d)",
                        attempt,
                        max_retries,
                        exc_info=e,
                    )
                    errors.append(e)

            else:
                # If we got back a response we need to check if that status
                # is indicative of a healthy node even if it's a non-2XX status
                if (
                    200 <= resp.meta.status < 299
                    or resp.meta.status in NOT_DEAD_NODE_HTTP_STATUSES
                ):
                    self.node_pool.mark_live(node)
                else:
                    self.node_pool.mark_dead(node)

                    if self._sniff_on_node_failure:
                        try:
                            self.sniff(False)
                        except TransportError:
                            # If sniffing on failure, it could fail too. Catch the
                            # exception not to interrupt the retries.
                            pass

                # We either got a response we're happy with or
                # we've exhausted all of our retries so we return it.
                if not retry or attempt >= max_retries:
                    return TransportApiResponse(resp.meta, body)
                else:
                    _logger.warning(
                        "Retrying request after non-successful status %d (attempt %d of %d)",
                        resp.meta.status,
                        attempt,
                        max_retries,
                    )

    def sniff(self, is_initial_sniff: bool = False) -> None:
        previously_sniffed_at = self._last_sniffed_at
        should_sniff = self._should_sniff(is_initial_sniff)
        try:
            if should_sniff:
                _logger.info("Started sniffing for additional nodes")
                self._last_sniffed_at = time.time()

                options = SniffOptions(
                    is_initial_sniff=is_initial_sniff, sniff_timeout=self._sniff_timeout
                )
                assert self._sniff_callback is not None
                node_configs = self._sniff_callback(self, options)
                if not node_configs and is_initial_sniff:
                    raise SniffingError(
                        "No viable nodes were discovered on the initial sniff attempt"
                    )

                prev_node_pool_size = len(self.node_pool)
                for node_config in node_configs:
                    self.node_pool.add(node_config)

                # Do some math to log which nodes are new/existing
                sniffed_nodes = len(node_configs)
                new_nodes = sniffed_nodes - (len(self.node_pool) - prev_node_pool_size)
                existing_nodes = sniffed_nodes - new_nodes
                _logger.debug(
                    "Discovered %d nodes during sniffing (%d new nodes, %d already in pool)",
                    sniffed_nodes,
                    new_nodes,
                    existing_nodes,
                )

        # If sniffing failed for any reason we
        # want to allow retrying immediately.
        except Exception as e:
            _logger.warning("Encountered an error during sniffing", exc_info=e)
            self._last_sniffed_at = previously_sniffed_at
            raise

        # If we started a sniff we need to release the lock.
        finally:
            if should_sniff:
                self._sniffing_lock.release()

    def close(self) -> None:
        """
        Explicitly closes all nodes in the transport's pool
        """
        for node in self.node_pool.all():
            node.close()

    def _should_sniff(self, is_initial_sniff: bool) -> bool:
        """Decide if we should sniff or not. If we return ``True`` from this
        method the caller has a responsibility to unlock the ``_sniffing_lock``
        """
        if not is_initial_sniff and (
            time.time() - self._last_sniffed_at < self._min_delay_between_sniffing
        ):
            return False
        return self._sniffing_lock.acquire(False)


def validate_sniffing_options(
    *,
    node_configs: List[NodeConfig],
    sniff_before_requests: bool,
    sniff_on_start: bool,
    sniff_on_node_failure: bool,
    sniff_callback: Optional[Any],
) -> None:
    """Validates the Transport configurations for sniffing"""

    sniffing_enabled = sniff_before_requests or sniff_on_start or sniff_on_node_failure
    if sniffing_enabled and not sniff_callback:
        raise ValueError("Enabling sniffing requires specifying a 'sniff_callback'")
    if not sniffing_enabled and sniff_callback:
        raise ValueError(
            "Using 'sniff_callback' requires enabling sniffing via 'sniff_on_start', "
            "'sniff_before_requests' or 'sniff_on_node_failure'"
        )

    # If we're sniffing we want to warn the user for non-homogenous NodeConfigs.
    if sniffing_enabled and len(node_configs) > 1:
        warn_if_varying_node_config_options(node_configs)


def warn_if_varying_node_config_options(node_configs: List[NodeConfig]) -> None:
    """Function which detects situations when sniffing may produce incorrect configs"""
    exempt_attrs = {"host", "port", "connections_per_node", "_extras"}
    match_attr_dict = None
    for node_config in node_configs:
        attr_dict = {
            k: v
            for k, v in dataclasses.asdict(node_config).items()
            if k not in exempt_attrs
        }
        if match_attr_dict is None:
            match_attr_dict = attr_dict

        # Detected two nodes that have different config, warn the user.
        elif match_attr_dict != attr_dict:
            warnings.warn(
                "Detected NodeConfig instances with different options. "
                "It's recommended to keep all options except for "
                "'host' and 'port' the same for sniffing to work reliably.",
                category=TransportWarning,
                stacklevel=warn_stacklevel(),
            )
