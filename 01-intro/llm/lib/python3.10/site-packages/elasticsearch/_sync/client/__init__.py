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


import logging
import typing as t
import warnings

from elastic_transport import (
    BaseNode,
    BinaryApiResponse,
    HeadApiResponse,
    NodeConfig,
    NodePool,
    NodeSelector,
    ObjectApiResponse,
    Serializer,
    Transport,
)
from elastic_transport.client_utils import DEFAULT, DefaultType

from ...exceptions import ApiError, TransportError
from ...serializer import DEFAULT_SERIALIZERS
from ._base import (
    BaseClient,
    create_sniff_callback,
    default_sniff_callback,
    resolve_auth_headers,
)
from .async_search import AsyncSearchClient
from .autoscaling import AutoscalingClient
from .cat import CatClient
from .ccr import CcrClient
from .cluster import ClusterClient
from .dangling_indices import DanglingIndicesClient
from .enrich import EnrichClient
from .eql import EqlClient
from .esql import EsqlClient
from .features import FeaturesClient
from .fleet import FleetClient
from .graph import GraphClient
from .ilm import IlmClient
from .indices import IndicesClient
from .inference import InferenceClient
from .ingest import IngestClient
from .license import LicenseClient
from .logstash import LogstashClient
from .migration import MigrationClient
from .ml import MlClient
from .monitoring import MonitoringClient
from .nodes import NodesClient
from .query_ruleset import QueryRulesetClient
from .rollup import RollupClient
from .search_application import SearchApplicationClient
from .searchable_snapshots import SearchableSnapshotsClient
from .security import SecurityClient
from .shutdown import ShutdownClient
from .slm import SlmClient
from .snapshot import SnapshotClient
from .sql import SqlClient
from .ssl import SslClient
from .synonyms import SynonymsClient
from .tasks import TasksClient
from .text_structure import TextStructureClient
from .transform import TransformClient
from .utils import (
    _TYPE_HOSTS,
    CLIENT_META_SERVICE,
    SKIP_IN_PATH,
    _quote,
    _rewrite_parameters,
    client_node_configs,
    is_requests_http_auth,
    is_requests_node_class,
)
from .watcher import WatcherClient
from .xpack import XPackClient

logger = logging.getLogger("elasticsearch")


SelfType = t.TypeVar("SelfType", bound="Elasticsearch")


