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


class LogstashClient(NamespacedClient):

    @_rewrite_parameters()
    def delete_pipeline(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes Logstash Pipelines used by Central Management

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/logstash-api-delete-pipeline.html>`_

        :param id: Identifier for the pipeline.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_logstash/pipeline/{__path_parts["id"]}'
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
            endpoint_id="logstash.delete_pipeline",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_pipeline(
        self,
        *,
        id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves Logstash Pipelines used by Central Management

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/logstash-api-get-pipeline.html>`_

        :param id: Comma-separated list of pipeline identifiers.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_logstash/pipeline/{__path_parts["id"]}'
        else:
            __path_parts = {}
            __path = "/_logstash/pipeline"
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
            endpoint_id="logstash.get_pipeline",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="pipeline",
    )
    def put_pipeline(
        self,
        *,
        id: str,
        pipeline: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Adds and updates Logstash Pipelines used for Central Management

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/logstash-api-put-pipeline.html>`_

        :param id: Identifier for the pipeline.
        :param pipeline:
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        if pipeline is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'pipeline' and 'body', one of them should be set."
            )
        elif pipeline is not None and body is not None:
            raise ValueError("Cannot set both 'pipeline' and 'body'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_logstash/pipeline/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __body = pipeline if pipeline is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="logstash.put_pipeline",
            path_parts=__path_parts,
        )
