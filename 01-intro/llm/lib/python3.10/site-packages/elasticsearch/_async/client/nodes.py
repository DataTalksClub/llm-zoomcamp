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

import typing as t

from elastic_transport import ObjectApiResponse, TextApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class NodesClient(NamespacedClient):

    @_rewrite_parameters()
    async def clear_repositories_metering_archive(
        self,
        *,
        node_id: t.Union[str, t.Sequence[str]],
        max_archive_version: int,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Removes the archived repositories metering information present in the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/clear-repositories-metering-archive-api.html>`_

        :param node_id: Comma-separated list of node IDs or names used to limit returned
            information. All the nodes selective options are explained [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster.html#cluster-nodes).
        :param max_archive_version: Specifies the maximum [archive_version](https://www.elastic.co/guide/en/elasticsearch/reference/current/get-repositories-metering-api.html#get-repositories-metering-api-response-body)
            to be cleared from the archive.
        """
        if node_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'node_id'")
        if max_archive_version in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'max_archive_version'")
        __path_parts: t.Dict[str, str] = {
            "node_id": _quote(node_id),
            "max_archive_version": _quote(max_archive_version),
        }
        __path = f'/_nodes/{__path_parts["node_id"]}/_repositories_metering/{__path_parts["max_archive_version"]}'
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
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="nodes.clear_repositories_metering_archive",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_repositories_metering_info(
        self,
        *,
        node_id: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns cluster repositories metering information.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-repositories-metering-api.html>`_

        :param node_id: Comma-separated list of node IDs or names used to limit returned
            information. All the nodes selective options are explained [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster.html#cluster-nodes).
        """
        if node_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'node_id'")
        __path_parts: t.Dict[str, str] = {"node_id": _quote(node_id)}
        __path = f'/_nodes/{__path_parts["node_id"]}/_repositories_metering'
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
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="nodes.get_repositories_metering_info",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def hot_threads(
        self,
        *,
        node_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_idle_threads: t.Optional[bool] = None,
        interval: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        snapshots: t.Optional[int] = None,
        sort: t.Optional[
            t.Union["t.Literal['block', 'cpu', 'gpu', 'mem', 'wait']", str]
        ] = None,
        threads: t.Optional[int] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        type: t.Optional[
            t.Union["t.Literal['block', 'cpu', 'gpu', 'mem', 'wait']", str]
        ] = None,
    ) -> TextApiResponse:
        """
        Returns information about hot threads on each node in the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/cluster-nodes-hot-threads.html>`_

        :param node_id: List of node IDs or names used to limit returned information.
        :param ignore_idle_threads: If true, known idle threads (e.g. waiting in a socket
            select, or to get a task from an empty queue) are filtered out.
        :param interval: The interval to do the second sampling of threads.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param snapshots: Number of samples of thread stacktrace.
        :param sort: The sort order for 'cpu' type (default: total)
        :param threads: Specifies the number of hot threads to provide information for.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        :param type: The type to sample.
        """
        __path_parts: t.Dict[str, str]
        if node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_nodes/{__path_parts["node_id"]}/hot_threads'
        else:
            __path_parts = {}
            __path = "/_nodes/hot_threads"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_idle_threads is not None:
            __query["ignore_idle_threads"] = ignore_idle_threads
        if interval is not None:
            __query["interval"] = interval
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if snapshots is not None:
            __query["snapshots"] = snapshots
        if sort is not None:
            __query["sort"] = sort
        if threads is not None:
            __query["threads"] = threads
        if timeout is not None:
            __query["timeout"] = timeout
        if type is not None:
            __query["type"] = type
        __headers = {"accept": "text/plain"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="nodes.hot_threads",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def info(
        self,
        *,
        node_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        metric: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        flat_settings: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information about nodes in the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/cluster-nodes-info.html>`_

        :param node_id: Comma-separated list of node IDs or names used to limit returned
            information.
        :param metric: Limits the information returned to the specific metrics. Supports
            a comma-separated list, such as http,ingest.
        :param flat_settings: If true, returns settings in flat format.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        __path_parts: t.Dict[str, str]
        if node_id not in SKIP_IN_PATH and metric not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id), "metric": _quote(metric)}
            __path = f'/_nodes/{__path_parts["node_id"]}/{__path_parts["metric"]}'
        elif node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_nodes/{__path_parts["node_id"]}'
        elif metric not in SKIP_IN_PATH:
            __path_parts = {"metric": _quote(metric)}
            __path = f'/_nodes/{__path_parts["metric"]}'
        else:
            __path_parts = {}
            __path = "/_nodes"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if flat_settings is not None:
            __query["flat_settings"] = flat_settings
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="nodes.info",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("secure_settings_password",),
    )
    async def reload_secure_settings(
        self,
        *,
        node_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        secure_settings_password: t.Optional[str] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Reloads secure settings.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/secure-settings.html#reloadable-secure-settings>`_

        :param node_id: The names of particular nodes in the cluster to target.
        :param secure_settings_password: The password for the Elasticsearch keystore.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        __path_parts: t.Dict[str, str]
        if node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_nodes/{__path_parts["node_id"]}/reload_secure_settings'
        else:
            __path_parts = {}
            __path = "/_nodes/reload_secure_settings"
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
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if secure_settings_password is not None:
                __body["secure_settings_password"] = secure_settings_password
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="nodes.reload_secure_settings",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def stats(
        self,
        *,
        node_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        metric: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        index_metric: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        completion_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        fielddata_fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        fields: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        groups: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        include_segment_file_sizes: t.Optional[bool] = None,
        include_unloaded_segments: t.Optional[bool] = None,
        level: t.Optional[
            t.Union["t.Literal['cluster', 'indices', 'shards']", str]
        ] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        types: t.Optional[t.Sequence[str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns statistical information about nodes in the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/cluster-nodes-stats.html>`_

        :param node_id: Comma-separated list of node IDs or names used to limit returned
            information.
        :param metric: Limit the information returned to the specified metrics
        :param index_metric: Limit the information returned for indices metric to the
            specific index metrics. It can be used only if indices (or all) metric is
            specified.
        :param completion_fields: Comma-separated list or wildcard expressions of fields
            to include in fielddata and suggest statistics.
        :param fielddata_fields: Comma-separated list or wildcard expressions of fields
            to include in fielddata statistics.
        :param fields: Comma-separated list or wildcard expressions of fields to include
            in the statistics.
        :param groups: Comma-separated list of search groups to include in the search
            statistics.
        :param include_segment_file_sizes: If true, the call reports the aggregated disk
            usage of each one of the Lucene index files (only applies if segment stats
            are requested).
        :param include_unloaded_segments: If `true`, the response includes information
            from segments that are not loaded into memory.
        :param level: Indicates whether statistics are aggregated at the cluster, index,
            or shard level.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        :param types: A comma-separated list of document types for the indexing index
            metric.
        """
        __path_parts: t.Dict[str, str]
        if (
            node_id not in SKIP_IN_PATH
            and metric not in SKIP_IN_PATH
            and index_metric not in SKIP_IN_PATH
        ):
            __path_parts = {
                "node_id": _quote(node_id),
                "metric": _quote(metric),
                "index_metric": _quote(index_metric),
            }
            __path = f'/_nodes/{__path_parts["node_id"]}/stats/{__path_parts["metric"]}/{__path_parts["index_metric"]}'
        elif node_id not in SKIP_IN_PATH and metric not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id), "metric": _quote(metric)}
            __path = f'/_nodes/{__path_parts["node_id"]}/stats/{__path_parts["metric"]}'
        elif metric not in SKIP_IN_PATH and index_metric not in SKIP_IN_PATH:
            __path_parts = {
                "metric": _quote(metric),
                "index_metric": _quote(index_metric),
            }
            __path = (
                f'/_nodes/stats/{__path_parts["metric"]}/{__path_parts["index_metric"]}'
            )
        elif node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_nodes/{__path_parts["node_id"]}/stats'
        elif metric not in SKIP_IN_PATH:
            __path_parts = {"metric": _quote(metric)}
            __path = f'/_nodes/stats/{__path_parts["metric"]}'
        else:
            __path_parts = {}
            __path = "/_nodes/stats"
        __query: t.Dict[str, t.Any] = {}
        if completion_fields is not None:
            __query["completion_fields"] = completion_fields
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if fielddata_fields is not None:
            __query["fielddata_fields"] = fielddata_fields
        if fields is not None:
            __query["fields"] = fields
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if groups is not None:
            __query["groups"] = groups
        if human is not None:
            __query["human"] = human
        if include_segment_file_sizes is not None:
            __query["include_segment_file_sizes"] = include_segment_file_sizes
        if include_unloaded_segments is not None:
            __query["include_unloaded_segments"] = include_unloaded_segments
        if level is not None:
            __query["level"] = level
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        if types is not None:
            __query["types"] = types
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="nodes.stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def usage(
        self,
        *,
        node_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        metric: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns low-level information about REST actions usage on nodes.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/cluster-nodes-usage.html>`_

        :param node_id: A comma-separated list of node IDs or names to limit the returned
            information; use `_local` to return information from the node you're connecting
            to, leave empty to get information from all nodes
        :param metric: Limits the information returned to the specific metrics. A comma-separated
            list of the following options: `_all`, `rest_actions`.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        __path_parts: t.Dict[str, str]
        if node_id not in SKIP_IN_PATH and metric not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id), "metric": _quote(metric)}
            __path = f'/_nodes/{__path_parts["node_id"]}/usage/{__path_parts["metric"]}'
        elif node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_nodes/{__path_parts["node_id"]}/usage'
        elif metric not in SKIP_IN_PATH:
            __path_parts = {"metric": _quote(metric)}
            __path = f'/_nodes/usage/{__path_parts["metric"]}'
        else:
            __path_parts = {}
            __path = "/_nodes/usage"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="nodes.usage",
            path_parts=__path_parts,
        )
