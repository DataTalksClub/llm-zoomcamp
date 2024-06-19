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


class SearchApplicationClient(NamespacedClient):

    @_rewrite_parameters()
    def delete(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a search application.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-search-application.html>`_

        :param name: The name of the search application to delete
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_application/search_application/{__path_parts["name"]}'
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
            endpoint_id="search_application.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_behavioral_analytics(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Delete a behavioral analytics collection.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-analytics-collection.html>`_

        :param name: The name of the analytics collection to be deleted
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_application/analytics/{__path_parts["name"]}'
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
            endpoint_id="search_application.delete_behavioral_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the details about a search application.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-search-application.html>`_

        :param name: The name of the search application
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_application/search_application/{__path_parts["name"]}'
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
            endpoint_id="search_application.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_behavioral_analytics(
        self,
        *,
        name: t.Optional[t.Sequence[str]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the existing behavioral analytics collections.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/list-analytics-collection.html>`_

        :param name: A list of analytics collections to limit the returned information
        """
        __path_parts: t.Dict[str, str]
        if name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_application/analytics/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_application/analytics"
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
            endpoint_id="search_application.get_behavioral_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    def list(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        q: t.Optional[str] = None,
        size: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the existing search applications.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/list-search-applications.html>`_

        :param from_: Starting offset.
        :param q: Query in the Lucene query string syntax.
        :param size: Specifies a max number of results to get.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_application/search_application"
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
        if q is not None:
            __query["q"] = q
        if size is not None:
            __query["size"] = size
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="search_application.list",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="search_application",
    )
    def put(
        self,
        *,
        name: str,
        search_application: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        create: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a search application.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-search-application.html>`_

        :param name: The name of the search application to be created or updated.
        :param search_application:
        :param create: If `true`, this request cannot replace or update existing Search
            Applications.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        if search_application is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'search_application' and 'body', one of them should be set."
            )
        elif search_application is not None and body is not None:
            raise ValueError("Cannot set both 'search_application' and 'body'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_application/search_application/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        if create is not None:
            __query["create"] = create
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __body = search_application if search_application is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="search_application.put",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def put_behavioral_analytics(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a behavioral analytics collection.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-analytics-collection.html>`_

        :param name: The name of the analytics collection to be created or updated.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_application/analytics/{__path_parts["name"]}'
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
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="search_application.put_behavioral_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("params",),
        ignore_deprecated_options={"params"},
    )
    def search(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        params: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        typed_keys: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Perform a search against a search application

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/search-application-search.html>`_

        :param name: The name of the search application to be searched.
        :param params: Query parameters specific to this request, which will override
            any defaults specified in the template.
        :param typed_keys: Determines whether aggregation names are prefixed by their
            respective types in the response.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_application/search_application/{__path_parts["name"]}/_search'
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
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        if not __body:
            if params is not None:
                __body["params"] = params
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
            endpoint_id="search_application.search",
            path_parts=__path_parts,
        )
