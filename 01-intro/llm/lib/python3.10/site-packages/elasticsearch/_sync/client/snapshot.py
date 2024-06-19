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


class SnapshotClient(NamespacedClient):

    @_rewrite_parameters()
    def cleanup_repository(
        self,
        *,
        name: str,
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
        Removes stale data from repository.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/clean-up-snapshot-repo-api.html>`_

        :param name: Snapshot repository to clean up.
        :param master_timeout: Period to wait for a connection to the master node.
        :param timeout: Period to wait for a response.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"repository": _quote(name)}
        __path = f'/_snapshot/{__path_parts["repository"]}/_cleanup'
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
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="snapshot.cleanup_repository",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("indices",),
    )
    def clone(
        self,
        *,
        repository: str,
        snapshot: str,
        target_snapshot: str,
        indices: t.Optional[str] = None,
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
        Clones indices from one snapshot into another snapshot in the same repository.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param repository: A repository name
        :param snapshot: The name of the snapshot to clone from
        :param target_snapshot: The name of the cloned snapshot to create
        :param indices:
        :param master_timeout: Explicit operation timeout for connection to master node
        :param timeout:
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'repository'")
        if snapshot in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot'")
        if target_snapshot in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'target_snapshot'")
        if indices is None and body is None:
            raise ValueError("Empty value passed for parameter 'indices'")
        __path_parts: t.Dict[str, str] = {
            "repository": _quote(repository),
            "snapshot": _quote(snapshot),
            "target_snapshot": _quote(target_snapshot),
        }
        __path = f'/_snapshot/{__path_parts["repository"]}/{__path_parts["snapshot"]}/_clone/{__path_parts["target_snapshot"]}'
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
            if indices is not None:
                __body["indices"] = indices
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="snapshot.clone",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "feature_states",
            "ignore_unavailable",
            "include_global_state",
            "indices",
            "metadata",
            "partial",
        ),
    )
    def create(
        self,
        *,
        repository: str,
        snapshot: str,
        error_trace: t.Optional[bool] = None,
        feature_states: t.Optional[t.Sequence[str]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        include_global_state: t.Optional[bool] = None,
        indices: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        metadata: t.Optional[t.Mapping[str, t.Any]] = None,
        partial: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        wait_for_completion: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a snapshot in a repository.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param repository: Repository for the snapshot.
        :param snapshot: Name of the snapshot. Must be unique in the repository.
        :param feature_states: Feature states to include in the snapshot. Each feature
            state includes one or more system indices containing related data. You can
            view a list of eligible features using the get features API. If `include_global_state`
            is `true`, all current feature states are included by default. If `include_global_state`
            is `false`, no feature states are included by default.
        :param ignore_unavailable: If `true`, the request ignores data streams and indices
            in `indices` that are missing or closed. If `false`, the request returns
            an error for any data stream or index that is missing or closed.
        :param include_global_state: If `true`, the current cluster state is included
            in the snapshot. The cluster state includes persistent cluster settings,
            composable index templates, legacy index templates, ingest pipelines, and
            ILM policies. It also includes data stored in system indices, such as Watches
            and task records (configurable via `feature_states`).
        :param indices: Data streams and indices to include in the snapshot. Supports
            multi-target syntax. Includes all data streams and indices by default.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param metadata: Optional metadata for the snapshot. May have any contents. Must
            be less than 1024 bytes. This map is not automatically generated by Elasticsearch.
        :param partial: If `true`, allows restoring a partial snapshot of indices with
            unavailable shards. Only shards that were successfully included in the snapshot
            will be restored. All missing shards will be recreated as empty. If `false`,
            the entire restore operation will fail if one or more indices included in
            the snapshot do not have all primary shards available.
        :param wait_for_completion: If `true`, the request returns a response when the
            snapshot is complete. If `false`, the request returns a response when the
            snapshot initializes.
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'repository'")
        if snapshot in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot'")
        __path_parts: t.Dict[str, str] = {
            "repository": _quote(repository),
            "snapshot": _quote(snapshot),
        }
        __path = f'/_snapshot/{__path_parts["repository"]}/{__path_parts["snapshot"]}'
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
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        if not __body:
            if feature_states is not None:
                __body["feature_states"] = feature_states
            if ignore_unavailable is not None:
                __body["ignore_unavailable"] = ignore_unavailable
            if include_global_state is not None:
                __body["include_global_state"] = include_global_state
            if indices is not None:
                __body["indices"] = indices
            if metadata is not None:
                __body["metadata"] = metadata
            if partial is not None:
                __body["partial"] = partial
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="snapshot.create",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="repository",
    )
    def create_repository(
        self,
        *,
        name: str,
        repository: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        verify: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a repository.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param name: A repository name
        :param repository:
        :param master_timeout: Explicit operation timeout for connection to master node
        :param timeout: Explicit operation timeout
        :param verify: Whether to verify the repository after creation
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        if repository is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'repository' and 'body', one of them should be set."
            )
        elif repository is not None and body is not None:
            raise ValueError("Cannot set both 'repository' and 'body'")
        __path_parts: t.Dict[str, str] = {"repository": _quote(name)}
        __path = f'/_snapshot/{__path_parts["repository"]}'
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
        if verify is not None:
            __query["verify"] = verify
        __body = repository if repository is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="snapshot.create_repository",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete(
        self,
        *,
        repository: str,
        snapshot: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes one or more snapshots.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param repository: A repository name
        :param snapshot: A comma-separated list of snapshot names
        :param master_timeout: Explicit operation timeout for connection to master node
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'repository'")
        if snapshot in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot'")
        __path_parts: t.Dict[str, str] = {
            "repository": _quote(repository),
            "snapshot": _quote(snapshot),
        }
        __path = f'/_snapshot/{__path_parts["repository"]}/{__path_parts["snapshot"]}'
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
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="snapshot.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_repository(
        self,
        *,
        name: t.Union[str, t.Sequence[str]],
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
        Deletes a repository.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param name: Name of the snapshot repository to unregister. Wildcard (`*`) patterns
            are supported.
        :param master_timeout: Explicit operation timeout for connection to master node
        :param timeout: Explicit operation timeout
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"repository": _quote(name)}
        __path = f'/_snapshot/{__path_parts["repository"]}'
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
            endpoint_id="snapshot.delete_repository",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get(
        self,
        *,
        repository: str,
        snapshot: t.Union[str, t.Sequence[str]],
        after: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_sort_value: t.Optional[str] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        include_repository: t.Optional[bool] = None,
        index_details: t.Optional[bool] = None,
        index_names: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        offset: t.Optional[int] = None,
        order: t.Optional[t.Union["t.Literal['asc', 'desc']", str]] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        slm_policy_filter: t.Optional[str] = None,
        sort: t.Optional[
            t.Union[
                "t.Literal['duration', 'failed_shard_count', 'index_count', 'name', 'repository', 'shard_count', 'start_time']",
                str,
            ]
        ] = None,
        verbose: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information about a snapshot.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param repository: Comma-separated list of snapshot repository names used to
            limit the request. Wildcard (*) expressions are supported.
        :param snapshot: Comma-separated list of snapshot names to retrieve. Also accepts
            wildcards (*). - To get information about all snapshots in a registered repository,
            use a wildcard (*) or _all. - To get information about any snapshots that
            are currently running, use _current.
        :param after: Offset identifier to start pagination from as returned by the next
            field in the response body.
        :param from_sort_value: Value of the current sort column at which to start retrieval.
            Can either be a string snapshot- or repository name when sorting by snapshot
            or repository name, a millisecond time value or a number when sorting by
            index- or shard count.
        :param ignore_unavailable: If false, the request returns an error for any snapshots
            that are unavailable.
        :param include_repository: If true, returns the repository name in each snapshot.
        :param index_details: If true, returns additional information about each index
            in the snapshot comprising the number of shards in the index, the total size
            of the index in bytes, and the maximum number of segments per shard in the
            index. Defaults to false, meaning that this information is omitted.
        :param index_names: If true, returns the name of each index in each snapshot.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param offset: Numeric offset to start pagination from based on the snapshots
            matching this request. Using a non-zero value for this parameter is mutually
            exclusive with using the after parameter. Defaults to 0.
        :param order: Sort order. Valid values are asc for ascending and desc for descending
            order. Defaults to asc, meaning ascending order.
        :param size: Maximum number of snapshots to return. Defaults to 0 which means
            return all that match the request without limit.
        :param slm_policy_filter: Filter snapshots by a comma-separated list of SLM policy
            names that snapshots belong to. Also accepts wildcards (*) and combinations
            of wildcards followed by exclude patterns starting with -. To include snapshots
            not created by an SLM policy you can use the special pattern _none that will
            match all snapshots without an SLM policy.
        :param sort: Allows setting a sort order for the result. Defaults to start_time,
            i.e. sorting by snapshot start time stamp.
        :param verbose: If true, returns additional information about each snapshot such
            as the version of Elasticsearch which took the snapshot, the start and end
            times of the snapshot, and the number of shards snapshotted.
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'repository'")
        if snapshot in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot'")
        __path_parts: t.Dict[str, str] = {
            "repository": _quote(repository),
            "snapshot": _quote(snapshot),
        }
        __path = f'/_snapshot/{__path_parts["repository"]}/{__path_parts["snapshot"]}'
        __query: t.Dict[str, t.Any] = {}
        if after is not None:
            __query["after"] = after
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_sort_value is not None:
            __query["from_sort_value"] = from_sort_value
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if include_repository is not None:
            __query["include_repository"] = include_repository
        if index_details is not None:
            __query["index_details"] = index_details
        if index_names is not None:
            __query["index_names"] = index_names
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if offset is not None:
            __query["offset"] = offset
        if order is not None:
            __query["order"] = order
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if slm_policy_filter is not None:
            __query["slm_policy_filter"] = slm_policy_filter
        if sort is not None:
            __query["sort"] = sort
        if verbose is not None:
            __query["verbose"] = verbose
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="snapshot.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_repository(
        self,
        *,
        name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information about a repository.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param name: A comma-separated list of repository names
        :param local: Return local information, do not retrieve the state from master
            node (default: false)
        :param master_timeout: Explicit operation timeout for connection to master node
        """
        __path_parts: t.Dict[str, str]
        if name not in SKIP_IN_PATH:
            __path_parts = {"repository": _quote(name)}
            __path = f'/_snapshot/{__path_parts["repository"]}'
        else:
            __path_parts = {}
            __path = "/_snapshot"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
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
            endpoint_id="snapshot.get_repository",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "feature_states",
            "ignore_index_settings",
            "ignore_unavailable",
            "include_aliases",
            "include_global_state",
            "index_settings",
            "indices",
            "partial",
            "rename_pattern",
            "rename_replacement",
        ),
    )
    def restore(
        self,
        *,
        repository: str,
        snapshot: str,
        error_trace: t.Optional[bool] = None,
        feature_states: t.Optional[t.Sequence[str]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_index_settings: t.Optional[t.Sequence[str]] = None,
        ignore_unavailable: t.Optional[bool] = None,
        include_aliases: t.Optional[bool] = None,
        include_global_state: t.Optional[bool] = None,
        index_settings: t.Optional[t.Mapping[str, t.Any]] = None,
        indices: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        partial: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        rename_pattern: t.Optional[str] = None,
        rename_replacement: t.Optional[str] = None,
        wait_for_completion: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Restores a snapshot.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param repository: A repository name
        :param snapshot: A snapshot name
        :param feature_states:
        :param ignore_index_settings:
        :param ignore_unavailable:
        :param include_aliases:
        :param include_global_state:
        :param index_settings:
        :param indices:
        :param master_timeout: Explicit operation timeout for connection to master node
        :param partial:
        :param rename_pattern:
        :param rename_replacement:
        :param wait_for_completion: Should this request wait until the operation has
            completed before returning
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'repository'")
        if snapshot in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot'")
        __path_parts: t.Dict[str, str] = {
            "repository": _quote(repository),
            "snapshot": _quote(snapshot),
        }
        __path = f'/_snapshot/{__path_parts["repository"]}/{__path_parts["snapshot"]}/_restore'
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
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        if not __body:
            if feature_states is not None:
                __body["feature_states"] = feature_states
            if ignore_index_settings is not None:
                __body["ignore_index_settings"] = ignore_index_settings
            if ignore_unavailable is not None:
                __body["ignore_unavailable"] = ignore_unavailable
            if include_aliases is not None:
                __body["include_aliases"] = include_aliases
            if include_global_state is not None:
                __body["include_global_state"] = include_global_state
            if index_settings is not None:
                __body["index_settings"] = index_settings
            if indices is not None:
                __body["indices"] = indices
            if partial is not None:
                __body["partial"] = partial
            if rename_pattern is not None:
                __body["rename_pattern"] = rename_pattern
            if rename_replacement is not None:
                __body["rename_replacement"] = rename_replacement
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
            endpoint_id="snapshot.restore",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def status(
        self,
        *,
        repository: t.Optional[str] = None,
        snapshot: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information about the status of a snapshot.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param repository: A repository name
        :param snapshot: A comma-separated list of snapshot names
        :param ignore_unavailable: Whether to ignore unavailable snapshots, defaults
            to false which means a SnapshotMissingException is thrown
        :param master_timeout: Explicit operation timeout for connection to master node
        """
        __path_parts: t.Dict[str, str]
        if repository not in SKIP_IN_PATH and snapshot not in SKIP_IN_PATH:
            __path_parts = {
                "repository": _quote(repository),
                "snapshot": _quote(snapshot),
            }
            __path = f'/_snapshot/{__path_parts["repository"]}/{__path_parts["snapshot"]}/_status'
        elif repository not in SKIP_IN_PATH:
            __path_parts = {"repository": _quote(repository)}
            __path = f'/_snapshot/{__path_parts["repository"]}/_status'
        else:
            __path_parts = {}
            __path = "/_snapshot/_status"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
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
            endpoint_id="snapshot.status",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def verify_repository(
        self,
        *,
        name: str,
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
        Verifies a repository.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-snapshots.html>`_

        :param name: A repository name
        :param master_timeout: Explicit operation timeout for connection to master node
        :param timeout: Explicit operation timeout
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"repository": _quote(name)}
        __path = f'/_snapshot/{__path_parts["repository"]}/_verify'
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
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="snapshot.verify_repository",
            path_parts=__path_parts,
        )
