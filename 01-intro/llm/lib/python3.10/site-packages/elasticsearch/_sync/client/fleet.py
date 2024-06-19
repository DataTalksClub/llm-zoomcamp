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


class FleetClient(NamespacedClient):

    @_rewrite_parameters()
    def global_checkpoints(
        self,
        *,
        index: str,
        checkpoints: t.Optional[t.Sequence[int]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        wait_for_advance: t.Optional[bool] = None,
        wait_for_index: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the current global checkpoints for an index. This API is design for internal
        use by the fleet server project.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-global-checkpoints.html>`_

        :param index: A single index or index alias that resolves to a single index.
        :param checkpoints: A comma separated list of previous global checkpoints. When
            used in combination with `wait_for_advance`, the API will only return once
            the global checkpoints advances past the checkpoints. Providing an empty
            list will cause Elasticsearch to immediately return the current global checkpoints.
        :param timeout: Period to wait for a global checkpoints to advance past `checkpoints`.
        :param wait_for_advance: A boolean value which controls whether to wait (until
            the timeout) for the global checkpoints to advance past the provided `checkpoints`.
        :param wait_for_index: A boolean value which controls whether to wait (until
            the timeout) for the target index to exist and all primary shards be active.
            Can only be true when `wait_for_advance` is true.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_fleet/global_checkpoints'
        __query: t.Dict[str, t.Any] = {}
        if checkpoints is not None:
            __query["checkpoints"] = checkpoints
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
        if wait_for_advance is not None:
            __query["wait_for_advance"] = wait_for_advance
        if wait_for_index is not None:
            __query["wait_for_index"] = wait_for_index
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="fleet.global_checkpoints",
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
        index: t.Optional[str] = None,
        allow_no_indices: t.Optional[bool] = None,
        allow_partial_search_results: t.Optional[bool] = None,
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
        search_type: t.Optional[
            t.Union["t.Literal['dfs_query_then_fetch', 'query_then_fetch']", str]
        ] = None,
        typed_keys: t.Optional[bool] = None,
        wait_for_checkpoints: t.Optional[t.Sequence[int]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Multi Search API where the search will only be executed after specified checkpoints
        are available due to a refresh. This API is designed for internal use by the
        fleet server project.

        :param searches:
        :param index: A single target to search. If the target is an index alias, it
            must resolve to a single index.
        :param allow_no_indices: If false, the request returns an error if any wildcard
            expression, index alias, or _all value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting foo*,bar* returns an error if an index starts
            with foo but no index starts with bar.
        :param allow_partial_search_results: If true, returns partial results if there
            are shard request timeouts or [shard failures](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-replication.html#shard-failures).
            If false, returns an error with no partial results. Defaults to the configured
            cluster setting `search.default_allow_partial_results` which is true by default.
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
        :param search_type: Indicates whether global term and document frequencies should
            be used when scoring returned documents.
        :param typed_keys: Specifies whether aggregation and suggester names should be
            prefixed by their respective types in the response.
        :param wait_for_checkpoints: A comma separated list of checkpoints. When configured,
            the search API will only be executed on a shard after the relevant checkpoint
            has become visible for search. Defaults to an empty list which will cause
            Elasticsearch to immediately execute the search.
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
            __path = f'/{__path_parts["index"]}/_fleet/_fleet_msearch'
        else:
            __path_parts = {}
            __path = "/_fleet/_fleet_msearch"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if allow_partial_search_results is not None:
            __query["allow_partial_search_results"] = allow_partial_search_results
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
        if search_type is not None:
            __query["search_type"] = search_type
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        if wait_for_checkpoints is not None:
            __query["wait_for_checkpoints"] = wait_for_checkpoints
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
            endpoint_id="fleet.msearch",
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
            "min_score",
            "pit",
            "post_filter",
            "profile",
            "query",
            "rescore",
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
        index: str,
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
        from_: t.Optional[int] = None,
        highlight: t.Optional[t.Mapping[str, t.Any]] = None,
        human: t.Optional[bool] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        indices_boost: t.Optional[t.Sequence[t.Mapping[str, float]]] = None,
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
        request_cache: t.Optional[bool] = None,
        rescore: t.Optional[
            t.Union[t.Mapping[str, t.Any], t.Sequence[t.Mapping[str, t.Any]]]
        ] = None,
        rest_total_hits_as_int: t.Optional[bool] = None,
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
        wait_for_checkpoints: t.Optional[t.Sequence[int]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Search API where the search will only be executed after specified checkpoints
        are available due to a refresh. This API is designed for internal use by the
        fleet server project.

        :param index: A single target to search. If the target is an index alias, it
            must resolve to a single index.
        :param aggregations:
        :param aggs:
        :param allow_no_indices:
        :param allow_partial_search_results: If true, returns partial results if there
            are shard request timeouts or [shard failures](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-replication.html#shard-failures).
            If false, returns an error with no partial results. Defaults to the configured
            cluster setting `search.default_allow_partial_results` which is true by default.
        :param analyze_wildcard:
        :param analyzer:
        :param batched_reduce_size:
        :param ccs_minimize_roundtrips:
        :param collapse:
        :param default_operator:
        :param df:
        :param docvalue_fields: Array of wildcard (*) patterns. The request returns doc
            values for field names matching these patterns in the hits.fields property
            of the response.
        :param expand_wildcards:
        :param explain: If true, returns detailed information about score computation
            as part of a hit.
        :param ext: Configuration of search extensions defined by Elasticsearch plugins.
        :param fields: Array of wildcard (*) patterns. The request returns values for
            field names matching these patterns in the hits.fields property of the response.
        :param from_: Starting document offset. By default, you cannot page through more
            than 10,000 hits using the from and size parameters. To page through more
            hits, use the search_after parameter.
        :param highlight:
        :param ignore_throttled:
        :param ignore_unavailable:
        :param indices_boost: Boosts the _score of documents from specified indices.
        :param lenient:
        :param max_concurrent_shard_requests:
        :param min_compatible_shard_node:
        :param min_score: Minimum _score for matching documents. Documents with a lower
            _score are not included in the search results.
        :param pit: Limits the search to a point in time (PIT). If you provide a PIT,
            you cannot specify an <index> in the request path.
        :param post_filter:
        :param pre_filter_shard_size:
        :param preference:
        :param profile:
        :param q:
        :param query: Defines the search definition using the Query DSL.
        :param request_cache:
        :param rescore:
        :param rest_total_hits_as_int:
        :param routing:
        :param runtime_mappings: Defines one or more runtime fields in the search request.
            These fields take precedence over mapped fields with the same name.
        :param script_fields: Retrieve a script evaluation (based on different fields)
            for each hit.
        :param scroll:
        :param search_after:
        :param search_type:
        :param seq_no_primary_term: If true, returns sequence number and primary term
            of the last modification of each hit. See Optimistic concurrency control.
        :param size: The number of hits to return. By default, you cannot page through
            more than 10,000 hits using the from and size parameters. To page through
            more hits, use the search_after parameter.
        :param slice:
        :param sort:
        :param source: Indicates which source fields are returned for matching documents.
            These fields are returned in the hits._source property of the search response.
        :param source_excludes:
        :param source_includes:
        :param stats: Stats groups to associate with the search. Each group maintains
            a statistics aggregation for its associated searches. You can retrieve these
            stats using the indices stats API.
        :param stored_fields: List of stored fields to return as part of a hit. If no
            fields are specified, no stored fields are included in the response. If this
            field is specified, the _source parameter defaults to false. You can pass
            _source: true to return both source fields and stored fields in the search
            response.
        :param suggest:
        :param suggest_field: Specifies which field to use for suggestions.
        :param suggest_mode:
        :param suggest_size:
        :param suggest_text: The source text for which the suggestions should be returned.
        :param terminate_after: Maximum number of documents to collect for each shard.
            If a query reaches this limit, Elasticsearch terminates the query early.
            Elasticsearch collects documents before sorting. Defaults to 0, which does
            not terminate query execution early.
        :param timeout: Specifies the period of time to wait for a response from each
            shard. If no response is received before the timeout expires, the request
            fails and returns an error. Defaults to no timeout.
        :param track_scores: If true, calculate and return document scores, even if the
            scores are not used for sorting.
        :param track_total_hits: Number of hits matching the query to count accurately.
            If true, the exact number of hits is returned at the cost of some performance.
            If false, the response does not include the total number of hits matching
            the query. Defaults to 10,000 hits.
        :param typed_keys:
        :param version: If true, returns document version as part of a hit.
        :param wait_for_checkpoints: A comma separated list of checkpoints. When configured,
            the search API will only be executed on a shard after the relevant checkpoint
            has become visible for search. Defaults to an empty list which will cause
            Elasticsearch to immediately execute the search.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_fleet/_fleet_search'
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
        if wait_for_checkpoints is not None:
            __query["wait_for_checkpoints"] = wait_for_checkpoints
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
            if rescore is not None:
                __body["rescore"] = rescore
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
            endpoint_id="fleet.search",
            path_parts=__path_parts,
        )
