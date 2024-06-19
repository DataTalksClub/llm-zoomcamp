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


class AsyncSearchClient(NamespacedClient):

    @_rewrite_parameters()
    def delete(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an async search by ID. If the search is still running, the search request
        will be cancelled. Otherwise, the saved search results are deleted.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/async-search.html>`_

        :param id: A unique identifier for the async search.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_async_search/{__path_parts["id"]}'
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
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="async_search.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        keep_alive: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        pretty: t.Optional[bool] = None,
        typed_keys: t.Optional[bool] = None,
        wait_for_completion_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves the results of a previously submitted async search request given its
        ID.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/async-search.html>`_

        :param id: A unique identifier for the async search.
        :param keep_alive: Specifies how long the async search should be available in
            the cluster. When not specified, the `keep_alive` set with the corresponding
            submit async request will be used. Otherwise, it is possible to override
            the value and extend the validity of the request. When this period expires,
            the search, if still running, is cancelled. If the search is completed, its
            saved results are deleted.
        :param typed_keys: Specify whether aggregation and suggester names should be
            prefixed by their respective types in the response
        :param wait_for_completion_timeout: Specifies to wait for the search to be completed
            up until the provided timeout. Final results will be returned if available
            before the timeout expires, otherwise the currently available results will
            be returned once the timeout expires. By default no timeout is set meaning
            that the currently available results will be returned without any additional
            wait.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_async_search/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if keep_alive is not None:
            __query["keep_alive"] = keep_alive
        if pretty is not None:
            __query["pretty"] = pretty
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        if wait_for_completion_timeout is not None:
            __query["wait_for_completion_timeout"] = wait_for_completion_timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="async_search.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def status(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves the status of a previously submitted async search request given its
        ID.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/async-search.html>`_

        :param id: A unique identifier for the async search.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_async_search/status/{__path_parts["id"]}'
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
            endpoint_id="async_search.status",
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
    def submit(
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
        from_: t.Optional[int] = None,
        highlight: t.Optional[t.Mapping[str, t.Any]] = None,
        human: t.Optional[bool] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        indices_boost: t.Optional[t.Sequence[t.Mapping[str, float]]] = None,
        keep_alive: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        keep_on_completion: t.Optional[bool] = None,
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
        wait_for_completion_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Executes a search request asynchronously.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/async-search.html>`_

        :param index: A comma-separated list of index names to search; use `_all` or
            empty string to perform the operation on all indices
        :param aggregations:
        :param aggs:
        :param allow_no_indices: Whether to ignore if a wildcard indices expression resolves
            into no concrete indices. (This includes `_all` string or when no indices
            have been specified)
        :param allow_partial_search_results: Indicate if an error should be returned
            if there is a partial search failure or timeout
        :param analyze_wildcard: Specify whether wildcard and prefix queries should be
            analyzed (default: false)
        :param analyzer: The analyzer to use for the query string
        :param batched_reduce_size: Affects how often partial results become available,
            which happens whenever shard results are reduced. A partial reduction is
            performed every time the coordinating node has received a certain number
            of new shard responses (5 by default).
        :param ccs_minimize_roundtrips: The default value is the only supported value.
        :param collapse:
        :param default_operator: The default operator for query string query (AND or
            OR)
        :param df: The field to use as default where no field prefix is given in the
            query string
        :param docvalue_fields: Array of wildcard (*) patterns. The request returns doc
            values for field names matching these patterns in the hits.fields property
            of the response.
        :param expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :param explain: If true, returns detailed information about score computation
            as part of a hit.
        :param ext: Configuration of search extensions defined by Elasticsearch plugins.
        :param fields: Array of wildcard (*) patterns. The request returns values for
            field names matching these patterns in the hits.fields property of the response.
        :param from_: Starting document offset. By default, you cannot page through more
            than 10,000 hits using the from and size parameters. To page through more
            hits, use the search_after parameter.
        :param highlight:
        :param ignore_throttled: Whether specified concrete, expanded or aliased indices
            should be ignored when throttled
        :param ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :param indices_boost: Boosts the _score of documents from specified indices.
        :param keep_alive: Specifies how long the async search needs to be available.
            Ongoing async searches and any saved search results are deleted after this
            period.
        :param keep_on_completion: If `true`, results are stored for later retrieval
            when the search completes within the `wait_for_completion_timeout`.
        :param knn: Defines the approximate kNN search to run.
        :param lenient: Specify whether format-based query failures (such as providing
            text to a numeric field) should be ignored
        :param max_concurrent_shard_requests: The number of concurrent shard requests
            per node this search executes concurrently. This value should be used to
            limit the impact of the search on the cluster in order to limit the number
            of concurrent shard requests
        :param min_compatible_shard_node:
        :param min_score: Minimum _score for matching documents. Documents with a lower
            _score are not included in the search results.
        :param pit: Limits the search to a point in time (PIT). If you provide a PIT,
            you cannot specify an <index> in the request path.
        :param post_filter:
        :param pre_filter_shard_size: The default value cannot be changed, which enforces
            the execution of a pre-filter roundtrip to retrieve statistics from each
            shard so that the ones that surely don’t hold any document matching the query
            get skipped.
        :param preference: Specify the node or shard the operation should be performed
            on (default: random)
        :param profile:
        :param q: Query in the Lucene query string syntax
        :param query: Defines the search definition using the Query DSL.
        :param request_cache: Specify if request cache should be used for this request
            or not, defaults to true
        :param rescore:
        :param rest_total_hits_as_int:
        :param routing: A comma-separated list of specific routing values
        :param runtime_mappings: Defines one or more runtime fields in the search request.
            These fields take precedence over mapped fields with the same name.
        :param script_fields: Retrieve a script evaluation (based on different fields)
            for each hit.
        :param scroll:
        :param search_after:
        :param search_type: Search operation type
        :param seq_no_primary_term: If true, returns sequence number and primary term
            of the last modification of each hit. See Optimistic concurrency control.
        :param size: The number of hits to return. By default, you cannot page through
            more than 10,000 hits using the from and size parameters. To page through
            more hits, use the search_after parameter.
        :param slice:
        :param sort:
        :param source: Indicates which source fields are returned for matching documents.
            These fields are returned in the hits._source property of the search response.
        :param source_excludes: A list of fields to exclude from the returned _source
            field
        :param source_includes: A list of fields to extract and return from the _source
            field
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
        :param suggest_mode: Specify suggest mode
        :param suggest_size: How many suggestions to return in response
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
        :param typed_keys: Specify whether aggregation and suggester names should be
            prefixed by their respective types in the response
        :param version: If true, returns document version as part of a hit.
        :param wait_for_completion_timeout: Blocks and waits until the search is completed
            up to a certain timeout. When the async search completes within the timeout,
            the response won’t include the ID as the results are not stored in the cluster.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_async_search'
        else:
            __path_parts = {}
            __path = "/_async_search"
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
        if keep_alive is not None:
            __query["keep_alive"] = keep_alive
        if keep_on_completion is not None:
            __query["keep_on_completion"] = keep_on_completion
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
        if wait_for_completion_timeout is not None:
            __query["wait_for_completion_timeout"] = wait_for_completion_timeout
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
            endpoint_id="async_search.submit",
            path_parts=__path_parts,
        )
