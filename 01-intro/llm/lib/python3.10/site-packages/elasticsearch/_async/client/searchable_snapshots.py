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

from elastic_transport import ObjectApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class SearchableSnapshotsClient(NamespacedClient):

    @_rewrite_parameters()
    async def cache_stats(
        self,
        *,
        node_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieve node-level cache statistics about searchable snapshots.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/searchable-snapshots-apis.html>`_

        :param node_id: A comma-separated list of node IDs or names to limit the returned
            information; use `_local` to return information from the node you're connecting
            to, leave empty to get information from all nodes
        :param master_timeout:
        """
        __path_parts: t.Dict[str, str]
        if node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_searchable_snapshots/{__path_parts["node_id"]}/cache/stats'
        else:
            __path_parts = {}
            __path = "/_searchable_snapshots/cache/stats"
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
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="searchable_snapshots.cache_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def clear_cache(
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
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Clear the cache of searchable snapshots.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/searchable-snapshots-apis.html>`_

        :param index: A comma-separated list of index names
        :param allow_no_indices: Whether to ignore if a wildcard indices expression resolves
            into no concrete indices. (This includes `_all` string or when no indices
            have been specified)
        :param expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :param ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_searchable_snapshots/cache/clear'
        else:
            __path_parts = {}
            __path = "/_searchable_snapshots/cache/clear"
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
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="searchable_snapshots.clear_cache",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "index",
            "ignore_index_settings",
            "index_settings",
            "renamed_index",
        ),
    )
    async def mount(
        self,
        *,
        repository: str,
        snapshot: str,
        index: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_index_settings: t.Optional[t.Sequence[str]] = None,
        index_settings: t.Optional[t.Mapping[str, t.Any]] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        renamed_index: t.Optional[str] = None,
        storage: t.Optional[str] = None,
        wait_for_completion: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Mount a snapshot as a searchable index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/searchable-snapshots-api-mount-snapshot.html>`_

        :param repository: The name of the repository containing the snapshot of the
            index to mount
        :param snapshot: The name of the snapshot of the index to mount
        :param index:
        :param ignore_index_settings:
        :param index_settings:
        :param master_timeout: Explicit operation timeout for connection to master node
        :param renamed_index:
        :param storage: Selects the kind of local storage used to accelerate searches.
            Experimental, and defaults to `full_copy`
        :param wait_for_completion: Should this request wait until the operation has
            completed before returning
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'repository'")
        if snapshot in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot'")
        if index is None and body is None:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {
            "repository": _quote(repository),
            "snapshot": _quote(snapshot),
        }
        __path = (
            f'/_snapshot/{__path_parts["repository"]}/{__path_parts["snapshot"]}/_mount'
        )
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
        if storage is not None:
            __query["storage"] = storage
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        if not __body:
            if index is not None:
                __body["index"] = index
            if ignore_index_settings is not None:
                __body["ignore_index_settings"] = ignore_index_settings
            if index_settings is not None:
                __body["index_settings"] = index_settings
            if renamed_index is not None:
                __body["renamed_index"] = renamed_index
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="searchable_snapshots.mount",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def stats(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        level: t.Optional[
            t.Union["t.Literal['cluster', 'indices', 'shards']", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieve shard-level statistics about searchable snapshots.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/searchable-snapshots-apis.html>`_

        :param index: A comma-separated list of index names
        :param level: Return stats aggregated at cluster, index or shard level
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_searchable_snapshots/stats'
        else:
            __path_parts = {}
            __path = "/_searchable_snapshots/stats"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if level is not None:
            __query["level"] = level
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="searchable_snapshots.stats",
            path_parts=__path_parts,
        )
