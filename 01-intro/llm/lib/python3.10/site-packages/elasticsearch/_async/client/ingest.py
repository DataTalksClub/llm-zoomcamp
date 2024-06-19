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


class IngestClient(NamespacedClient):

    @_rewrite_parameters()
    async def delete_pipeline(
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
        Deletes a pipeline.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-pipeline-api.html>`_

        :param id: Pipeline ID or wildcard expression of pipeline IDs used to limit the
            request. To delete all ingest pipelines in a cluster, use a value of `*`.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_ingest/pipeline/{__path_parts["id"]}'
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
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ingest.delete_pipeline",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def geo_ip_stats(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns statistical information about geoip databases

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/geoip-processor.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ingest/geoip/stats"
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
            endpoint_id="ingest.geo_ip_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_pipeline(
        self,
        *,
        id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        summary: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns a pipeline.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-pipeline-api.html>`_

        :param id: Comma-separated list of pipeline IDs to retrieve. Wildcard (`*`) expressions
            are supported. To get all ingest pipelines, omit this parameter or use `*`.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param summary: Return pipelines without their definitions (default: false)
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_ingest/pipeline/{__path_parts["id"]}'
        else:
            __path_parts = {}
            __path = "/_ingest/pipeline"
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
        if summary is not None:
            __query["summary"] = summary
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ingest.get_pipeline",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def processor_grok(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns a list of the built-in patterns.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/grok-processor.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ingest/processor/grok"
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
            endpoint_id="ingest.processor_grok",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("description", "meta", "on_failure", "processors", "version"),
        parameter_aliases={"_meta": "meta"},
    )
    async def put_pipeline(
        self,
        *,
        id: str,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        if_version: t.Optional[int] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        meta: t.Optional[t.Mapping[str, t.Any]] = None,
        on_failure: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        pretty: t.Optional[bool] = None,
        processors: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        version: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a pipeline.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ingest.html>`_

        :param id: ID of the ingest pipeline to create or update.
        :param description: Description of the ingest pipeline.
        :param if_version: Required version for optimistic concurrency control for pipeline
            updates
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param meta: Optional metadata about the ingest pipeline. May have any contents.
            This map is not automatically generated by Elasticsearch.
        :param on_failure: Processors to run immediately after a processor failure. Each
            processor supports a processor-level `on_failure` value. If a processor without
            an `on_failure` value fails, Elasticsearch uses this pipeline-level parameter
            as a fallback. The processors in this parameter run sequentially in the order
            specified. Elasticsearch will not attempt to run the pipeline's remaining
            processors.
        :param processors: Processors used to perform transformations on documents before
            indexing. Processors run sequentially in the order specified.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        :param version: Version number used by external systems to track ingest pipelines.
            This parameter is intended for external systems only. Elasticsearch does
            not use or validate pipeline version numbers.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_ingest/pipeline/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if if_version is not None:
            __query["if_version"] = if_version
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if description is not None:
                __body["description"] = description
            if meta is not None:
                __body["_meta"] = meta
            if on_failure is not None:
                __body["on_failure"] = on_failure
            if processors is not None:
                __body["processors"] = processors
            if version is not None:
                __body["version"] = version
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ingest.put_pipeline",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("docs", "pipeline"),
    )
    async def simulate(
        self,
        *,
        id: t.Optional[str] = None,
        docs: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pipeline: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        verbose: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Allows to simulate a pipeline with example documents.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/simulate-pipeline-api.html>`_

        :param id: Pipeline to test. If you don’t specify a `pipeline` in the request
            body, this parameter is required.
        :param docs: Sample documents to test in the pipeline.
        :param pipeline: Pipeline to test. If you don’t specify the `pipeline` request
            path parameter, this parameter is required. If you specify both this and
            the request path parameter, the API only uses the request path parameter.
        :param verbose: If `true`, the response includes output data for each processor
            in the executed pipeline.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_ingest/pipeline/{__path_parts["id"]}/_simulate'
        else:
            __path_parts = {}
            __path = "/_ingest/pipeline/_simulate"
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
        if verbose is not None:
            __query["verbose"] = verbose
        if not __body:
            if docs is not None:
                __body["docs"] = docs
            if pipeline is not None:
                __body["pipeline"] = pipeline
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ingest.simulate",
            path_parts=__path_parts,
        )
