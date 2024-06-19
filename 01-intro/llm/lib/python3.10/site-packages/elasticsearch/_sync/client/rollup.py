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


class RollupClient(NamespacedClient):

    @_rewrite_parameters()
    def delete_job(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an existing rollup job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-delete-job.html>`_

        :param id: Identifier for the job.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_rollup/job/{__path_parts["id"]}'
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
            endpoint_id="rollup.delete_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_jobs(
        self,
        *,
        id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves the configuration, stats, and status of rollup jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-get-job.html>`_

        :param id: Identifier for the rollup job. If it is `_all` or omitted, the API
            returns all rollup jobs.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_rollup/job/{__path_parts["id"]}'
        else:
            __path_parts = {}
            __path = "/_rollup/job"
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
            endpoint_id="rollup.get_jobs",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_rollup_caps(
        self,
        *,
        id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the capabilities of any rollup jobs that have been configured for a specific
        index or index pattern.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-get-rollup-caps.html>`_

        :param id: Index, indices or index-pattern to return rollup capabilities for.
            `_all` may be used to fetch rollup capabilities from all jobs.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_rollup/data/{__path_parts["id"]}'
        else:
            __path_parts = {}
            __path = "/_rollup/data"
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
            endpoint_id="rollup.get_rollup_caps",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_rollup_index_caps(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the rollup capabilities of all jobs inside of a rollup index (e.g. the
        index where rollup data is stored).

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-get-rollup-index-caps.html>`_

        :param index: Data stream or index to check for rollup capabilities. Wildcard
            (`*`) expressions are supported.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_rollup/data'
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
            endpoint_id="rollup.get_rollup_index_caps",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "cron",
            "groups",
            "index_pattern",
            "page_size",
            "rollup_index",
            "headers",
            "metrics",
            "timeout",
        ),
        ignore_deprecated_options={"headers"},
    )
    def put_job(
        self,
        *,
        id: str,
        cron: t.Optional[str] = None,
        groups: t.Optional[t.Mapping[str, t.Any]] = None,
        index_pattern: t.Optional[str] = None,
        page_size: t.Optional[int] = None,
        rollup_index: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        headers: t.Optional[t.Mapping[str, t.Union[str, t.Sequence[str]]]] = None,
        human: t.Optional[bool] = None,
        metrics: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a rollup job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-put-job.html>`_

        :param id: Identifier for the rollup job. This can be any alphanumeric string
            and uniquely identifies the data that is associated with the rollup job.
            The ID is persistent; it is stored with the rolled up data. If you create
            a job, let it run for a while, then delete the job, the data that the job
            rolled up is still be associated with this job ID. You cannot create a new
            job with the same ID since that could lead to problems with mismatched job
            configurations.
        :param cron: A cron string which defines the intervals when the rollup job should
            be executed. When the interval triggers, the indexer attempts to rollup the
            data in the index pattern. The cron pattern is unrelated to the time interval
            of the data being rolled up. For example, you may wish to create hourly rollups
            of your document but to only run the indexer on a daily basis at midnight,
            as defined by the cron. The cron pattern is defined just like a Watcher cron
            schedule.
        :param groups: Defines the grouping fields and aggregations that are defined
            for this rollup job. These fields will then be available later for aggregating
            into buckets. These aggs and fields can be used in any combination. Think
            of the groups configuration as defining a set of tools that can later be
            used in aggregations to partition the data. Unlike raw data, we have to think
            ahead to which fields and aggregations might be used. Rollups provide enough
            flexibility that you simply need to determine which fields are needed, not
            in what order they are needed.
        :param index_pattern: The index or index pattern to roll up. Supports wildcard-style
            patterns (`logstash-*`). The job attempts to rollup the entire index or index-pattern.
        :param page_size: The number of bucket results that are processed on each iteration
            of the rollup indexer. A larger value tends to execute faster, but requires
            more memory during processing. This value has no effect on how the data is
            rolled up; it is merely used for tweaking the speed or memory cost of the
            indexer.
        :param rollup_index: The index that contains the rollup results. The index can
            be shared with other rollup jobs. The data is stored so that it doesn’t interfere
            with unrelated jobs.
        :param headers:
        :param metrics: Defines the metrics to collect for each grouping tuple. By default,
            only the doc_counts are collected for each group. To make rollup useful,
            you will often add metrics like averages, mins, maxes, etc. Metrics are defined
            on a per-field basis and for each field you configure which metric should
            be collected.
        :param timeout: Time to wait for the request to complete.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        if cron is None and body is None:
            raise ValueError("Empty value passed for parameter 'cron'")
        if groups is None and body is None:
            raise ValueError("Empty value passed for parameter 'groups'")
        if index_pattern is None and body is None:
            raise ValueError("Empty value passed for parameter 'index_pattern'")
        if page_size is None and body is None:
            raise ValueError("Empty value passed for parameter 'page_size'")
        if rollup_index is None and body is None:
            raise ValueError("Empty value passed for parameter 'rollup_index'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_rollup/job/{__path_parts["id"]}'
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
            if cron is not None:
                __body["cron"] = cron
            if groups is not None:
                __body["groups"] = groups
            if index_pattern is not None:
                __body["index_pattern"] = index_pattern
            if page_size is not None:
                __body["page_size"] = page_size
            if rollup_index is not None:
                __body["rollup_index"] = rollup_index
            if headers is not None:
                __body["headers"] = headers
            if metrics is not None:
                __body["metrics"] = metrics
            if timeout is not None:
                __body["timeout"] = timeout
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="rollup.put_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("aggregations", "aggs", "query", "size"),
    )
    def rollup_search(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        aggregations: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        aggs: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        rest_total_hits_as_int: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        typed_keys: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Enables searching rolled-up data using the standard query DSL.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-search.html>`_

        :param index: Enables searching rolled-up data using the standard Query DSL.
        :param aggregations: Specifies aggregations.
        :param aggs: Specifies aggregations.
        :param query: Specifies a DSL query.
        :param rest_total_hits_as_int: Indicates whether hits.total should be rendered
            as an integer or an object in the rest search response
        :param size: Must be zero if set, as rollups work on pre-aggregated data.
        :param typed_keys: Specify whether aggregation and suggester names should be
            prefixed by their respective types in the response
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_rollup_search'
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
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        if not __body:
            if aggregations is not None:
                __body["aggregations"] = aggregations
            if aggs is not None:
                __body["aggs"] = aggs
            if query is not None:
                __body["query"] = query
            if size is not None:
                __body["size"] = size
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="rollup.rollup_search",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def start_job(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Starts an existing, stopped rollup job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-start-job.html>`_

        :param id: Identifier for the rollup job.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_rollup/job/{__path_parts["id"]}/_start'
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
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="rollup.start_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def stop_job(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        wait_for_completion: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Stops an existing, started rollup job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/rollup-stop-job.html>`_

        :param id: Identifier for the rollup job.
        :param timeout: If `wait_for_completion` is `true`, the API blocks for (at maximum)
            the specified duration while waiting for the job to stop. If more than `timeout`
            time has passed, the API throws a timeout exception.
        :param wait_for_completion: If set to `true`, causes the API to block until the
            indexer state completely stops. If set to `false`, the API returns immediately
            and the indexer is stopped asynchronously in the background.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_rollup/job/{__path_parts["id"]}/_stop'
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
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="rollup.stop_job",
            path_parts=__path_parts,
        )
