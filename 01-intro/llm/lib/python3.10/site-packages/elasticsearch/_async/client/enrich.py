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


class EnrichClient(NamespacedClient):

    @_rewrite_parameters()
    async def delete_policy(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an existing enrich policy and its enrich index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-enrich-policy-api.html>`_

        :param name: Enrich policy to delete.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_enrich/policy/{__path_parts["name"]}'
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
            endpoint_id="enrich.delete_policy",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def execute_policy(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        wait_for_completion: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates the enrich index for an existing enrich policy.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/execute-enrich-policy-api.html>`_

        :param name: Enrich policy to execute.
        :param wait_for_completion: If `true`, the request blocks other enrich policy
            execution requests until complete.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_enrich/policy/{__path_parts["name"]}/_execute'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="enrich.execute_policy",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_policy(
        self,
        *,
        name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Gets information about an enrich policy.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-enrich-policy-api.html>`_

        :param name: Comma-separated list of enrich policy names used to limit the request.
            To return information for all enrich policies, omit this parameter.
        """
        __path_parts: t.Dict[str, str]
        if name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_enrich/policy/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_enrich/policy"
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
            endpoint_id="enrich.get_policy",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("geo_match", "match", "range"),
    )
    async def put_policy(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        geo_match: t.Optional[t.Mapping[str, t.Any]] = None,
        human: t.Optional[bool] = None,
        match: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        range: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a new enrich policy.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-enrich-policy-api.html>`_

        :param name: Name of the enrich policy to create or update.
        :param geo_match: Matches enrich data to incoming documents based on a `geo_shape`
            query.
        :param match: Matches enrich data to incoming documents based on a `term` query.
        :param range: Matches a number, date, or IP address in incoming documents to
            a range in the enrich index based on a `term` query.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_enrich/policy/{__path_parts["name"]}'
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
            if geo_match is not None:
                __body["geo_match"] = geo_match
            if match is not None:
                __body["match"] = match
            if range is not None:
                __body["range"] = range
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="enrich.put_policy",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def stats(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Gets enrich coordinator statistics and information about enrich policies that
        are currently executing.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/enrich-stats-api.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_enrich/_stats"
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
            endpoint_id="enrich.stats",
            path_parts=__path_parts,
        )