class Elasticsearch(BaseClient):
    """
    Elasticsearch low-level client. Provides a straightforward mapping from
    Python to Elasticsearch REST APIs.

    The client instance has additional attributes to update APIs in different
    namespaces such as ``async_search``, ``indices``, ``security``, and more:

    .. code-block:: python

        client = Elasticsearch("http://localhost:9200")

        # Get Document API
        client.get(index="*", id="1")

        # Get Index API
        client.indices.get(index="*")

    Transport options can be set on the client constructor or using
    the :meth:`~elasticsearch.Elasticsearch.options` method:

    .. code-block:: python

        # Set 'api_key' on the constructor
        client = Elasticsearch(
            "http://localhost:9200",
            api_key="api_key",
        )
        client.search(...)

        # Set 'api_key' per request
        client.options(api_key="api_key").search(...)
    """

    def __init__(
        self,
        hosts: t.Optional[_TYPE_HOSTS] = None,
        *,
        # API
        cloud_id: t.Optional[str] = None,
        api_key: t.Optional[t.Union[str, t.Tuple[str, str]]] = None,
        basic_auth: t.Optional[t.Union[str, t.Tuple[str, str]]] = None,
        bearer_auth: t.Optional[str] = None,
        opaque_id: t.Optional[str] = None,
        # Node
        headers: t.Union[DefaultType, t.Mapping[str, str]] = DEFAULT,
        connections_per_node: t.Union[DefaultType, int] = DEFAULT,
        http_compress: t.Union[DefaultType, bool] = DEFAULT,
        verify_certs: t.Union[DefaultType, bool] = DEFAULT,
        ca_certs: t.Union[DefaultType, str] = DEFAULT,
        client_cert: t.Union[DefaultType, str] = DEFAULT,
        client_key: t.Union[DefaultType, str] = DEFAULT,
        ssl_assert_hostname: t.Union[DefaultType, str] = DEFAULT,
        ssl_assert_fingerprint: t.Union[DefaultType, str] = DEFAULT,
        ssl_version: t.Union[DefaultType, int] = DEFAULT,
        ssl_context: t.Union[DefaultType, t.Any] = DEFAULT,
        ssl_show_warn: t.Union[DefaultType, bool] = DEFAULT,
        # Transport
        transport_class: t.Type[Transport] = Transport,
        request_timeout: t.Union[DefaultType, None, float] = DEFAULT,
        node_class: t.Union[DefaultType, t.Type[BaseNode]] = DEFAULT,
        node_pool_class: t.Union[DefaultType, t.Type[NodePool]] = DEFAULT,
        randomize_nodes_in_pool: t.Union[DefaultType, bool] = DEFAULT,
        node_selector_class: t.Union[DefaultType, t.Type[NodeSelector]] = DEFAULT,
        dead_node_backoff_factor: t.Union[DefaultType, float] = DEFAULT,
        max_dead_node_backoff: t.Union[DefaultType, float] = DEFAULT,
        serializer: t.Optional[Serializer] = None,
        serializers: t.Union[DefaultType, t.Mapping[str, Serializer]] = DEFAULT,
        default_mimetype: str = "application/json",
        max_retries: t.Union[DefaultType, int] = DEFAULT,
        retry_on_status: t.Union[DefaultType, int, t.Collection[int]] = DEFAULT,
        retry_on_timeout: t.Union[DefaultType, bool] = DEFAULT,
        sniff_on_start: t.Union[DefaultType, bool] = DEFAULT,
        sniff_before_requests: t.Union[DefaultType, bool] = DEFAULT,
        sniff_on_node_failure: t.Union[DefaultType, bool] = DEFAULT,
        sniff_timeout: t.Union[DefaultType, None, float] = DEFAULT,
        min_delay_between_sniffing: t.Union[DefaultType, None, float] = DEFAULT,
        sniffed_node_callback: t.Optional[
            t.Callable[[t.Dict[str, t.Any], NodeConfig], t.Optional[NodeConfig]]
        ] = None,
        meta_header: t.Union[DefaultType, bool] = DEFAULT,
        timeout: t.Union[DefaultType, None, float] = DEFAULT,
        randomize_hosts: t.Union[DefaultType, bool] = DEFAULT,
        host_info_callback: t.Optional[
            t.Callable[
                [t.Dict[str, t.Any], t.Dict[str, t.Union[str, int]]],
                t.Optional[t.Dict[str, t.Union[str, int]]],
            ]
        ] = None,
        sniffer_timeout: t.Union[DefaultType, None, float] = DEFAULT,
        sniff_on_connection_fail: t.Union[DefaultType, bool] = DEFAULT,
        http_auth: t.Union[DefaultType, t.Any] = DEFAULT,
        maxsize: t.Union[DefaultType, int] = DEFAULT,
        # Internal use only
        _transport: t.Optional[Transport] = None,
    ) -> None:
        if hosts is None and cloud_id is None and _transport is None:
            raise ValueError("Either 'hosts' or 'cloud_id' must be specified")

        if timeout is not DEFAULT:
            if request_timeout is not DEFAULT:
                raise ValueError(
                    "Can't specify both 'timeout' and 'request_timeout', "
                    "instead only specify 'request_timeout'"
                )
            warnings.warn(
                "The 'timeout' parameter is deprecated in favor of 'request_timeout'",
                category=DeprecationWarning,
                stacklevel=2,
            )
            request_timeout = timeout

        if serializer is not None:
            if serializers is not DEFAULT:
                raise ValueError(
                    "Can't specify both 'serializer' and 'serializers' parameters "
                    "together. Instead only specify one of the other."
                )
            serializers = {default_mimetype: serializer}

        if randomize_hosts is not DEFAULT:
            if randomize_nodes_in_pool is not DEFAULT:
                raise ValueError(
                    "Can't specify both 'randomize_hosts' and 'randomize_nodes_in_pool', "
                    "instead only specify 'randomize_nodes_in_pool'"
                )
            warnings.warn(
                "The 'randomize_hosts' parameter is deprecated in favor of 'randomize_nodes_in_pool'",
                category=DeprecationWarning,
                stacklevel=2,
            )
            randomize_nodes_in_pool = randomize_hosts

        if sniffer_timeout is not DEFAULT:
            if min_delay_between_sniffing is not DEFAULT:
                raise ValueError(
                    "Can't specify both 'sniffer_timeout' and 'min_delay_between_sniffing', "
                    "instead only specify 'min_delay_between_sniffing'"
                )
            warnings.warn(
                "The 'sniffer_timeout' parameter is deprecated in favor of 'min_delay_between_sniffing'",
                category=DeprecationWarning,
                stacklevel=2,
            )
            min_delay_between_sniffing = sniffer_timeout

        if sniff_on_connection_fail is not DEFAULT:
            if sniff_on_node_failure is not DEFAULT:
                raise ValueError(
                    "Can't specify both 'sniff_on_connection_fail' and 'sniff_on_node_failure', "
                    "instead only specify 'sniff_on_node_failure'"
                )
            warnings.warn(
                "The 'sniff_on_connection_fail' parameter is deprecated in favor of 'sniff_on_node_failure'",
                category=DeprecationWarning,
                stacklevel=2,
            )
            sniff_on_node_failure = sniff_on_connection_fail

        if maxsize is not DEFAULT:
            if connections_per_node is not DEFAULT:
                raise ValueError(
                    "Can't specify both 'maxsize' and 'connections_per_node', "
                    "instead only specify 'connections_per_node'"
                )
            warnings.warn(
                "The 'maxsize' parameter is deprecated in favor of 'connections_per_node'",
                category=DeprecationWarning,
                stacklevel=2,
            )
            connections_per_node = maxsize

        # Setting min_delay_between_sniffing=True implies sniff_before_requests=True
        if min_delay_between_sniffing is not DEFAULT:
            sniff_before_requests = True

        sniffing_options = (
            sniff_timeout,
            sniff_on_start,
            sniff_before_requests,
            sniff_on_node_failure,
            sniffed_node_callback,
            min_delay_between_sniffing,
            sniffed_node_callback,
        )
        if cloud_id is not None and any(
            x is not DEFAULT and x is not None for x in sniffing_options
        ):
            raise ValueError(
                "Sniffing should not be enabled when connecting to Elastic Cloud"
            )

        sniff_callback = None
        if host_info_callback is not None:
            if sniffed_node_callback is not None:
                raise ValueError(
                    "Can't specify both 'host_info_callback' and 'sniffed_node_callback', "
                    "instead only specify 'sniffed_node_callback'"
                )
            warnings.warn(
                "The 'host_info_callback' parameter is deprecated in favor of 'sniffed_node_callback'",
                category=DeprecationWarning,
                stacklevel=2,
            )

            sniff_callback = create_sniff_callback(
                host_info_callback=host_info_callback
            )
        elif sniffed_node_callback is not None:
            sniff_callback = create_sniff_callback(
                sniffed_node_callback=sniffed_node_callback
            )
        elif (
            sniff_on_start is True
            or sniff_before_requests is True
            or sniff_on_node_failure is True
        ):
            sniff_callback = default_sniff_callback

        if _transport is None:
            requests_session_auth = None
            if http_auth is not None and http_auth is not DEFAULT:
                if is_requests_http_auth(http_auth):
                    # If we're using custom requests authentication
                    # then we need to alert the user that they also
                    # need to use 'node_class=requests'.
                    if not is_requests_node_class(node_class):
                        raise ValueError(
                            "Using a custom 'requests.auth.AuthBase' class for "
                            "'http_auth' must be used with node_class='requests'"
                        )

                    # Reset 'http_auth' to DEFAULT so it's not consumed below.
                    requests_session_auth = http_auth
                    http_auth = DEFAULT

            node_configs = client_node_configs(
                hosts,
                cloud_id=cloud_id,
                requests_session_auth=requests_session_auth,
                connections_per_node=connections_per_node,
                http_compress=http_compress,
                verify_certs=verify_certs,
                ca_certs=ca_certs,
                client_cert=client_cert,
                client_key=client_key,
                ssl_assert_hostname=ssl_assert_hostname,
                ssl_assert_fingerprint=ssl_assert_fingerprint,
                ssl_version=ssl_version,
                ssl_context=ssl_context,
                ssl_show_warn=ssl_show_warn,
            )
            transport_kwargs: t.Dict[str, t.Any] = {}
            if node_class is not DEFAULT:
                transport_kwargs["node_class"] = node_class
            if node_pool_class is not DEFAULT:
                transport_kwargs["node_pool_class"] = node_pool_class
            if randomize_nodes_in_pool is not DEFAULT:
                transport_kwargs["randomize_nodes_in_pool"] = randomize_nodes_in_pool
            if node_selector_class is not DEFAULT:
                transport_kwargs["node_selector_class"] = node_selector_class
            if dead_node_backoff_factor is not DEFAULT:
                transport_kwargs["dead_node_backoff_factor"] = dead_node_backoff_factor
            if max_dead_node_backoff is not DEFAULT:
                transport_kwargs["max_dead_node_backoff"] = max_dead_node_backoff
            if meta_header is not DEFAULT:
                transport_kwargs["meta_header"] = meta_header

            transport_serializers = DEFAULT_SERIALIZERS.copy()
            if serializers is not DEFAULT:
                transport_serializers.update(serializers)

                # Override compatibility serializers from their non-compat mimetypes too.
                # So we use the same serializer for requests and responses.
                for mime_subtype in ("json", "x-ndjson"):
                    if f"application/{mime_subtype}" in serializers:
                        compat_mimetype = (
                            f"application/vnd.elasticsearch+{mime_subtype}"
                        )
                        if compat_mimetype not in serializers:
                            transport_serializers[compat_mimetype] = serializers[
                                f"application/{mime_subtype}"
                            ]

            transport_kwargs["serializers"] = transport_serializers

            transport_kwargs["default_mimetype"] = default_mimetype
            if sniff_on_start is not DEFAULT:
                transport_kwargs["sniff_on_start"] = sniff_on_start
            if sniff_before_requests is not DEFAULT:
                transport_kwargs["sniff_before_requests"] = sniff_before_requests
            if sniff_on_node_failure is not DEFAULT:
                transport_kwargs["sniff_on_node_failure"] = sniff_on_node_failure
            if sniff_timeout is not DEFAULT:
                transport_kwargs["sniff_timeout"] = sniff_timeout
            if min_delay_between_sniffing is not DEFAULT:
                transport_kwargs["min_delay_between_sniffing"] = (
                    min_delay_between_sniffing
                )

            _transport = transport_class(
                node_configs,
                client_meta_service=CLIENT_META_SERVICE,
                sniff_callback=sniff_callback,
                **transport_kwargs,
            )

            super().__init__(_transport)

            # These are set per-request so are stored separately.
            self._request_timeout = request_timeout
            self._max_retries = max_retries
            self._retry_on_timeout = retry_on_timeout
            if isinstance(retry_on_status, int):
                retry_on_status = (retry_on_status,)
            self._retry_on_status = retry_on_status

        else:
            super().__init__(_transport)

        if headers is not DEFAULT and headers is not None:
            self._headers.update(headers)
        if opaque_id is not DEFAULT and opaque_id is not None:  # type: ignore[comparison-overlap]
            self._headers["x-opaque-id"] = opaque_id
        self._headers = resolve_auth_headers(
            self._headers,
            http_auth=http_auth,
            api_key=api_key,
            basic_auth=basic_auth,
            bearer_auth=bearer_auth,
        )

        # namespaced clients for compatibility with API names
        self.async_search = AsyncSearchClient(self)
        self.autoscaling = AutoscalingClient(self)
        self.cat = CatClient(self)
        self.cluster = ClusterClient(self)
        self.fleet = FleetClient(self)
        self.features = FeaturesClient(self)
        self.indices = IndicesClient(self)
        self.inference = InferenceClient(self)
        self.ingest = IngestClient(self)
        self.nodes = NodesClient(self)
        self.snapshot = SnapshotClient(self)
        self.tasks = TasksClient(self)

        self.xpack = XPackClient(self)
        self.ccr = CcrClient(self)
        self.dangling_indices = DanglingIndicesClient(self)
        self.enrich = EnrichClient(self)
        self.eql = EqlClient(self)
        self.esql = EsqlClient(self)
        self.graph = GraphClient(self)
        self.ilm = IlmClient(self)
        self.license = LicenseClient(self)
        self.logstash = LogstashClient(self)
        self.migration = MigrationClient(self)
        self.ml = MlClient(self)
        self.monitoring = MonitoringClient(self)
        self.query_ruleset = QueryRulesetClient(self)
        self.rollup = RollupClient(self)
        self.search_application = SearchApplicationClient(self)
        self.searchable_snapshots = SearchableSnapshotsClient(self)
        self.security = SecurityClient(self)
        self.slm = SlmClient(self)
        self.shutdown = ShutdownClient(self)
        self.sql = SqlClient(self)
        self.ssl = SslClient(self)
        self.synonyms = SynonymsClient(self)
        self.text_structure = TextStructureClient(self)
        self.transform = TransformClient(self)
        self.watcher = WatcherClient(self)

    def __repr__(self) -> str:
        try:
            # get a list of all connections
            nodes = [node.base_url for node in self.transport.node_pool.all()]
            # truncate to 5 if there are too many
            if len(nodes) > 5:
                nodes = nodes[:5] + ["..."]
            return f"<{self.__class__.__name__}({nodes})>"
        except Exception:
            # probably operating on custom transport and connection_pool, ignore
            return super().__repr__()

    def __enter__(self) -> "Elasticsearch":
        try:
            # All this to avoid a Mypy error when using unasync.
            getattr(self.transport, "_async_call")()
        except AttributeError:
            pass
        return self

    def __exit__(self, *_: t.Any) -> None:
        self.close()

    def options(
        self: SelfType,
        *,
        opaque_id: t.Union[DefaultType, str] = DEFAULT,
        api_key: t.Union[DefaultType, str, t.Tuple[str, str]] = DEFAULT,
        basic_auth: t.Union[DefaultType, str, t.Tuple[str, str]] = DEFAULT,
        bearer_auth: t.Union[DefaultType, str] = DEFAULT,
        headers: t.Union[DefaultType, t.Mapping[str, str]] = DEFAULT,
        request_timeout: t.Union[DefaultType, t.Optional[float]] = DEFAULT,
        ignore_status: t.Union[DefaultType, int, t.Collection[int]] = DEFAULT,
        max_retries: t.Union[DefaultType, int] = DEFAULT,
        retry_on_status: t.Union[DefaultType, int, t.Collection[int]] = DEFAULT,
        retry_on_timeout: t.Union[DefaultType, bool] = DEFAULT,
    ) -> SelfType:
        client = type(self)(_transport=self.transport)

        resolved_headers = headers if headers is not DEFAULT else None
        resolved_headers = resolve_auth_headers(
            headers=resolved_headers,
            api_key=api_key,
            basic_auth=basic_auth,
            bearer_auth=bearer_auth,
        )
        resolved_opaque_id = opaque_id if opaque_id is not DEFAULT else None
        if resolved_opaque_id:
            resolved_headers["x-opaque-id"] = resolved_opaque_id

        if resolved_headers:
            new_headers = self._headers.copy()
            new_headers.update(resolved_headers)
            client._headers = new_headers
        else:
            client._headers = self._headers.copy()

        if request_timeout is not DEFAULT:
            client._request_timeout = request_timeout
        else:
            client._request_timeout = self._request_timeout

        if ignore_status is not DEFAULT:
            if isinstance(ignore_status, int):
                ignore_status = (ignore_status,)
            client._ignore_status = ignore_status
        else:
            client._ignore_status = self._ignore_status

        if max_retries is not DEFAULT:
            if not isinstance(max_retries, int):
                raise TypeError("'max_retries' must be of type 'int'")
            client._max_retries = max_retries
        else:
            client._max_retries = self._max_retries

        if retry_on_status is not DEFAULT:
            if isinstance(retry_on_status, int):
                retry_on_status = (retry_on_status,)
            client._retry_on_status = retry_on_status
        else:
            client._retry_on_status = self._retry_on_status

        if retry_on_timeout is not DEFAULT:
            if not isinstance(retry_on_timeout, bool):
                raise TypeError("'retry_on_timeout' must be of type 'bool'")
            client._retry_on_timeout = retry_on_timeout
        else:
            client._retry_on_timeout = self._retry_on_timeout

        return client

    def close(self) -> None:
        """Closes the Transport and all internal connections"""
        self.transport.close()

    @_rewrite_parameters()
    def ping(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[t.List[str], str]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> bool:
        """
        Returns True if a successful response returns from the info() API,
        otherwise returns False. This API call can fail either at the transport
        layer (due to connection errors or timeouts) or from a non-2XX HTTP response
        (due to authentication or authorization issues).

        If you want to discover why the request failed you should use the ``info()`` API.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`_
        """
        __path = "/"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        try:
            self.perform_request("HEAD", __path, params=__query, headers=__headers)
            return True
        except (ApiError, TransportError):
            return False

    # AUTO-GENERATED-API-DEFINITIONS #

    @_rewrite_parameters(
        body_name="operations",
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def bulk(
        self,
        *,
        operations: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        index: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pipeline: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union["t.Literal['false', 'true', 'wait_for']", bool, str]
        ] = None,
        require_alias: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Union[str, t.Sequence[str]]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to perform multiple index/update/delete operations in a single request.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-bulk.html>`_

        :param operations:
        :param index: Name of the data stream, index, or index alias to perform bulk
            actions on.
        :param pipeline: ID of the pipeline to use to preprocess incoming documents.
            If the index has a default ingest pipeline specified, then setting the value
            to `_none` disables the default ingest pipeline for this request. If a final
            pipeline is configured it will always run, regardless of the value of this
            parameter.
        :param refresh: If `true`, Elasticsearch refreshes the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` do nothing with refreshes.
            Valid values: `true`, `false`, `wait_for`.
        :param require_alias: If `true`, the request’s actions must target an index alias.
        :param routing: Custom value used to route operations to a specific shard.
        :param source: `true` or `false` to return the `_source` field or not, or a list
            of fields to return.
        :param source_excludes: A comma-separated list of source fields to exclude from
            the response.
        :param source_includes: A comma-separated list of source fields to include in
            the response.
        :param timeout: Period each action waits for the following operations: automatic
            index creation, dynamic mapping updates, waiting for active shards.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to all or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        """
        if operations is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'operations' and 'body', one of them should be set."
            )
        elif operations is not None and body is not None:
            raise ValueError("Cannot set both 'operations' and 'body'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_bulk'
        else:
            __path_parts = {}
            __path = "/_bulk"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pipeline is not None:
            __query["pipeline"] = pipeline
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if require_alias is not None:
            __query["require_alias"] = require_alias
        if routing is not None:
            __query["routing"] = routing
        if source is not None:
            __query["_source"] = source
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if timeout is not None:
            __query["timeout"] = timeout
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        __body = operations if operations is not None else body
        __headers = {
            "accept": "application/json",
            "content-type": "application/x-ndjson",
        }
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="bulk",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("scroll_id",),
    )
    def clear_scroll(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        scroll_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Explicitly clears the search context for a scroll.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/clear-scroll-api.html>`_

        :param scroll_id: Scroll IDs to clear. To clear all scroll IDs, use `_all`.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_search/scroll"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if scroll_id is not None:
                __body["scroll_id"] = scroll_id
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="clear_scroll",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("id",),
    )
    def close_point_in_time(
        self,
        *,
        id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Close a point in time

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/point-in-time-api.html>`_

        :param id: The ID of the point-in-time.
        """
        if id is None and body is None:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_pit"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if id is not None:
                __body["id"] = id
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="close_point_in_time",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("query",),
    )
    def count(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        analyze_wildcard: t.Optional[bool] = None,
        analyzer: t.Optional[str] = None,
        default_operator: t.Optional[t.Union["t.Literal['and', 'or']", str]] = None,
        df: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        lenient: t.Optional[bool] = None,
        min_score: t.Optional[float] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        q: t.Optional[str] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        routing: t.Optional[str] = None,
        terminate_after: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns number of documents matching a query.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-count.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases to search.
            Supports wildcards (`*`). To search all data streams and indices, omit this
            parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param analyze_wildcard: If `true`, wildcard and prefix queries are analyzed.
            This parameter can only be used when the `q` query string parameter is specified.
        :param analyzer: Analyzer to use for the query string. This parameter can only
            be used when the `q` query string parameter is specified.
        :param default_operator: The default operator for query string query: `AND` or
            `OR`. This parameter can only be used when the `q` query string parameter
            is specified.
        :param df: Field to use as default where no field prefix is given in the query
            string. This parameter can only be used when the `q` query string parameter
            is specified.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`.
        :param ignore_throttled: If `true`, concrete, expanded or aliased indices are
            ignored when frozen.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param lenient: If `true`, format-based query failures (such as providing text
            to a numeric field) in the query string will be ignored.
        :param min_score: Sets the minimum `_score` value that documents must have to
            be included in the result.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param q: Query in the Lucene query string syntax.
        :param query: Defines the search definition using the Query DSL.
        :param routing: Custom value used to route operations to a specific shard.
        :param terminate_after: Maximum number of documents to collect for each shard.
            If a query reaches this limit, Elasticsearch terminates the query early.
            Elasticsearch collects documents before sorting.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_count'
        else:
            __path_parts = {}
            __path = "/_count"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if analyze_wildcard is not None:
            __query["analyze_wildcard"] = analyze_wildcard
        if analyzer is not None:
            __query["analyzer"] = analyzer
        if default_operator is not None:
            __query["default_operator"] = default_operator
        if df is not None:
            __query["df"] = df
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_throttled is not None:
            __query["ignore_throttled"] = ignore_throttled
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if lenient is not None:
            __query["lenient"] = lenient
        if min_score is not None:
            __query["min_score"] = min_score
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if q is not None:
            __query["q"] = q
        if routing is not None:
            __query["routing"] = routing
        if terminate_after is not None:
            __query["terminate_after"] = terminate_after
        if not __body:
            if query is not None:
                __body["query"] = query
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="count",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="document",
    )
    def create(
        self,
        *,
        index: str,
        id: str,
        document: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pipeline: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union["t.Literal['false', 'true', 'wait_for']", bool, str]
        ] = None,
        routing: t.Optional[str] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a new document in the index. Returns a 409 response when a document with
        a same ID already exists in the index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-index_.html>`_

        :param index: Name of the data stream or index to target. If the target doesn’t
            exist and matches the name or wildcard (`*`) pattern of an index template
            with a `data_stream` definition, this request creates the data stream. If
            the target doesn’t exist and doesn’t match a data stream template, this request
            creates the index.
        :param id: Unique identifier for the document.
        :param document:
        :param pipeline: ID of the pipeline to use to preprocess incoming documents.
            If the index has a default ingest pipeline specified, then setting the value
            to `_none` disables the default ingest pipeline for this request. If a final
            pipeline is configured it will always run, regardless of the value of this
            parameter.
        :param refresh: If `true`, Elasticsearch refreshes the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` do nothing with refreshes.
            Valid values: `true`, `false`, `wait_for`.
        :param routing: Custom value used to route operations to a specific shard.
        :param timeout: Period the request waits for the following operations: automatic
            index creation, dynamic mapping updates, waiting for active shards.
        :param version: Explicit version number for concurrency control. The specified
            version must match the current version of the document for the request to
            succeed.
        :param version_type: Specific version type: `external`, `external_gte`.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to `all` or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        if document is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'document' and 'body', one of them should be set."
            )
        elif document is not None and body is not None:
            raise ValueError("Cannot set both 'document' and 'body'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_create/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pipeline is not None:
            __query["pipeline"] = pipeline
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if routing is not None:
            __query["routing"] = routing
        if timeout is not None:
            __query["timeout"] = timeout
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        __body = document if document is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="create",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete(
        self,
        *,
        index: str,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        if_primary_term: t.Optional[int] = None,
        if_seq_no: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union["t.Literal['false', 'true', 'wait_for']", bool, str]
        ] = None,
        routing: t.Optional[str] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Removes a document from the index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-delete.html>`_

        :param index: Name of the target index.
        :param id: Unique identifier for the document.
        :param if_primary_term: Only perform the operation if the document has this primary
            term.
        :param if_seq_no: Only perform the operation if the document has this sequence
            number.
        :param refresh: If `true`, Elasticsearch refreshes the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` do nothing with refreshes.
            Valid values: `true`, `false`, `wait_for`.
        :param routing: Custom value used to route operations to a specific shard.
        :param timeout: Period to wait for active shards.
        :param version: Explicit version number for concurrency control. The specified
            version must match the current version of the document for the request to
            succeed.
        :param version_type: Specific version type: `external`, `external_gte`.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to `all` or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_doc/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if if_primary_term is not None:
            __query["if_primary_term"] = if_primary_term
        if if_seq_no is not None:
            __query["if_seq_no"] = if_seq_no
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if routing is not None:
            __query["routing"] = routing
        if timeout is not None:
            __query["timeout"] = timeout
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("max_docs", "query", "slice"),
        parameter_aliases={"from": "from_"},
    )
    def delete_by_query(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        allow_no_indices: t.Optional[bool] = None,
        analyze_wildcard: t.Optional[bool] = None,
        analyzer: t.Optional[str] = None,
        conflicts: t.Optional[t.Union["t.Literal['abort', 'proceed']", str]] = None,
        default_operator: t.Optional[t.Union["t.Literal['and', 'or']", str]] = None,
        df: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        lenient: t.Optional[bool] = None,
        max_docs: t.Optional[int] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        q: t.Optional[str] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        refresh: t.Optional[bool] = None,
        request_cache: t.Optional[bool] = None,
        requests_per_second: t.Optional[float] = None,
        routing: t.Optional[str] = None,
        scroll: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        scroll_size: t.Optional[int] = None,
        search_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        search_type: t.Optional[
            t.Union["t.Literal['dfs_query_then_fetch', 'query_then_fetch']", str]
        ] = None,
        slice: t.Optional[t.Mapping[str, t.Any]] = None,
        slices: t.Optional[t.Union[int, t.Union["t.Literal['auto']", str]]] = None,
        sort: t.Optional[t.Sequence[str]] = None,
        stats: t.Optional[t.Sequence[str]] = None,
        terminate_after: t.Optional[int] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        version: t.Optional[bool] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
        wait_for_completion: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes documents matching the provided query.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-delete-by-query.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases to search.
            Supports wildcards (`*`). To search all data streams or indices, omit this
            parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param analyze_wildcard: If `true`, wildcard and prefix queries are analyzed.
        :param analyzer: Analyzer to use for the query string.
        :param conflicts: What to do if delete by query hits version conflicts: `abort`
            or `proceed`.
        :param default_operator: The default operator for query string query: `AND` or
            `OR`.
        :param df: Field to use as default where no field prefix is given in the query
            string.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param from_: Starting offset (default: 0)
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param lenient: If `true`, format-based query failures (such as providing text
            to a numeric field) in the query string will be ignored.
        :param max_docs: The maximum number of documents to delete.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param q: Query in the Lucene query string syntax.
        :param query: Specifies the documents to delete using the Query DSL.
        :param refresh: If `true`, Elasticsearch refreshes all shards involved in the
            delete by query after the request completes.
        :param request_cache: If `true`, the request cache is used for this request.
            Defaults to the index-level setting.
        :param requests_per_second: The throttle for this request in sub-requests per
            second.
        :param routing: Custom value used to route operations to a specific shard.
        :param scroll: Period to retain the search context for scrolling.
        :param scroll_size: Size of the scroll request that powers the operation.
        :param search_timeout: Explicit timeout for each search request. Defaults to
            no timeout.
        :param search_type: The type of the search operation. Available options: `query_then_fetch`,
            `dfs_query_then_fetch`.
        :param slice: Slice the request manually using the provided slice ID and total
            number of slices.
        :param slices: The number of slices this task should be divided into.
        :param sort: A comma-separated list of <field>:<direction> pairs.
        :param stats: Specific `tag` of the request for logging and statistical purposes.
        :param terminate_after: Maximum number of documents to collect for each shard.
            If a query reaches this limit, Elasticsearch terminates the query early.
            Elasticsearch collects documents before sorting. Use with caution. Elasticsearch
            applies this parameter to each shard handling the request. When possible,
            let Elasticsearch perform early termination automatically. Avoid specifying
            this parameter for requests that target data streams with backing indices
            across multiple data tiers.
        :param timeout: Period each deletion request waits for active shards.
        :param version: If `true`, returns the document version as part of a hit.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to all or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        :param wait_for_completion: If `true`, the request blocks until the operation
            is complete.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_delete_by_query'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        # The 'sort' parameter with a colon can't be encoded to the body.
        if sort is not None and (
            (isinstance(sort, str) and ":" in sort)
            or (
                isinstance(sort, (list, tuple))
                and all(isinstance(_x, str) for _x in sort)
                and any(":" in _x for _x in sort)
            )
        ):
            __query["sort"] = sort
            sort = None
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if analyze_wildcard is not None:
            __query["analyze_wildcard"] = analyze_wildcard
        if analyzer is not None:
            __query["analyzer"] = analyzer
        if conflicts is not None:
            __query["conflicts"] = conflicts
        if default_operator is not None:
            __query["default_operator"] = default_operator
        if df is not None:
            __query["df"] = df
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if lenient is not None:
            __query["lenient"] = lenient
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if q is not None:
            __query["q"] = q
        if refresh is not None:
            __query["refresh"] = refresh
        if request_cache is not None:
            __query["request_cache"] = request_cache
        if requests_per_second is not None:
            __query["requests_per_second"] = requests_per_second
        if routing is not None:
            __query["routing"] = routing
        if scroll is not None:
            __query["scroll"] = scroll
        if scroll_size is not None:
            __query["scroll_size"] = scroll_size
        if search_timeout is not None:
            __query["search_timeout"] = search_timeout
        if search_type is not None:
            __query["search_type"] = search_type
        if slices is not None:
            __query["slices"] = slices
        if sort is not None:
            __query["sort"] = sort
        if stats is not None:
            __query["stats"] = stats
        if terminate_after is not None:
            __query["terminate_after"] = terminate_after
        if timeout is not None:
            __query["timeout"] = timeout
        if version is not None:
            __query["version"] = version
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        if not __body:
            if max_docs is not None:
                __body["max_docs"] = max_docs
            if query is not None:
                __body["query"] = query
            if slice is not None:
                __body["slice"] = slice
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="delete_by_query",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_by_query_rethrottle(
        self,
        *,
        task_id: t.Union[int, str],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        requests_per_second: t.Optional[float] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Changes the number of requests per second for a particular Delete By Query operation.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-delete-by-query.html>`_

        :param task_id: The ID for the task.
        :param requests_per_second: The throttle for this request in sub-requests per
            second.
        """
        if task_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'task_id'")
        __path_parts: t.Dict[str, str] = {"task_id": _quote(task_id)}
        __path = f'/_delete_by_query/{__path_parts["task_id"]}/_rethrottle'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if requests_per_second is not None:
            __query["requests_per_second"] = requests_per_second
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="delete_by_query_rethrottle",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_script(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a script.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-scripting.html>`_

        :param id: Identifier for the stored script or search template.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_scripts/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="delete_script",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def exists(
        self,
        *,
        index: str,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        realtime: t.Optional[bool] = None,
        refresh: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Union[str, t.Sequence[str]]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        stored_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
    ) -> HeadApiResponse:
        """
        Returns information about whether a document exists in an index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-get.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases. Supports
            wildcards (`*`).
        :param id: Identifier of the document.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param realtime: If `true`, the request is real-time as opposed to near-real-time.
        :param refresh: If `true`, Elasticsearch refreshes all shards involved in the
            delete by query after the request completes.
        :param routing: Target the specified primary shard.
        :param source: `true` or `false` to return the `_source` field or not, or a list
            of fields to return.
        :param source_excludes: A comma-separated list of source fields to exclude in
            the response.
        :param source_includes: A comma-separated list of source fields to include in
            the response.
        :param stored_fields: List of stored fields to return as part of a hit. If no
            fields are specified, no stored fields are included in the response. If this
            field is specified, the `_source` parameter defaults to false.
        :param version: Explicit version number for concurrency control. The specified
            version must match the current version of the document for the request to
            succeed.
        :param version_type: Specific version type: `external`, `external_gte`.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_doc/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if realtime is not None:
            __query["realtime"] = realtime
        if refresh is not None:
            __query["refresh"] = refresh
        if routing is not None:
            __query["routing"] = routing
        if source is not None:
            __query["_source"] = source
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if stored_fields is not None:
            __query["stored_fields"] = stored_fields
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "HEAD",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="exists",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def exists_source(
        self,
        *,
        index: str,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        realtime: t.Optional[bool] = None,
        refresh: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Union[str, t.Sequence[str]]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
    ) -> HeadApiResponse:
        """
        Returns information about whether a document source exists in an index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-get.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases. Supports
            wildcards (`*`).
        :param id: Identifier of the document.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param realtime: If true, the request is real-time as opposed to near-real-time.
        :param refresh: If `true`, Elasticsearch refreshes all shards involved in the
            delete by query after the request completes.
        :param routing: Target the specified primary shard.
        :param source: `true` or `false` to return the `_source` field or not, or a list
            of fields to return.
        :param source_excludes: A comma-separated list of source fields to exclude in
            the response.
        :param source_includes: A comma-separated list of source fields to include in
            the response.
        :param version: Explicit version number for concurrency control. The specified
            version must match the current version of the document for the request to
            succeed.
        :param version_type: Specific version type: `external`, `external_gte`.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_source/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if realtime is not None:
            __query["realtime"] = realtime
        if refresh is not None:
            __query["refresh"] = refresh
        if routing is not None:
            __query["routing"] = routing
        if source is not None:
            __query["_source"] = source
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "HEAD",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="exists_source",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("query",),
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def explain(
        self,
        *,
        index: str,
        id: str,
        analyze_wildcard: t.Optional[bool] = None,
        analyzer: t.Optional[str] = None,
        default_operator: t.Optional[t.Union["t.Literal['and', 'or']", str]] = None,
        df: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        lenient: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        q: t.Optional[str] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Union[str, t.Sequence[str]]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        stored_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information about why a specific matches (or doesn't match) a query.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-explain.html>`_

        :param index: Index names used to limit the request. Only a single index name
            can be provided to this parameter.
        :param id: Defines the document ID.
        :param analyze_wildcard: If `true`, wildcard and prefix queries are analyzed.
        :param analyzer: Analyzer to use for the query string. This parameter can only
            be used when the `q` query string parameter is specified.
        :param default_operator: The default operator for query string query: `AND` or
            `OR`.
        :param df: Field to use as default where no field prefix is given in the query
            string.
        :param lenient: If `true`, format-based query failures (such as providing text
            to a numeric field) in the query string will be ignored.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param q: Query in the Lucene query string syntax.
        :param query: Defines the search definition using the Query DSL.
        :param routing: Custom value used to route operations to a specific shard.
        :param source: True or false to return the `_source` field or not, or a list
            of fields to return.
        :param source_excludes: A comma-separated list of source fields to exclude from
            the response.
        :param source_includes: A comma-separated list of source fields to include in
            the response.
        :param stored_fields: A comma-separated list of stored fields to return in the
            response.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_explain/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if analyze_wildcard is not None:
            __query["analyze_wildcard"] = analyze_wildcard
        if analyzer is not None:
            __query["analyzer"] = analyzer
        if default_operator is not None:
            __query["default_operator"] = default_operator
        if df is not None:
            __query["df"] = df
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if lenient is not None:
            __query["lenient"] = lenient
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if q is not None:
            __query["q"] = q
        if routing is not None:
            __query["routing"] = routing
        if source is not None:
            __query["_source"] = source
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if stored_fields is not None:
            __query["stored_fields"] = stored_fields
        if not __body:
            if query is not None:
                __body["query"] = query
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="explain",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("fields", "index_filter", "runtime_mappings"),
    )
    def field_caps(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filters: t.Optional[str] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        include_empty_fields: t.Optional[bool] = None,
        include_unmapped: t.Optional[bool] = None,
        index_filter: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        runtime_mappings: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        types: t.Optional[t.Sequence[str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the information about the capabilities of fields among multiple indices.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-field-caps.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases used
            to limit the request. Supports wildcards (*). To target all data streams
            and indices, omit this parameter or use * or _all.
        :param allow_no_indices: If false, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with foo but no index starts with bar.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`.
        :param fields: List of fields to retrieve capabilities for. Wildcard (`*`) expressions
            are supported.
        :param filters: An optional set of filters: can include +metadata,-metadata,-nested,-multifield,-parent
        :param ignore_unavailable: If `true`, missing or closed indices are not included
            in the response.
        :param include_empty_fields: If false, empty fields are not included in the response.
        :param include_unmapped: If true, unmapped fields are included in the response.
        :param index_filter: Allows to filter indices if the provided query rewrites
            to match_none on every shard.
        :param runtime_mappings: Defines ad-hoc runtime fields in the request similar
            to the way it is done in search requests. These fields exist only as part
            of the query and take precedence over fields defined with the same name in
            the index mappings.
        :param types: Only return results for fields that have one of the types in the
            list
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_field_caps'
        else:
            __path_parts = {}
            __path = "/_field_caps"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if filters is not None:
            __query["filters"] = filters
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if include_empty_fields is not None:
            __query["include_empty_fields"] = include_empty_fields
        if include_unmapped is not None:
            __query["include_unmapped"] = include_unmapped
        if pretty is not None:
            __query["pretty"] = pretty
        if types is not None:
            __query["types"] = types
        if not __body:
            if fields is not None:
                __body["fields"] = fields
            if index_filter is not None:
                __body["index_filter"] = index_filter
            if runtime_mappings is not None:
                __body["runtime_mappings"] = runtime_mappings
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="field_caps",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def get(
        self,
        *,
        index: str,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force_synthetic_source: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        realtime: t.Optional[bool] = None,
        refresh: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Union[str, t.Sequence[str]]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        stored_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns a document.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-get.html>`_

        :param index: Name of the index that contains the document.
        :param id: Unique identifier of the document.
        :param force_synthetic_source: Should this request force synthetic _source? Use
            this to test if the mapping supports synthetic _source and to get a sense
            of the worst case performance. Fetches with this enabled will be slower the
            enabling synthetic source natively in the index.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param realtime: If `true`, the request is real-time as opposed to near-real-time.
        :param refresh: If true, Elasticsearch refreshes the affected shards to make
            this operation visible to search. If false, do nothing with refreshes.
        :param routing: Target the specified primary shard.
        :param source: True or false to return the _source field or not, or a list of
            fields to return.
        :param source_excludes: A comma-separated list of source fields to exclude in
            the response.
        :param source_includes: A comma-separated list of source fields to include in
            the response.
        :param stored_fields: List of stored fields to return as part of a hit. If no
            fields are specified, no stored fields are included in the response. If this
            field is specified, the `_source` parameter defaults to false.
        :param version: Explicit version number for concurrency control. The specified
            version must match the current version of the document for the request to
            succeed.
        :param version_type: Specific version type: internal, external, external_gte.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_doc/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force_synthetic_source is not None:
            __query["force_synthetic_source"] = force_synthetic_source
        if human is not None:
            __query["human"] = human
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if realtime is not None:
            __query["realtime"] = realtime
        if refresh is not None:
            __query["refresh"] = refresh
        if routing is not None:
            __query["routing"] = routing
        if source is not None:
            __query["_source"] = source
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if stored_fields is not None:
            __query["stored_fields"] = stored_fields
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_script(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns a script.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-scripting.html>`_

        :param id: Identifier for the stored script or search template.
        :param master_timeout: Specify timeout for connection to master
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_scripts/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="get_script",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_script_context(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns all script contexts.

        `<https://www.elastic.co/guide/en/elasticsearch/painless/8.14/painless-contexts.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_script_context"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="get_script_context",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_script_languages(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns available script types, languages and contexts

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-scripting.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_script_language"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="get_script_languages",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def get_source(
        self,
        *,
        index: str,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        realtime: t.Optional[bool] = None,
        refresh: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Union[str, t.Sequence[str]]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        stored_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the source of a document.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-get.html>`_

        :param index: Name of the index that contains the document.
        :param id: Unique identifier of the document.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param realtime: Boolean) If true, the request is real-time as opposed to near-real-time.
        :param refresh: If true, Elasticsearch refreshes the affected shards to make
            this operation visible to search. If false, do nothing with refreshes.
        :param routing: Target the specified primary shard.
        :param source: True or false to return the _source field or not, or a list of
            fields to return.
        :param source_excludes: A comma-separated list of source fields to exclude in
            the response.
        :param source_includes: A comma-separated list of source fields to include in
            the response.
        :param stored_fields:
        :param version: Explicit version number for concurrency control. The specified
            version must match the current version of the document for the request to
            succeed.
        :param version_type: Specific version type: internal, external, external_gte.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_source/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if realtime is not None:
            __query["realtime"] = realtime
        if refresh is not None:
            __query["refresh"] = refresh
        if routing is not None:
            __query["routing"] = routing
        if source is not None:
            __query["_source"] = source
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if stored_fields is not None:
            __query["stored_fields"] = stored_fields
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="get_source",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def health_report(
        self,
        *,
        feature: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        verbose: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the health of the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/health-api.html>`_

        :param feature: A feature of the cluster, as returned by the top-level health
            report API.
        :param size: Limit the number of affected resources the health report API returns.
        :param timeout: Explicit operation timeout.
        :param verbose: Opt-in for more information about the health of the system.
        """
        __path_parts: t.Dict[str, str]
        if feature not in SKIP_IN_PATH:
            __path_parts = {"feature": _quote(feature)}
            __path = f'/_health_report/{__path_parts["feature"]}'
        else:
            __path_parts = {}
            __path = "/_health_report"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if timeout is not None:
            __query["timeout"] = timeout
        if verbose is not None:
            __query["verbose"] = verbose
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="health_report",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="document",
    )
    def index(
        self,
        *,
        index: str,
        document: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        if_primary_term: t.Optional[int] = None,
        if_seq_no: t.Optional[int] = None,
        op_type: t.Optional[t.Union["t.Literal['create', 'index']", str]] = None,
        pipeline: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union["t.Literal['false', 'true', 'wait_for']", bool, str]
        ] = None,
        require_alias: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a document in an index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-index_.html>`_

        :param index: Name of the data stream or index to target.
        :param document:
        :param id: Unique identifier for the document.
        :param if_primary_term: Only perform the operation if the document has this primary
            term.
        :param if_seq_no: Only perform the operation if the document has this sequence
            number.
        :param op_type: Set to create to only index the document if it does not already
            exist (put if absent). If a document with the specified `_id` already exists,
            the indexing operation will fail. Same as using the `<index>/_create` endpoint.
            Valid values: `index`, `create`. If document id is specified, it defaults
            to `index`. Otherwise, it defaults to `create`.
        :param pipeline: ID of the pipeline to use to preprocess incoming documents.
            If the index has a default ingest pipeline specified, then setting the value
            to `_none` disables the default ingest pipeline for this request. If a final
            pipeline is configured it will always run, regardless of the value of this
            parameter.
        :param refresh: If `true`, Elasticsearch refreshes the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` do nothing with refreshes.
            Valid values: `true`, `false`, `wait_for`.
        :param require_alias: If `true`, the destination must be an index alias.
        :param routing: Custom value used to route operations to a specific shard.
        :param timeout: Period the request waits for the following operations: automatic
            index creation, dynamic mapping updates, waiting for active shards.
        :param version: Explicit version number for concurrency control. The specified
            version must match the current version of the document for the request to
            succeed.
        :param version_type: Specific version type: `external`, `external_gte`.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to all or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if document is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'document' and 'body', one of them should be set."
            )
        elif document is not None and body is not None:
            raise ValueError("Cannot set both 'document' and 'body'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH and id not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index), "id": _quote(id)}
            __path = f'/{__path_parts["index"]}/_doc/{__path_parts["id"]}'
            __method = "PUT"
        elif index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_doc'
            __method = "POST"
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if if_primary_term is not None:
            __query["if_primary_term"] = if_primary_term
        if if_seq_no is not None:
            __query["if_seq_no"] = if_seq_no
        if op_type is not None:
            __query["op_type"] = op_type
        if pipeline is not None:
            __query["pipeline"] = pipeline
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if require_alias is not None:
            __query["require_alias"] = require_alias
        if routing is not None:
            __query["routing"] = routing
        if timeout is not None:
            __query["timeout"] = timeout
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        __body = document if document is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            __method,
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="index",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def info(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns basic information about the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/index.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="info",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "knn",
            "docvalue_fields",
            "fields",
            "filter",
            "source",
            "stored_fields",
        ),
        parameter_aliases={"_source": "source"},
    )
    def knn_search(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        knn: t.Optional[t.Mapping[str, t.Any]] = None,
        docvalue_fields: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filter: t.Optional[
            t.Union[t.Mapping[str, t.Any], t.Sequence[t.Mapping[str, t.Any]]]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Mapping[str, t.Any]]] = None,
        stored_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Performs a kNN search.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-search.html>`_

        :param index: A comma-separated list of index names to search; use `_all` or
            to perform the operation on all indices
        :param knn: kNN query to execute
        :param docvalue_fields: The request returns doc values for field names matching
            these patterns in the hits.fields property of the response. Accepts wildcard
            (*) patterns.
        :param fields: The request returns values for field names matching these patterns
            in the hits.fields property of the response. Accepts wildcard (*) patterns.
        :param filter: Query to filter the documents that can match. The kNN search will
            return the top `k` documents that also match this filter. The value can be
            a single query or a list of queries. If `filter` isn't provided, all documents
            are allowed to match.
        :param routing: A comma-separated list of specific routing values
        :param source: Indicates which source fields are returned for matching documents.
            These fields are returned in the hits._source property of the search response.
        :param stored_fields: List of stored fields to return as part of a hit. If no
            fields are specified, no stored fields are included in the response. If this
            field is specified, the _source parameter defaults to false. You can pass
            _source: true to return both source fields and stored fields in the search
            response.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if knn is None and body is None:
            raise ValueError("Empty value passed for parameter 'knn'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_knn_search'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if routing is not None:
            __query["routing"] = routing
        if not __body:
            if knn is not None:
                __body["knn"] = knn
            if docvalue_fields is not None:
                __body["docvalue_fields"] = docvalue_fields
            if fields is not None:
                __body["fields"] = fields
            if filter is not None:
                __body["filter"] = filter
            if source is not None:
                __body["_source"] = source
            if stored_fields is not None:
                __body["stored_fields"] = stored_fields
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="knn_search",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("docs", "ids"),
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def mget(
        self,
        *,
        index: t.Optional[str] = None,
        docs: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force_synthetic_source: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        ids: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        realtime: t.Optional[bool] = None,
        refresh: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        source: t.Optional[t.Union[bool, t.Union[str, t.Sequence[str]]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        stored_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to get multiple documents in one request.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-multi-get.html>`_

        :param index: Name of the index to retrieve documents from when `ids` are specified,
            or when a document in the `docs` array does not specify an index.
        :param docs: The documents you want to retrieve. Required if no index is specified
            in the request URI.
        :param force_synthetic_source: Should this request force synthetic _source? Use
            this to test if the mapping supports synthetic _source and to get a sense
            of the worst case performance. Fetches with this enabled will be slower the
            enabling synthetic source natively in the index.
        :param ids: The IDs of the documents you want to retrieve. Allowed when the index
            is specified in the request URI.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param realtime: If `true`, the request is real-time as opposed to near-real-time.
        :param refresh: If `true`, the request refreshes relevant shards before retrieving
            documents.
        :param routing: Custom value used to route operations to a specific shard.
        :param source: True or false to return the `_source` field or not, or a list
            of fields to return.
        :param source_excludes: A comma-separated list of source fields to exclude from
            the response. You can also use this parameter to exclude fields from the
            subset specified in `_source_includes` query parameter.
        :param source_includes: A comma-separated list of source fields to include in
            the response. If this parameter is specified, only these source fields are
            returned. You can exclude fields from this subset using the `_source_excludes`
            query parameter. If the `_source` parameter is `false`, this parameter is
            ignored.
        :param stored_fields: If `true`, retrieves the document fields stored in the
            index rather than the document `_source`.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_mget'
        else:
            __path_parts = {}
            __path = "/_mget"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force_synthetic_source is not None:
            __query["force_synthetic_source"] = force_synthetic_source
        if human is not None:
            __query["human"] = human
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if realtime is not None:
            __query["realtime"] = realtime
        if refresh is not None:
            __query["refresh"] = refresh
        if routing is not None:
            __query["routing"] = routing
        if source is not None:
            __query["_source"] = source
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if stored_fields is not None:
            __query["stored_fields"] = stored_fields
        if not __body:
            if docs is not None:
                __body["docs"] = docs
            if ids is not None:
                __body["ids"] = ids
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="mget",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="searches",
    )
    def msearch(
        self,
        *,
        searches: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        ccs_minimize_roundtrips: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        max_concurrent_searches: t.Optional[int] = None,
        max_concurrent_shard_requests: t.Optional[int] = None,
        pre_filter_shard_size: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        rest_total_hits_as_int: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        search_type: t.Optional[
            t.Union["t.Literal['dfs_query_then_fetch', 'query_then_fetch']", str]
        ] = None,
        typed_keys: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to execute several search operations in one request.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-multi-search.html>`_

        :param searches:
        :param index: Comma-separated list of data streams, indices, and index aliases
            to search.
        :param allow_no_indices: If false, the request returns an error if any wildcard
            expression, index alias, or _all value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting foo*,bar* returns an error if an index starts
            with foo but no index starts with bar.
        :param ccs_minimize_roundtrips: If true, network roundtrips between the coordinating
            node and remote clusters are minimized for cross-cluster search requests.
        :param expand_wildcards: Type of index that wildcard expressions can match. If
            the request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams.
        :param ignore_throttled: If true, concrete, expanded or aliased indices are ignored
            when frozen.
        :param ignore_unavailable: If true, missing or closed indices are not included
            in the response.
        :param max_concurrent_searches: Maximum number of concurrent searches the multi
            search API can execute.
        :param max_concurrent_shard_requests: Maximum number of concurrent shard requests
            that each sub-search request executes per node.
        :param pre_filter_shard_size: Defines a threshold that enforces a pre-filter
            roundtrip to prefilter search shards based on query rewriting if the number
            of shards the search request expands to exceeds the threshold. This filter
            roundtrip can limit the number of shards significantly if for instance a
            shard can not match any documents based on its rewrite method i.e., if date
            filters are mandatory to match but the shard bounds and the query are disjoint.
        :param rest_total_hits_as_int: If true, hits.total are returned as an integer
            in the response. Defaults to false, which returns an object.
        :param routing: Custom routing value used to route search operations to a specific
            shard.
        :param search_type: Indicates whether global term and document frequencies should
            be used when scoring returned documents.
        :param typed_keys: Specifies whether aggregation and suggester names should be
            prefixed by their respective types in the response.
        """
        if searches is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'searches' and 'body', one of them should be set."
            )
        elif searches is not None and body is not None:
            raise ValueError("Cannot set both 'searches' and 'body'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_msearch'
        else:
            __path_parts = {}
            __path = "/_msearch"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if ccs_minimize_roundtrips is not None:
            __query["ccs_minimize_roundtrips"] = ccs_minimize_roundtrips
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_throttled is not None:
            __query["ignore_throttled"] = ignore_throttled
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if max_concurrent_searches is not None:
            __query["max_concurrent_searches"] = max_concurrent_searches
        if max_concurrent_shard_requests is not None:
            __query["max_concurrent_shard_requests"] = max_concurrent_shard_requests
        if pre_filter_shard_size is not None:
            __query["pre_filter_shard_size"] = pre_filter_shard_size
        if pretty is not None:
            __query["pretty"] = pretty
        if rest_total_hits_as_int is not None:
            __query["rest_total_hits_as_int"] = rest_total_hits_as_int
        if routing is not None:
            __query["routing"] = routing
        if search_type is not None:
            __query["search_type"] = search_type
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        __body = searches if searches is not None else body
        __headers = {
            "accept": "application/json",
            "content-type": "application/x-ndjson",
        }
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="msearch",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="search_templates",
    )
    def msearch_template(
        self,
        *,
        search_templates: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        ccs_minimize_roundtrips: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        max_concurrent_searches: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        rest_total_hits_as_int: t.Optional[bool] = None,
        search_type: t.Optional[
            t.Union["t.Literal['dfs_query_then_fetch', 'query_then_fetch']", str]
        ] = None,
        typed_keys: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to execute several search template operations in one request.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-multi-search.html>`_

        :param search_templates:
        :param index: Comma-separated list of data streams, indices, and aliases to search.
            Supports wildcards (`*`). To search all data streams and indices, omit this
            parameter or use `*`.
        :param ccs_minimize_roundtrips: If `true`, network round-trips are minimized
            for cross-cluster search requests.
        :param max_concurrent_searches: Maximum number of concurrent searches the API
            can run.
        :param rest_total_hits_as_int: If `true`, the response returns `hits.total` as
            an integer. If `false`, it returns `hits.total` as an object.
        :param search_type: The type of the search operation. Available options: `query_then_fetch`,
            `dfs_query_then_fetch`.
        :param typed_keys: If `true`, the response prefixes aggregation and suggester
            names with their respective types.
        """
        if search_templates is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'search_templates' and 'body', one of them should be set."
            )
        elif search_templates is not None and body is not None:
            raise ValueError("Cannot set both 'search_templates' and 'body'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_msearch/template'
        else:
            __path_parts = {}
            __path = "/_msearch/template"
        __query: t.Dict[str, t.Any] = {}
        if ccs_minimize_roundtrips is not None:
            __query["ccs_minimize_roundtrips"] = ccs_minimize_roundtrips
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if max_concurrent_searches is not None:
            __query["max_concurrent_searches"] = max_concurrent_searches
        if pretty is not None:
            __query["pretty"] = pretty
        if rest_total_hits_as_int is not None:
            __query["rest_total_hits_as_int"] = rest_total_hits_as_int
        if search_type is not None:
            __query["search_type"] = search_type
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        __body = search_templates if search_templates is not None else body
        __headers = {
            "accept": "application/json",
            "content-type": "application/x-ndjson",
        }
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="msearch_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("docs", "ids"),
    )
    def mtermvectors(
        self,
        *,
        index: t.Optional[str] = None,
        docs: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        field_statistics: t.Optional[bool] = None,
        fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ids: t.Optional[t.Sequence[str]] = None,
        offsets: t.Optional[bool] = None,
        payloads: t.Optional[bool] = None,
        positions: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        realtime: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        term_statistics: t.Optional[bool] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns multiple termvectors in one request.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-multi-termvectors.html>`_

        :param index: Name of the index that contains the documents.
        :param docs: Array of existing or artificial documents.
        :param field_statistics: If `true`, the response includes the document count,
            sum of document frequencies, and sum of total term frequencies.
        :param fields: Comma-separated list or wildcard expressions of fields to include
            in the statistics. Used as the default list unless a specific field list
            is provided in the `completion_fields` or `fielddata_fields` parameters.
        :param ids: Simplified syntax to specify documents by their ID if they're in
            the same index.
        :param offsets: If `true`, the response includes term offsets.
        :param payloads: If `true`, the response includes term payloads.
        :param positions: If `true`, the response includes term positions.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param realtime: If true, the request is real-time as opposed to near-real-time.
        :param routing: Custom value used to route operations to a specific shard.
        :param term_statistics: If true, the response includes term frequency and document
            frequency.
        :param version: If `true`, returns the document version as part of a hit.
        :param version_type: Specific version type.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_mtermvectors'
        else:
            __path_parts = {}
            __path = "/_mtermvectors"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if field_statistics is not None:
            __query["field_statistics"] = field_statistics
        if fields is not None:
            __query["fields"] = fields
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if offsets is not None:
            __query["offsets"] = offsets
        if payloads is not None:
            __query["payloads"] = payloads
        if positions is not None:
            __query["positions"] = positions
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if realtime is not None:
            __query["realtime"] = realtime
        if routing is not None:
            __query["routing"] = routing
        if term_statistics is not None:
            __query["term_statistics"] = term_statistics
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        if not __body:
            if docs is not None:
                __body["docs"] = docs
            if ids is not None:
                __body["ids"] = ids
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="mtermvectors",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def open_point_in_time(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        keep_alive: t.Union["t.Literal[-1]", "t.Literal[0]", str],
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Open a point in time that can be used in subsequent searches

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/point-in-time-api.html>`_

        :param index: A comma-separated list of index names to open point in time; use
            `_all` or empty string to perform the operation on all indices
        :param keep_alive: Extends the time to live of the corresponding point in time.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param routing: Custom value used to route operations to a specific shard.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if keep_alive is None:
            raise ValueError("Empty value passed for parameter 'keep_alive'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_pit'
        __query: t.Dict[str, t.Any] = {}
        if keep_alive is not None:
            __query["keep_alive"] = keep_alive
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if routing is not None:
            __query["routing"] = routing
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="open_point_in_time",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("script",),
    )
    def put_script(
        self,
        *,
        id: str,
        script: t.Optional[t.Mapping[str, t.Any]] = None,
        context: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a script.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-scripting.html>`_

        :param id: Identifier for the stored script or search template. Must be unique
            within the cluster.
        :param script: Contains the script or search template, its parameters, and its
            language.
        :param context: Context in which the script or search template should run. To
            prevent errors, the API immediately compiles the script or template in this
            context.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        if script is None and body is None:
            raise ValueError("Empty value passed for parameter 'script'")
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH and context not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id), "context": _quote(context)}
            __path = f'/_scripts/{__path_parts["id"]}/{__path_parts["context"]}'
        elif id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_scripts/{__path_parts["id"]}'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if script is not None:
                __body["script"] = script
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="put_script",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("requests", "metric"),
    )
    def rank_eval(
        self,
        *,
        requests: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        metric: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        search_type: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to evaluate the quality of ranked search results over a set of typical
        search queries

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-rank-eval.html>`_

        :param requests: A set of typical search requests, together with their provided
            ratings.
        :param index: Comma-separated list of data streams, indices, and index aliases
            used to limit the request. Wildcard (`*`) expressions are supported. To target
            all data streams and indices in a cluster, omit this parameter or use `_all`
            or `*`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :param ignore_unavailable: If `true`, missing or closed indices are not included
            in the response.
        :param metric: Definition of the evaluation metric to calculate.
        :param search_type: Search operation type
        """
        if requests is None and body is None:
            raise ValueError("Empty value passed for parameter 'requests'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_rank_eval'
        else:
            __path_parts = {}
            __path = "/_rank_eval"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if pretty is not None:
            __query["pretty"] = pretty
        if search_type is not None:
            __query["search_type"] = search_type
        if not __body:
            if requests is not None:
                __body["requests"] = requests
            if metric is not None:
                __body["metric"] = metric
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="rank_eval",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("dest", "source", "conflicts", "max_docs", "script", "size"),
    )
    def reindex(
        self,
        *,
        dest: t.Optional[t.Mapping[str, t.Any]] = None,
        source: t.Optional[t.Mapping[str, t.Any]] = None,
        conflicts: t.Optional[t.Union["t.Literal['abort', 'proceed']", str]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        max_docs: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[bool] = None,
        requests_per_second: t.Optional[float] = None,
        require_alias: t.Optional[bool] = None,
        script: t.Optional[t.Mapping[str, t.Any]] = None,
        scroll: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        size: t.Optional[int] = None,
        slices: t.Optional[t.Union[int, t.Union["t.Literal['auto']", str]]] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
        wait_for_completion: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to copy documents from one index to another, optionally filtering the
        source documents by a query, changing the destination index settings, or fetching
        the documents from a remote cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-reindex.html>`_

        :param dest: The destination you are copying to.
        :param source: The source you are copying from.
        :param conflicts: Set to proceed to continue reindexing even if there are conflicts.
        :param max_docs: The maximum number of documents to reindex.
        :param refresh: If `true`, the request refreshes affected shards to make this
            operation visible to search.
        :param requests_per_second: The throttle for this request in sub-requests per
            second. Defaults to no throttle.
        :param require_alias: If `true`, the destination must be an index alias.
        :param script: The script to run to update the document source or metadata when
            reindexing.
        :param scroll: Specifies how long a consistent view of the index should be maintained
            for scrolled search.
        :param size:
        :param slices: The number of slices this task should be divided into. Defaults
            to 1 slice, meaning the task isn’t sliced into subtasks.
        :param timeout: Period each indexing waits for automatic index creation, dynamic
            mapping updates, and waiting for active shards.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to `all` or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        :param wait_for_completion: If `true`, the request blocks until the operation
            is complete.
        """
        if dest is None and body is None:
            raise ValueError("Empty value passed for parameter 'dest'")
        if source is None and body is None:
            raise ValueError("Empty value passed for parameter 'source'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_reindex"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if requests_per_second is not None:
            __query["requests_per_second"] = requests_per_second
        if require_alias is not None:
            __query["require_alias"] = require_alias
        if scroll is not None:
            __query["scroll"] = scroll
        if slices is not None:
            __query["slices"] = slices
        if timeout is not None:
            __query["timeout"] = timeout
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        if not __body:
            if dest is not None:
                __body["dest"] = dest
            if source is not None:
                __body["source"] = source
            if conflicts is not None:
                __body["conflicts"] = conflicts
            if max_docs is not None:
                __body["max_docs"] = max_docs
            if script is not None:
                __body["script"] = script
            if size is not None:
                __body["size"] = size
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="reindex",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def reindex_rethrottle(
        self,
        *,
        task_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        requests_per_second: t.Optional[float] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Changes the number of requests per second for a particular Reindex operation.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-reindex.html>`_

        :param task_id: Identifier for the task.
        :param requests_per_second: The throttle for this request in sub-requests per
            second.
        """
        if task_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'task_id'")
        __path_parts: t.Dict[str, str] = {"task_id": _quote(task_id)}
        __path = f'/_reindex/{__path_parts["task_id"]}/_rethrottle'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if requests_per_second is not None:
            __query["requests_per_second"] = requests_per_second
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="reindex_rethrottle",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("file", "params", "source"),
        ignore_deprecated_options={"params"},
    )
    def render_search_template(
        self,
        *,
        id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        file: t.Optional[str] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        params: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        source: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to use the Mustache language to pre-render a search definition.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/render-search-template-api.html>`_

        :param id: ID of the search template to render. If no `source` is specified,
            this or the `id` request body parameter is required.
        :param file:
        :param params: Key-value pairs used to replace Mustache variables in the template.
            The key is the variable name. The value is the variable value.
        :param source: An inline search template. Supports the same parameters as the
            search API's request body. These parameters also support Mustache variables.
            If no `id` or `<templated-id>` is specified, this parameter is required.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_render/template/{__path_parts["id"]}'
        else:
            __path_parts = {}
            __path = "/_render/template"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if file is not None:
                __body["file"] = file
            if params is not None:
                __body["params"] = params
            if source is not None:
                __body["source"] = source
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="render_search_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("context", "context_setup", "script"),
    )
    def scripts_painless_execute(
        self,
        *,
        context: t.Optional[str] = None,
        context_setup: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        script: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows an arbitrary script to be executed and a result to be returned

        `<https://www.elastic.co/guide/en/elasticsearch/painless/8.14/painless-execute-api.html>`_

        :param context: The context that the script should run in.
        :param context_setup: Additional parameters for the `context`.
        :param script: The Painless script to execute.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_scripts/painless/_execute"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if context is not None:
                __body["context"] = context
            if context_setup is not None:
                __body["context_setup"] = context_setup
            if script is not None:
                __body["script"] = script
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="scripts_painless_execute",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("scroll_id", "scroll"),
    )
    def scroll(
        self,
        *,
        scroll_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        rest_total_hits_as_int: t.Optional[bool] = None,
        scroll: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to retrieve a large numbers of results from a single search request.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-request-body.html#request-body-search-scroll>`_

        :param scroll_id: Scroll ID of the search.
        :param rest_total_hits_as_int: If true, the API response’s hit.total property
            is returned as an integer. If false, the API response’s hit.total property
            is returned as an object.
        :param scroll: Period to retain the search context for scrolling.
        """
        if scroll_id is None and body is None:
            raise ValueError("Empty value passed for parameter 'scroll_id'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_search/scroll"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if rest_total_hits_as_int is not None:
            __query["rest_total_hits_as_int"] = rest_total_hits_as_int
        if not __body:
            if scroll_id is not None:
                __body["scroll_id"] = scroll_id
            if scroll is not None:
                __body["scroll"] = scroll
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="scroll",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "aggregations",
            "aggs",
            "collapse",
            "docvalue_fields",
            "explain",
            "ext",
            "fields",
            "from_",
            "highlight",
            "indices_boost",
            "knn",
            "min_score",
            "pit",
            "post_filter",
            "profile",
            "query",
            "rank",
            "rescore",
            "retriever",
            "runtime_mappings",
            "script_fields",
            "search_after",
            "seq_no_primary_term",
            "size",
            "slice",
            "sort",
            "source",
            "stats",
            "stored_fields",
            "suggest",
            "terminate_after",
            "timeout",
            "track_scores",
            "track_total_hits",
            "version",
        ),
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
            "from": "from_",
        },
    )
    def search(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        aggregations: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        aggs: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        allow_partial_search_results: t.Optional[bool] = None,
        analyze_wildcard: t.Optional[bool] = None,
        analyzer: t.Optional[str] = None,
        batched_reduce_size: t.Optional[int] = None,
        ccs_minimize_roundtrips: t.Optional[bool] = None,
        collapse: t.Optional[t.Mapping[str, t.Any]] = None,
        default_operator: t.Optional[t.Union["t.Literal['and', 'or']", str]] = None,
        df: t.Optional[str] = None,
        docvalue_fields: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        explain: t.Optional[bool] = None,
        ext: t.Optional[t.Mapping[str, t.Any]] = None,
        fields: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force_synthetic_source: t.Optional[bool] = None,
        from_: t.Optional[int] = None,
        highlight: t.Optional[t.Mapping[str, t.Any]] = None,
        human: t.Optional[bool] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        indices_boost: t.Optional[t.Sequence[t.Mapping[str, float]]] = None,
        knn: t.Optional[
            t.Union[t.Mapping[str, t.Any], t.Sequence[t.Mapping[str, t.Any]]]
        ] = None,
        lenient: t.Optional[bool] = None,
        max_concurrent_shard_requests: t.Optional[int] = None,
        min_compatible_shard_node: t.Optional[str] = None,
        min_score: t.Optional[float] = None,
        pit: t.Optional[t.Mapping[str, t.Any]] = None,
        post_filter: t.Optional[t.Mapping[str, t.Any]] = None,
        pre_filter_shard_size: t.Optional[int] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        profile: t.Optional[bool] = None,
        q: t.Optional[str] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        rank: t.Optional[t.Mapping[str, t.Any]] = None,
        request_cache: t.Optional[bool] = None,
        rescore: t.Optional[
            t.Union[t.Mapping[str, t.Any], t.Sequence[t.Mapping[str, t.Any]]]
        ] = None,
        rest_total_hits_as_int: t.Optional[bool] = None,
        retriever: t.Optional[t.Mapping[str, t.Any]] = None,
        routing: t.Optional[str] = None,
        runtime_mappings: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        script_fields: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        scroll: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        search_after: t.Optional[
            t.Sequence[t.Union[None, bool, float, int, str, t.Any]]
        ] = None,
        search_type: t.Optional[
            t.Union["t.Literal['dfs_query_then_fetch', 'query_then_fetch']", str]
        ] = None,
        seq_no_primary_term: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        slice: t.Optional[t.Mapping[str, t.Any]] = None,
        sort: t.Optional[
            t.Union[
                t.Sequence[t.Union[str, t.Mapping[str, t.Any]]],
                t.Union[str, t.Mapping[str, t.Any]],
            ]
        ] = None,
        source: t.Optional[t.Union[bool, t.Mapping[str, t.Any]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        stats: t.Optional[t.Sequence[str]] = None,
        stored_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        suggest: t.Optional[t.Mapping[str, t.Any]] = None,
        suggest_field: t.Optional[str] = None,
        suggest_mode: t.Optional[
            t.Union["t.Literal['always', 'missing', 'popular']", str]
        ] = None,
        suggest_size: t.Optional[int] = None,
        suggest_text: t.Optional[str] = None,
        terminate_after: t.Optional[int] = None,
        timeout: t.Optional[str] = None,
        track_scores: t.Optional[bool] = None,
        track_total_hits: t.Optional[t.Union[bool, int]] = None,
        typed_keys: t.Optional[bool] = None,
        version: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns results matching a query.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-search.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases to search.
            Supports wildcards (`*`). To search all data streams and indices, omit this
            parameter or use `*` or `_all`.
        :param aggregations: Defines the aggregations that are run as part of the search
            request.
        :param aggs: Defines the aggregations that are run as part of the search request.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param allow_partial_search_results: If true, returns partial results if there
            are shard request timeouts or shard failures. If false, returns an error
            with no partial results.
        :param analyze_wildcard: If true, wildcard and prefix queries are analyzed. This
            parameter can only be used when the q query string parameter is specified.
        :param analyzer: Analyzer to use for the query string. This parameter can only
            be used when the q query string parameter is specified.
        :param batched_reduce_size: The number of shard results that should be reduced
            at once on the coordinating node. This value should be used as a protection
            mechanism to reduce the memory overhead per search request if the potential
            number of shards in the request can be large.
        :param ccs_minimize_roundtrips: If true, network round-trips between the coordinating
            node and the remote clusters are minimized when executing cross-cluster search
            (CCS) requests.
        :param collapse: Collapses search results the values of the specified field.
        :param default_operator: The default operator for query string query: AND or
            OR. This parameter can only be used when the `q` query string parameter is
            specified.
        :param df: Field to use as default where no field prefix is given in the query
            string. This parameter can only be used when the q query string parameter
            is specified.
        :param docvalue_fields: Array of wildcard (`*`) patterns. The request returns
            doc values for field names matching these patterns in the `hits.fields` property
            of the response.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`.
        :param explain: If true, returns detailed information about score computation
            as part of a hit.
        :param ext: Configuration of search extensions defined by Elasticsearch plugins.
        :param fields: Array of wildcard (`*`) patterns. The request returns values for
            field names matching these patterns in the `hits.fields` property of the
            response.
        :param force_synthetic_source: Should this request force synthetic _source? Use
            this to test if the mapping supports synthetic _source and to get a sense
            of the worst case performance. Fetches with this enabled will be slower the
            enabling synthetic source natively in the index.
        :param from_: Starting document offset. Needs to be non-negative. By default,
            you cannot page through more than 10,000 hits using the `from` and `size`
            parameters. To page through more hits, use the `search_after` parameter.
        :param highlight: Specifies the highlighter to use for retrieving highlighted
            snippets from one or more fields in your search results.
        :param ignore_throttled: If `true`, concrete, expanded or aliased indices will
            be ignored when frozen.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param indices_boost: Boosts the _score of documents from specified indices.
        :param knn: Defines the approximate kNN search to run.
        :param lenient: If `true`, format-based query failures (such as providing text
            to a numeric field) in the query string will be ignored. This parameter can
            only be used when the `q` query string parameter is specified.
        :param max_concurrent_shard_requests: Defines the number of concurrent shard
            requests per node this search executes concurrently. This value should be
            used to limit the impact of the search on the cluster in order to limit the
            number of concurrent shard requests.
        :param min_compatible_shard_node: The minimum version of the node that can handle
            the request Any handling node with a lower version will fail the request.
        :param min_score: Minimum `_score` for matching documents. Documents with a lower
            `_score` are not included in the search results.
        :param pit: Limits the search to a point in time (PIT). If you provide a PIT,
            you cannot specify an `<index>` in the request path.
        :param post_filter: Use the `post_filter` parameter to filter search results.
            The search hits are filtered after the aggregations are calculated. A post
            filter has no impact on the aggregation results.
        :param pre_filter_shard_size: Defines a threshold that enforces a pre-filter
            roundtrip to prefilter search shards based on query rewriting if the number
            of shards the search request expands to exceeds the threshold. This filter
            roundtrip can limit the number of shards significantly if for instance a
            shard can not match any documents based on its rewrite method (if date filters
            are mandatory to match but the shard bounds and the query are disjoint).
            When unspecified, the pre-filter phase is executed if any of these conditions
            is met: the request targets more than 128 shards; the request targets one
            or more read-only index; the primary sort of the query targets an indexed
            field.
        :param preference: Nodes and shards used for the search. By default, Elasticsearch
            selects from eligible nodes and shards using adaptive replica selection,
            accounting for allocation awareness. Valid values are: `_only_local` to run
            the search only on shards on the local node; `_local` to, if possible, run
            the search on shards on the local node, or if not, select shards using the
            default method; `_only_nodes:<node-id>,<node-id>` to run the search on only
            the specified nodes IDs, where, if suitable shards exist on more than one
            selected node, use shards on those nodes using the default method, or if
            none of the specified nodes are available, select shards from any available
            node using the default method; `_prefer_nodes:<node-id>,<node-id>` to if
            possible, run the search on the specified nodes IDs, or if not, select shards
            using the default method; `_shards:<shard>,<shard>` to run the search only
            on the specified shards; `<custom-string>` (any string that does not start
            with `_`) to route searches with the same `<custom-string>` to the same shards
            in the same order.
        :param profile: Set to `true` to return detailed timing information about the
            execution of individual components in a search request. NOTE: This is a debugging
            tool and adds significant overhead to search execution.
        :param q: Query in the Lucene query string syntax using query parameter search.
            Query parameter searches do not support the full Elasticsearch Query DSL
            but are handy for testing.
        :param query: Defines the search definition using the Query DSL.
        :param rank: Defines the Reciprocal Rank Fusion (RRF) to use.
        :param request_cache: If `true`, the caching of search results is enabled for
            requests where `size` is `0`. Defaults to index level settings.
        :param rescore: Can be used to improve precision by reordering just the top (for
            example 100 - 500) documents returned by the `query` and `post_filter` phases.
        :param rest_total_hits_as_int: Indicates whether `hits.total` should be rendered
            as an integer or an object in the rest search response.
        :param retriever: A retriever is a specification to describe top documents returned
            from a search. A retriever replaces other elements of the search API that
            also return top documents such as query and knn.
        :param routing: Custom value used to route operations to a specific shard.
        :param runtime_mappings: Defines one or more runtime fields in the search request.
            These fields take precedence over mapped fields with the same name.
        :param script_fields: Retrieve a script evaluation (based on different fields)
            for each hit.
        :param scroll: Period to retain the search context for scrolling. See Scroll
            search results. By default, this value cannot exceed `1d` (24 hours). You
            can change this limit using the `search.max_keep_alive` cluster-level setting.
        :param search_after: Used to retrieve the next page of hits using a set of sort
            values from the previous page.
        :param search_type: How distributed term frequencies are calculated for relevance
            scoring.
        :param seq_no_primary_term: If `true`, returns sequence number and primary term
            of the last modification of each hit.
        :param size: The number of hits to return. By default, you cannot page through
            more than 10,000 hits using the `from` and `size` parameters. To page through
            more hits, use the `search_after` parameter.
        :param slice: Can be used to split a scrolled search into multiple slices that
            can be consumed independently.
        :param sort: A comma-separated list of <field>:<direction> pairs.
        :param source: Indicates which source fields are returned for matching documents.
            These fields are returned in the hits._source property of the search response.
        :param source_excludes: A comma-separated list of source fields to exclude from
            the response. You can also use this parameter to exclude fields from the
            subset specified in `_source_includes` query parameter. If the `_source`
            parameter is `false`, this parameter is ignored.
        :param source_includes: A comma-separated list of source fields to include in
            the response. If this parameter is specified, only these source fields are
            returned. You can exclude fields from this subset using the `_source_excludes`
            query parameter. If the `_source` parameter is `false`, this parameter is
            ignored.
        :param stats: Stats groups to associate with the search. Each group maintains
            a statistics aggregation for its associated searches. You can retrieve these
            stats using the indices stats API.
        :param stored_fields: List of stored fields to return as part of a hit. If no
            fields are specified, no stored fields are included in the response. If this
            field is specified, the `_source` parameter defaults to `false`. You can
            pass `_source: true` to return both source fields and stored fields in the
            search response.
        :param suggest: Defines a suggester that provides similar looking terms based
            on a provided text.
        :param suggest_field: Specifies which field to use for suggestions.
        :param suggest_mode: Specifies the suggest mode. This parameter can only be used
            when the `suggest_field` and `suggest_text` query string parameters are specified.
        :param suggest_size: Number of suggestions to return. This parameter can only
            be used when the `suggest_field` and `suggest_text` query string parameters
            are specified.
        :param suggest_text: The source text for which the suggestions should be returned.
            This parameter can only be used when the `suggest_field` and `suggest_text`
            query string parameters are specified.
        :param terminate_after: Maximum number of documents to collect for each shard.
            If a query reaches this limit, Elasticsearch terminates the query early.
            Elasticsearch collects documents before sorting. Use with caution. Elasticsearch
            applies this parameter to each shard handling the request. When possible,
            let Elasticsearch perform early termination automatically. Avoid specifying
            this parameter for requests that target data streams with backing indices
            across multiple data tiers. If set to `0` (default), the query does not terminate
            early.
        :param timeout: Specifies the period of time to wait for a response from each
            shard. If no response is received before the timeout expires, the request
            fails and returns an error. Defaults to no timeout.
        :param track_scores: If true, calculate and return document scores, even if the
            scores are not used for sorting.
        :param track_total_hits: Number of hits matching the query to count accurately.
            If `true`, the exact number of hits is returned at the cost of some performance.
            If `false`, the response does not include the total number of hits matching
            the query.
        :param typed_keys: If `true`, aggregation and suggester names are be prefixed
            by their respective types in the response.
        :param version: If true, returns document version as part of a hit.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_search'
        else:
            __path_parts = {}
            __path = "/_search"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        # The 'sort' parameter with a colon can't be encoded to the body.
        if sort is not None and (
            (isinstance(sort, str) and ":" in sort)
            or (
                isinstance(sort, (list, tuple))
                and all(isinstance(_x, str) for _x in sort)
                and any(":" in _x for _x in sort)
            )
        ):
            __query["sort"] = sort
            sort = None
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if allow_partial_search_results is not None:
            __query["allow_partial_search_results"] = allow_partial_search_results
        if analyze_wildcard is not None:
            __query["analyze_wildcard"] = analyze_wildcard
        if analyzer is not None:
            __query["analyzer"] = analyzer
        if batched_reduce_size is not None:
            __query["batched_reduce_size"] = batched_reduce_size
        if ccs_minimize_roundtrips is not None:
            __query["ccs_minimize_roundtrips"] = ccs_minimize_roundtrips
        if default_operator is not None:
            __query["default_operator"] = default_operator
        if df is not None:
            __query["df"] = df
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force_synthetic_source is not None:
            __query["force_synthetic_source"] = force_synthetic_source
        if human is not None:
            __query["human"] = human
        if ignore_throttled is not None:
            __query["ignore_throttled"] = ignore_throttled
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if lenient is not None:
            __query["lenient"] = lenient
        if max_concurrent_shard_requests is not None:
            __query["max_concurrent_shard_requests"] = max_concurrent_shard_requests
        if min_compatible_shard_node is not None:
            __query["min_compatible_shard_node"] = min_compatible_shard_node
        if pre_filter_shard_size is not None:
            __query["pre_filter_shard_size"] = pre_filter_shard_size
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if q is not None:
            __query["q"] = q
        if request_cache is not None:
            __query["request_cache"] = request_cache
        if rest_total_hits_as_int is not None:
            __query["rest_total_hits_as_int"] = rest_total_hits_as_int
        if routing is not None:
            __query["routing"] = routing
        if scroll is not None:
            __query["scroll"] = scroll
        if search_type is not None:
            __query["search_type"] = search_type
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if suggest_field is not None:
            __query["suggest_field"] = suggest_field
        if suggest_mode is not None:
            __query["suggest_mode"] = suggest_mode
        if suggest_size is not None:
            __query["suggest_size"] = suggest_size
        if suggest_text is not None:
            __query["suggest_text"] = suggest_text
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        if not __body:
            if aggregations is not None:
                __body["aggregations"] = aggregations
            if aggs is not None:
                __body["aggs"] = aggs
            if collapse is not None:
                __body["collapse"] = collapse
            if docvalue_fields is not None:
                __body["docvalue_fields"] = docvalue_fields
            if explain is not None:
                __body["explain"] = explain
            if ext is not None:
                __body["ext"] = ext
            if fields is not None:
                __body["fields"] = fields
            if from_ is not None:
                __body["from"] = from_
            if highlight is not None:
                __body["highlight"] = highlight
            if indices_boost is not None:
                __body["indices_boost"] = indices_boost
            if knn is not None:
                __body["knn"] = knn
            if min_score is not None:
                __body["min_score"] = min_score
            if pit is not None:
                __body["pit"] = pit
            if post_filter is not None:
                __body["post_filter"] = post_filter
            if profile is not None:
                __body["profile"] = profile
            if query is not None:
                __body["query"] = query
            if rank is not None:
                __body["rank"] = rank
            if rescore is not None:
                __body["rescore"] = rescore
            if retriever is not None:
                __body["retriever"] = retriever
            if runtime_mappings is not None:
                __body["runtime_mappings"] = runtime_mappings
            if script_fields is not None:
                __body["script_fields"] = script_fields
            if search_after is not None:
                __body["search_after"] = search_after
            if seq_no_primary_term is not None:
                __body["seq_no_primary_term"] = seq_no_primary_term
            if size is not None:
                __body["size"] = size
            if slice is not None:
                __body["slice"] = slice
            if sort is not None:
                __body["sort"] = sort
            if source is not None:
                __body["_source"] = source
            if stats is not None:
                __body["stats"] = stats
            if stored_fields is not None:
                __body["stored_fields"] = stored_fields
            if suggest is not None:
                __body["suggest"] = suggest
            if terminate_after is not None:
                __body["terminate_after"] = terminate_after
            if timeout is not None:
                __body["timeout"] = timeout
            if track_scores is not None:
                __body["track_scores"] = track_scores
            if track_total_hits is not None:
                __body["track_total_hits"] = track_total_hits
            if version is not None:
                __body["version"] = version
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="search",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "aggs",
            "buffer",
            "exact_bounds",
            "extent",
            "fields",
            "grid_agg",
            "grid_precision",
            "grid_type",
            "query",
            "runtime_mappings",
            "size",
            "sort",
            "track_total_hits",
            "with_labels",
        ),
    )
    def search_mvt(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        field: str,
        zoom: int,
        x: int,
        y: int,
        aggs: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        buffer: t.Optional[int] = None,
        error_trace: t.Optional[bool] = None,
        exact_bounds: t.Optional[bool] = None,
        extent: t.Optional[int] = None,
        fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        grid_agg: t.Optional[t.Union["t.Literal['geohex', 'geotile']", str]] = None,
        grid_precision: t.Optional[int] = None,
        grid_type: t.Optional[
            t.Union["t.Literal['centroid', 'grid', 'point']", str]
        ] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        runtime_mappings: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[
            t.Union[
                t.Sequence[t.Union[str, t.Mapping[str, t.Any]]],
                t.Union[str, t.Mapping[str, t.Any]],
            ]
        ] = None,
        track_total_hits: t.Optional[t.Union[bool, int]] = None,
        with_labels: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> BinaryApiResponse:
        """
        Searches a vector tile for geospatial values. Returns results as a binary Mapbox
        vector tile.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-vector-tile-api.html>`_

        :param index: Comma-separated list of data streams, indices, or aliases to search
        :param field: Field containing geospatial data to return
        :param zoom: Zoom level for the vector tile to search
        :param x: X coordinate for the vector tile to search
        :param y: Y coordinate for the vector tile to search
        :param aggs: Sub-aggregations for the geotile_grid. Supports the following aggregation
            types: - avg - cardinality - max - min - sum
        :param buffer: Size, in pixels, of a clipping buffer outside the tile. This allows
            renderers to avoid outline artifacts from geometries that extend past the
            extent of the tile.
        :param exact_bounds: If false, the meta layer’s feature is the bounding box of
            the tile. If true, the meta layer’s feature is a bounding box resulting from
            a geo_bounds aggregation. The aggregation runs on <field> values that intersect
            the <zoom>/<x>/<y> tile with wrap_longitude set to false. The resulting bounding
            box may be larger than the vector tile.
        :param extent: Size, in pixels, of a side of the tile. Vector tiles are square
            with equal sides.
        :param fields: Fields to return in the `hits` layer. Supports wildcards (`*`).
            This parameter does not support fields with array values. Fields with array
            values may return inconsistent results.
        :param grid_agg: Aggregation used to create a grid for the `field`.
        :param grid_precision: Additional zoom levels available through the aggs layer.
            For example, if <zoom> is 7 and grid_precision is 8, you can zoom in up to
            level 15. Accepts 0-8. If 0, results don’t include the aggs layer.
        :param grid_type: Determines the geometry type for features in the aggs layer.
            In the aggs layer, each feature represents a geotile_grid cell. If 'grid'
            each feature is a Polygon of the cells bounding box. If 'point' each feature
            is a Point that is the centroid of the cell.
        :param query: Query DSL used to filter documents for the search.
        :param runtime_mappings: Defines one or more runtime fields in the search request.
            These fields take precedence over mapped fields with the same name.
        :param size: Maximum number of features to return in the hits layer. Accepts
            0-10000. If 0, results don’t include the hits layer.
        :param sort: Sorts features in the hits layer. By default, the API calculates
            a bounding box for each feature. It sorts features based on this box’s diagonal
            length, from longest to shortest.
        :param track_total_hits: Number of hits matching the query to count accurately.
            If `true`, the exact number of hits is returned at the cost of some performance.
            If `false`, the response does not include the total number of hits matching
            the query.
        :param with_labels: If `true`, the hits and aggs layers will contain additional
            point features representing suggested label positions for the original features.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if field in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'field'")
        if zoom in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'zoom'")
        if x in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'x'")
        if y in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'y'")
        __path_parts: t.Dict[str, str] = {
            "index": _quote(index),
            "field": _quote(field),
            "zoom": _quote(zoom),
            "x": _quote(x),
            "y": _quote(y),
        }
        __path = f'/{__path_parts["index"]}/_mvt/{__path_parts["field"]}/{__path_parts["zoom"]}/{__path_parts["x"]}/{__path_parts["y"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        # The 'sort' parameter with a colon can't be encoded to the body.
        if sort is not None and (
            (isinstance(sort, str) and ":" in sort)
            or (
                isinstance(sort, (list, tuple))
                and all(isinstance(_x, str) for _x in sort)
                and any(":" in _x for _x in sort)
            )
        ):
            __query["sort"] = sort
            sort = None
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if aggs is not None:
                __body["aggs"] = aggs
            if buffer is not None:
                __body["buffer"] = buffer
            if exact_bounds is not None:
                __body["exact_bounds"] = exact_bounds
            if extent is not None:
                __body["extent"] = extent
            if fields is not None:
                __body["fields"] = fields
            if grid_agg is not None:
                __body["grid_agg"] = grid_agg
            if grid_precision is not None:
                __body["grid_precision"] = grid_precision
            if grid_type is not None:
                __body["grid_type"] = grid_type
            if query is not None:
                __body["query"] = query
            if runtime_mappings is not None:
                __body["runtime_mappings"] = runtime_mappings
            if size is not None:
                __body["size"] = size
            if sort is not None:
                __body["sort"] = sort
            if track_total_hits is not None:
                __body["track_total_hits"] = track_total_hits
            if with_labels is not None:
                __body["with_labels"] = with_labels
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/vnd.mapbox-vector-tile"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="search_mvt",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def search_shards(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information about the indices and shards that a search request would
        be executed against.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-shards.html>`_

        :param index: Returns the indices and shards that a search request would be executed
            against.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param local: If `true`, the request retrieves information from the local node
            only.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param routing: Custom value used to route operations to a specific shard.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_search_shards'
        else:
            __path_parts = {}
            __path = "/_search_shards"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if local is not None:
            __query["local"] = local
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if routing is not None:
            __query["routing"] = routing
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="search_shards",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("explain", "id", "params", "profile", "source"),
        ignore_deprecated_options={"params"},
    )
    def search_template(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        ccs_minimize_roundtrips: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        explain: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        id: t.Optional[str] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        params: t.Optional[t.Mapping[str, t.Any]] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        profile: t.Optional[bool] = None,
        rest_total_hits_as_int: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        scroll: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        search_type: t.Optional[
            t.Union["t.Literal['dfs_query_then_fetch', 'query_then_fetch']", str]
        ] = None,
        source: t.Optional[str] = None,
        typed_keys: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to use the Mustache language to pre-render a search definition.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-template.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases to search.
            Supports wildcards (*).
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param ccs_minimize_roundtrips: If `true`, network round-trips are minimized
            for cross-cluster search requests.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param explain: If `true`, returns detailed information about score calculation
            as part of each hit.
        :param id: ID of the search template to use. If no source is specified, this
            parameter is required.
        :param ignore_throttled: If `true`, specified concrete, expanded, or aliased
            indices are not included in the response when throttled.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param params: Key-value pairs used to replace Mustache variables in the template.
            The key is the variable name. The value is the variable value.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param profile: If `true`, the query execution is profiled.
        :param rest_total_hits_as_int: If true, hits.total are rendered as an integer
            in the response.
        :param routing: Custom value used to route operations to a specific shard.
        :param scroll: Specifies how long a consistent view of the index should be maintained
            for scrolled search.
        :param search_type: The type of the search operation.
        :param source: An inline search template. Supports the same parameters as the
            search API's request body. Also supports Mustache variables. If no id is
            specified, this parameter is required.
        :param typed_keys: If `true`, the response prefixes aggregation and suggester
            names with their respective types.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_search/template'
        else:
            __path_parts = {}
            __path = "/_search/template"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if ccs_minimize_roundtrips is not None:
            __query["ccs_minimize_roundtrips"] = ccs_minimize_roundtrips
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_throttled is not None:
            __query["ignore_throttled"] = ignore_throttled
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if rest_total_hits_as_int is not None:
            __query["rest_total_hits_as_int"] = rest_total_hits_as_int
        if routing is not None:
            __query["routing"] = routing
        if scroll is not None:
            __query["scroll"] = scroll
        if search_type is not None:
            __query["search_type"] = search_type
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        if not __body:
            if explain is not None:
                __body["explain"] = explain
            if id is not None:
                __body["id"] = id
            if params is not None:
                __body["params"] = params
            if profile is not None:
                __body["profile"] = profile
            if source is not None:
                __body["source"] = source
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="search_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "field",
            "case_insensitive",
            "index_filter",
            "search_after",
            "size",
            "string",
            "timeout",
        ),
    )
    def terms_enum(
        self,
        *,
        index: str,
        field: t.Optional[str] = None,
        case_insensitive: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        index_filter: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        search_after: t.Optional[str] = None,
        size: t.Optional[int] = None,
        string: t.Optional[str] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        The terms enum API can be used to discover terms in the index that begin with
        the provided string. It is designed for low-latency look-ups used in auto-complete
        scenarios.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-terms-enum.html>`_

        :param index: Comma-separated list of data streams, indices, and index aliases
            to search. Wildcard (*) expressions are supported.
        :param field: The string to match at the start of indexed terms. If not provided,
            all terms in the field are considered.
        :param case_insensitive: When true the provided search string is matched against
            index terms without case sensitivity.
        :param index_filter: Allows to filter an index shard if the provided query rewrites
            to match_none.
        :param search_after:
        :param size: How many matching terms to return.
        :param string: The string after which terms in the index should be returned.
            Allows for a form of pagination if the last result from one request is passed
            as the search_after parameter for a subsequent request.
        :param timeout: The maximum length of time to spend collecting results. Defaults
            to "1s" (one second). If the timeout is exceeded the complete flag set to
            false in the response and the results may be partial or empty.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if field is None and body is None:
            raise ValueError("Empty value passed for parameter 'field'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_terms_enum'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if field is not None:
                __body["field"] = field
            if case_insensitive is not None:
                __body["case_insensitive"] = case_insensitive
            if index_filter is not None:
                __body["index_filter"] = index_filter
            if search_after is not None:
                __body["search_after"] = search_after
            if size is not None:
                __body["size"] = size
            if string is not None:
                __body["string"] = string
            if timeout is not None:
                __body["timeout"] = timeout
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="terms_enum",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("doc", "filter", "per_field_analyzer"),
    )
    def termvectors(
        self,
        *,
        index: str,
        id: t.Optional[str] = None,
        doc: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        field_statistics: t.Optional[bool] = None,
        fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filter: t.Optional[t.Mapping[str, t.Any]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        offsets: t.Optional[bool] = None,
        payloads: t.Optional[bool] = None,
        per_field_analyzer: t.Optional[t.Mapping[str, str]] = None,
        positions: t.Optional[bool] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        realtime: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        term_statistics: t.Optional[bool] = None,
        version: t.Optional[int] = None,
        version_type: t.Optional[
            t.Union["t.Literal['external', 'external_gte', 'force', 'internal']", str]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information and statistics about terms in the fields of a particular
        document.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-termvectors.html>`_

        :param index: Name of the index that contains the document.
        :param id: Unique identifier of the document.
        :param doc: An artificial document (a document not present in the index) for
            which you want to retrieve term vectors.
        :param field_statistics: If `true`, the response includes the document count,
            sum of document frequencies, and sum of total term frequencies.
        :param fields: Comma-separated list or wildcard expressions of fields to include
            in the statistics. Used as the default list unless a specific field list
            is provided in the `completion_fields` or `fielddata_fields` parameters.
        :param filter: Filter terms based on their tf-idf scores.
        :param offsets: If `true`, the response includes term offsets.
        :param payloads: If `true`, the response includes term payloads.
        :param per_field_analyzer: Overrides the default per-field analyzer.
        :param positions: If `true`, the response includes term positions.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param realtime: If true, the request is real-time as opposed to near-real-time.
        :param routing: Custom value used to route operations to a specific shard.
        :param term_statistics: If `true`, the response includes term frequency and document
            frequency.
        :param version: If `true`, returns the document version as part of a hit.
        :param version_type: Specific version type.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH and id not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index), "id": _quote(id)}
            __path = f'/{__path_parts["index"]}/_termvectors/{__path_parts["id"]}'
        elif index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_termvectors'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if field_statistics is not None:
            __query["field_statistics"] = field_statistics
        if fields is not None:
            __query["fields"] = fields
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if offsets is not None:
            __query["offsets"] = offsets
        if payloads is not None:
            __query["payloads"] = payloads
        if positions is not None:
            __query["positions"] = positions
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if realtime is not None:
            __query["realtime"] = realtime
        if routing is not None:
            __query["routing"] = routing
        if term_statistics is not None:
            __query["term_statistics"] = term_statistics
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        if not __body:
            if doc is not None:
                __body["doc"] = doc
            if filter is not None:
                __body["filter"] = filter
            if per_field_analyzer is not None:
                __body["per_field_analyzer"] = per_field_analyzer
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="termvectors",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "detect_noop",
            "doc",
            "doc_as_upsert",
            "script",
            "scripted_upsert",
            "source",
            "upsert",
        ),
        parameter_aliases={
            "_source": "source",
            "_source_excludes": "source_excludes",
            "_source_includes": "source_includes",
        },
    )
    def update(
        self,
        *,
        index: str,
        id: str,
        detect_noop: t.Optional[bool] = None,
        doc: t.Optional[t.Mapping[str, t.Any]] = None,
        doc_as_upsert: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        if_primary_term: t.Optional[int] = None,
        if_seq_no: t.Optional[int] = None,
        lang: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union["t.Literal['false', 'true', 'wait_for']", bool, str]
        ] = None,
        require_alias: t.Optional[bool] = None,
        retry_on_conflict: t.Optional[int] = None,
        routing: t.Optional[str] = None,
        script: t.Optional[t.Mapping[str, t.Any]] = None,
        scripted_upsert: t.Optional[bool] = None,
        source: t.Optional[t.Union[bool, t.Mapping[str, t.Any]]] = None,
        source_excludes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        source_includes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        upsert: t.Optional[t.Mapping[str, t.Any]] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates a document with a script or partial document.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-update.html>`_

        :param index: The name of the index
        :param id: Document ID
        :param detect_noop: Set to false to disable setting 'result' in the response
            to 'noop' if no change to the document occurred.
        :param doc: A partial update to an existing document.
        :param doc_as_upsert: Set to true to use the contents of 'doc' as the value of
            'upsert'
        :param if_primary_term: Only perform the operation if the document has this primary
            term.
        :param if_seq_no: Only perform the operation if the document has this sequence
            number.
        :param lang: The script language.
        :param refresh: If 'true', Elasticsearch refreshes the affected shards to make
            this operation visible to search, if 'wait_for' then wait for a refresh to
            make this operation visible to search, if 'false' do nothing with refreshes.
        :param require_alias: If true, the destination must be an index alias.
        :param retry_on_conflict: Specify how many times should the operation be retried
            when a conflict occurs.
        :param routing: Custom value used to route operations to a specific shard.
        :param script: Script to execute to update the document.
        :param scripted_upsert: Set to true to execute the script whether or not the
            document exists.
        :param source: Set to false to disable source retrieval. You can also specify
            a comma-separated list of the fields you want to retrieve.
        :param source_excludes: Specify the source fields you want to exclude.
        :param source_includes: Specify the source fields you want to retrieve.
        :param timeout: Period to wait for dynamic mapping updates and active shards.
            This guarantees Elasticsearch waits for at least the timeout before failing.
            The actual wait time could be longer, particularly when multiple waits occur.
        :param upsert: If the document does not already exist, the contents of 'upsert'
            are inserted as a new document. If the document exists, the 'script' is executed.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operations. Set to 'all' or any positive integer
            up to the total number of shards in the index (number_of_replicas+1). Defaults
            to 1 meaning the primary shard.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "id": _quote(id)}
        __path = f'/{__path_parts["index"]}/_update/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if if_primary_term is not None:
            __query["if_primary_term"] = if_primary_term
        if if_seq_no is not None:
            __query["if_seq_no"] = if_seq_no
        if lang is not None:
            __query["lang"] = lang
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if require_alias is not None:
            __query["require_alias"] = require_alias
        if retry_on_conflict is not None:
            __query["retry_on_conflict"] = retry_on_conflict
        if routing is not None:
            __query["routing"] = routing
        if source_excludes is not None:
            __query["_source_excludes"] = source_excludes
        if source_includes is not None:
            __query["_source_includes"] = source_includes
        if timeout is not None:
            __query["timeout"] = timeout
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        if not __body:
            if detect_noop is not None:
                __body["detect_noop"] = detect_noop
            if doc is not None:
                __body["doc"] = doc
            if doc_as_upsert is not None:
                __body["doc_as_upsert"] = doc_as_upsert
            if script is not None:
                __body["script"] = script
            if scripted_upsert is not None:
                __body["scripted_upsert"] = scripted_upsert
            if source is not None:
                __body["_source"] = source
            if upsert is not None:
                __body["upsert"] = upsert
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="update",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("conflicts", "max_docs", "query", "script", "slice"),
        parameter_aliases={"from": "from_"},
    )
    def update_by_query(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        allow_no_indices: t.Optional[bool] = None,
        analyze_wildcard: t.Optional[bool] = None,
        analyzer: t.Optional[str] = None,
        conflicts: t.Optional[t.Union["t.Literal['abort', 'proceed']", str]] = None,
        default_operator: t.Optional[t.Union["t.Literal['and', 'or']", str]] = None,
        df: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        lenient: t.Optional[bool] = None,
        max_docs: t.Optional[int] = None,
        pipeline: t.Optional[str] = None,
        preference: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        refresh: t.Optional[bool] = None,
        request_cache: t.Optional[bool] = None,
        requests_per_second: t.Optional[float] = None,
        routing: t.Optional[str] = None,
        script: t.Optional[t.Mapping[str, t.Any]] = None,
        scroll: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        scroll_size: t.Optional[int] = None,
        search_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        search_type: t.Optional[
            t.Union["t.Literal['dfs_query_then_fetch', 'query_then_fetch']", str]
        ] = None,
        slice: t.Optional[t.Mapping[str, t.Any]] = None,
        slices: t.Optional[t.Union[int, t.Union["t.Literal['auto']", str]]] = None,
        sort: t.Optional[t.Sequence[str]] = None,
        stats: t.Optional[t.Sequence[str]] = None,
        terminate_after: t.Optional[int] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        version: t.Optional[bool] = None,
        version_type: t.Optional[bool] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union["t.Literal['all', 'index-setting']", str]]
        ] = None,
        wait_for_completion: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates documents that match the specified query. If no query is specified, performs
        an update on every document in the index without changing the source, for example
        to pick up a mapping change.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-update-by-query.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases to search.
            Supports wildcards (`*`). To search all data streams or indices, omit this
            parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param analyze_wildcard: If `true`, wildcard and prefix queries are analyzed.
        :param analyzer: Analyzer to use for the query string.
        :param conflicts: What to do if update by query hits version conflicts: `abort`
            or `proceed`.
        :param default_operator: The default operator for query string query: `AND` or
            `OR`.
        :param df: Field to use as default where no field prefix is given in the query
            string.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param from_: Starting offset (default: 0)
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param lenient: If `true`, format-based query failures (such as providing text
            to a numeric field) in the query string will be ignored.
        :param max_docs: The maximum number of documents to update.
        :param pipeline: ID of the pipeline to use to preprocess incoming documents.
            If the index has a default ingest pipeline specified, then setting the value
            to `_none` disables the default ingest pipeline for this request. If a final
            pipeline is configured it will always run, regardless of the value of this
            parameter.
        :param preference: Specifies the node or shard the operation should be performed
            on. Random by default.
        :param query: Specifies the documents to update using the Query DSL.
        :param refresh: If `true`, Elasticsearch refreshes affected shards to make the
            operation visible to search.
        :param request_cache: If `true`, the request cache is used for this request.
        :param requests_per_second: The throttle for this request in sub-requests per
            second.
        :param routing: Custom value used to route operations to a specific shard.
        :param script: The script to run to update the document source or metadata when
            updating.
        :param scroll: Period to retain the search context for scrolling.
        :param scroll_size: Size of the scroll request that powers the operation.
        :param search_timeout: Explicit timeout for each search request.
        :param search_type: The type of the search operation. Available options: `query_then_fetch`,
            `dfs_query_then_fetch`.
        :param slice: Slice the request manually using the provided slice ID and total
            number of slices.
        :param slices: The number of slices this task should be divided into.
        :param sort: A comma-separated list of <field>:<direction> pairs.
        :param stats: Specific `tag` of the request for logging and statistical purposes.
        :param terminate_after: Maximum number of documents to collect for each shard.
            If a query reaches this limit, Elasticsearch terminates the query early.
            Elasticsearch collects documents before sorting. Use with caution. Elasticsearch
            applies this parameter to each shard handling the request. When possible,
            let Elasticsearch perform early termination automatically. Avoid specifying
            this parameter for requests that target data streams with backing indices
            across multiple data tiers.
        :param timeout: Period each update request waits for the following operations:
            dynamic mapping updates, waiting for active shards.
        :param version: If `true`, returns the document version as part of a hit.
        :param version_type: Should the document increment the version number (internal)
            on hit or not (reindex)
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to `all` or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        :param wait_for_completion: If `true`, the request blocks until the operation
            is complete.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_update_by_query'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        # The 'sort' parameter with a colon can't be encoded to the body.
        if sort is not None and (
            (isinstance(sort, str) and ":" in sort)
            or (
                isinstance(sort, (list, tuple))
                and all(isinstance(_x, str) for _x in sort)
                and any(":" in _x for _x in sort)
            )
        ):
            __query["sort"] = sort
            sort = None
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if analyze_wildcard is not None:
            __query["analyze_wildcard"] = analyze_wildcard
        if analyzer is not None:
            __query["analyzer"] = analyzer
        if default_operator is not None:
            __query["default_operator"] = default_operator
        if df is not None:
            __query["df"] = df
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if lenient is not None:
            __query["lenient"] = lenient
        if pipeline is not None:
            __query["pipeline"] = pipeline
        if preference is not None:
            __query["preference"] = preference
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if request_cache is not None:
            __query["request_cache"] = request_cache
        if requests_per_second is not None:
            __query["requests_per_second"] = requests_per_second
        if routing is not None:
            __query["routing"] = routing
        if scroll is not None:
            __query["scroll"] = scroll
        if scroll_size is not None:
            __query["scroll_size"] = scroll_size
        if search_timeout is not None:
            __query["search_timeout"] = search_timeout
        if search_type is not None:
            __query["search_type"] = search_type
        if slices is not None:
            __query["slices"] = slices
        if sort is not None:
            __query["sort"] = sort
        if stats is not None:
            __query["stats"] = stats
        if terminate_after is not None:
            __query["terminate_after"] = terminate_after
        if timeout is not None:
            __query["timeout"] = timeout
        if version is not None:
            __query["version"] = version
        if version_type is not None:
            __query["version_type"] = version_type
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        if not __body:
            if conflicts is not None:
                __body["conflicts"] = conflicts
            if max_docs is not None:
                __body["max_docs"] = max_docs
            if query is not None:
                __body["query"] = query
            if script is not None:
                __body["script"] = script
            if slice is not None:
                __body["slice"] = slice
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="update_by_query",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def update_by_query_rethrottle(
        self,
        *,
        task_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        requests_per_second: t.Optional[float] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Changes the number of requests per second for a particular Update By Query operation.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/docs-update-by-query.html>`_

        :param task_id: The ID for the task.
        :param requests_per_second: The throttle for this request in sub-requests per
            second.
        """
        if task_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'task_id'")
        __path_parts: t.Dict[str, str] = {"task_id": _quote(task_id)}
        __path = f'/_update_by_query/{__path_parts["task_id"]}/_rethrottle'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if requests_per_second is not None:
            __query["requests_per_second"] = requests_per_second
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="update_by_query_rethrottle",
            path_parts=__path_parts,
        )
