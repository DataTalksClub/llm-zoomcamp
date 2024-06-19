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


class QueryRulesetClient(NamespacedClient):

    @_rewrite_parameters()
    async def delete(
        self,
        *,
        ruleset_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a query ruleset.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-query-ruleset.html>`_

        :param ruleset_id: The unique identifier of the query ruleset to delete
        """
        if ruleset_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'ruleset_id'")
        __path_parts: t.Dict[str, str] = {"ruleset_id": _quote(ruleset_id)}
        __path = f'/_query_rules/{__path_parts["ruleset_id"]}'
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
            endpoint_id="query_ruleset.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get(
        self,
        *,
        ruleset_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the details about a query ruleset.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-query-ruleset.html>`_

        :param ruleset_id: The unique identifier of the query ruleset
        """
        if ruleset_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'ruleset_id'")
        __path_parts: t.Dict[str, str] = {"ruleset_id": _quote(ruleset_id)}
        __path = f'/_query_rules/{__path_parts["ruleset_id"]}'
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
            endpoint_id="query_ruleset.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    async def list(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Lists query rulesets.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/list-query-rulesets.html>`_

        :param from_: Starting offset (default: 0)
        :param size: specifies a max number of results to get
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_query_rules"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="query_ruleset.list",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("rules",),
    )
    async def put(
        self,
        *,
        ruleset_id: str,
        rules: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a query ruleset.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-query-ruleset.html>`_

        :param ruleset_id: The unique identifier of the query ruleset to be created or
            updated
        :param rules:
        """
        if ruleset_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'ruleset_id'")
        if rules is None and body is None:
            raise ValueError("Empty value passed for parameter 'rules'")
        __path_parts: t.Dict[str, str] = {"ruleset_id": _quote(ruleset_id)}
        __path = f'/_query_rules/{__path_parts["ruleset_id"]}'
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
            if rules is not None:
                __body["rules"] = rules
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="query_ruleset.put",
            path_parts=__path_parts,
        )
