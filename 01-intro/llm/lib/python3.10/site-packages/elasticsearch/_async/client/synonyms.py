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


class SynonymsClient(NamespacedClient):

    @_rewrite_parameters()
    async def delete_synonym(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a synonym set

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-synonyms-set.html>`_

        :param id: The id of the synonyms set to be deleted
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_synonyms/{__path_parts["id"]}'
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
            endpoint_id="synonyms.delete_synonym",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def delete_synonym_rule(
        self,
        *,
        set_id: str,
        rule_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a synonym rule in a synonym set

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-synonym-rule.html>`_

        :param set_id: The id of the synonym set to be updated
        :param rule_id: The id of the synonym rule to be deleted
        """
        if set_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'set_id'")
        if rule_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'rule_id'")
        __path_parts: t.Dict[str, str] = {
            "set_id": _quote(set_id),
            "rule_id": _quote(rule_id),
        }
        __path = f'/_synonyms/{__path_parts["set_id"]}/{__path_parts["rule_id"]}'
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
            endpoint_id="synonyms.delete_synonym_rule",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    async def get_synonym(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves a synonym set

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-synonyms-set.html>`_

        :param id: "The id of the synonyms set to be retrieved
        :param from_: Starting offset for query rules to be retrieved
        :param size: specifies a max number of query rules to retrieve
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_synonyms/{__path_parts["id"]}'
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
            endpoint_id="synonyms.get_synonym",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_synonym_rule(
        self,
        *,
        set_id: str,
        rule_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves a synonym rule from a synonym set

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-synonym-rule.html>`_

        :param set_id: The id of the synonym set to retrieve the synonym rule from
        :param rule_id: The id of the synonym rule to retrieve
        """
        if set_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'set_id'")
        if rule_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'rule_id'")
        __path_parts: t.Dict[str, str] = {
            "set_id": _quote(set_id),
            "rule_id": _quote(rule_id),
        }
        __path = f'/_synonyms/{__path_parts["set_id"]}/{__path_parts["rule_id"]}'
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
            endpoint_id="synonyms.get_synonym_rule",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    async def get_synonyms_sets(
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
        Retrieves a summary of all defined synonym sets

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/list-synonyms-sets.html>`_

        :param from_: Starting offset
        :param size: specifies a max number of results to get
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_synonyms"
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
            endpoint_id="synonyms.get_synonyms_sets",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("synonyms_set",),
    )
    async def put_synonym(
        self,
        *,
        id: str,
        synonyms_set: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a synonyms set

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-synonyms-set.html>`_

        :param id: The id of the synonyms set to be created or updated
        :param synonyms_set: The synonym set information to update
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        if synonyms_set is None and body is None:
            raise ValueError("Empty value passed for parameter 'synonyms_set'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_synonyms/{__path_parts["id"]}'
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
            if synonyms_set is not None:
                __body["synonyms_set"] = synonyms_set
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="synonyms.put_synonym",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("synonyms",),
    )
    async def put_synonym_rule(
        self,
        *,
        set_id: str,
        rule_id: str,
        synonyms: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a synonym rule in a synonym set

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-synonym-rule.html>`_

        :param set_id: The id of the synonym set to be updated with the synonym rule
        :param rule_id: The id of the synonym rule to be updated or created
        :param synonyms:
        """
        if set_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'set_id'")
        if rule_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'rule_id'")
        if synonyms is None and body is None:
            raise ValueError("Empty value passed for parameter 'synonyms'")
        __path_parts: t.Dict[str, str] = {
            "set_id": _quote(set_id),
            "rule_id": _quote(rule_id),
        }
        __path = f'/_synonyms/{__path_parts["set_id"]}/{__path_parts["rule_id"]}'
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
            if synonyms is not None:
                __body["synonyms"] = synonyms
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="synonyms.put_synonym_rule",
            path_parts=__path_parts,
        )
