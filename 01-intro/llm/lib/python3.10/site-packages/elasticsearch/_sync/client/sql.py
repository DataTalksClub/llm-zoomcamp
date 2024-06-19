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


class SqlClient(NamespacedClient):

    @_rewrite_parameters(
        body_fields=("cursor",),
    )
    def clear_cursor(
        self,
        *,
        cursor: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Clears the SQL cursor

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/clear-sql-cursor-api.html>`_

        :param cursor: Cursor to clear.
        """
        if cursor is None and body is None:
            raise ValueError("Empty value passed for parameter 'cursor'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_sql/close"
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
            if cursor is not None:
                __body["cursor"] = cursor
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="sql.clear_cursor",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_async(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an async SQL search or a stored synchronous SQL search. If the search
        is still running, the API cancels it.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-async-sql-search-api.html>`_

        :param id: Identifier for the search.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_sql/async/delete/{__path_parts["id"]}'
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
            endpoint_id="sql.delete_async",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_async(
        self,
        *,
        id: str,
        delimiter: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        format: t.Optional[str] = None,
        human: t.Optional[bool] = None,
        keep_alive: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        pretty: t.Optional[bool] = None,
        wait_for_completion_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the current status and available results for an async SQL search or stored
        synchronous SQL search

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-async-sql-search-api.html>`_

        :param id: Identifier for the search.
        :param delimiter: Separator for CSV results. The API only supports this parameter
            for CSV responses.
        :param format: Format for the response. You must specify a format using this
            parameter or the Accept HTTP header. If you specify both, the API uses this
            parameter.
        :param keep_alive: Retention period for the search and its results. Defaults
            to the `keep_alive` period for the original SQL search.
        :param wait_for_completion_timeout: Period to wait for complete results. Defaults
            to no timeout, meaning the request waits for complete search results.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_sql/async/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if delimiter is not None:
            __query["delimiter"] = delimiter
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if human is not None:
            __query["human"] = human
        if keep_alive is not None:
            __query["keep_alive"] = keep_alive
        if pretty is not None:
            __query["pretty"] = pretty
        if wait_for_completion_timeout is not None:
            __query["wait_for_completion_timeout"] = wait_for_completion_timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="sql.get_async",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_async_status(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns the current status of an async SQL search or a stored synchronous SQL
        search

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-async-sql-search-status-api.html>`_

        :param id: Identifier for the search.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_sql/async/status/{__path_parts["id"]}'
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
            endpoint_id="sql.get_async_status",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "catalog",
            "columnar",
            "cursor",
            "fetch_size",
            "field_multi_value_leniency",
            "filter",
            "index_using_frozen",
            "keep_alive",
            "keep_on_completion",
            "page_timeout",
            "params",
            "query",
            "request_timeout",
            "runtime_mappings",
            "time_zone",
            "wait_for_completion_timeout",
        ),
        ignore_deprecated_options={"params", "request_timeout"},
    )
    def query(
        self,
        *,
        catalog: t.Optional[str] = None,
        columnar: t.Optional[bool] = None,
        cursor: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        fetch_size: t.Optional[int] = None,
        field_multi_value_leniency: t.Optional[bool] = None,
        filter: t.Optional[t.Mapping[str, t.Any]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        format: t.Optional[str] = None,
        human: t.Optional[bool] = None,
        index_using_frozen: t.Optional[bool] = None,
        keep_alive: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        keep_on_completion: t.Optional[bool] = None,
        page_timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        params: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[str] = None,
        request_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        runtime_mappings: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        time_zone: t.Optional[str] = None,
        wait_for_completion_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Executes a SQL request

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/sql-search-api.html>`_

        :param catalog: Default catalog (cluster) for queries. If unspecified, the queries
            execute on the data in the local cluster only.
        :param columnar: If true, the results in a columnar fashion: one row represents
            all the values of a certain column from the current page of results.
        :param cursor: Cursor used to retrieve a set of paginated results. If you specify
            a cursor, the API only uses the `columnar` and `time_zone` request body parameters.
            It ignores other request body parameters.
        :param fetch_size: The maximum number of rows (or entries) to return in one response
        :param field_multi_value_leniency: Throw an exception when encountering multiple
            values for a field (default) or be lenient and return the first value from
            the list (without any guarantees of what that will be - typically the first
            in natural ascending order).
        :param filter: Elasticsearch query DSL for additional filtering.
        :param format: Format for the response.
        :param index_using_frozen: If true, the search can run on frozen indices. Defaults
            to false.
        :param keep_alive: Retention period for an async or saved synchronous search.
        :param keep_on_completion: If true, Elasticsearch stores synchronous searches
            if you also specify the wait_for_completion_timeout parameter. If false,
            Elasticsearch only stores async searches that don’t finish before the wait_for_completion_timeout.
        :param page_timeout: The timeout before a pagination request fails.
        :param params: Values for parameters in the query.
        :param query: SQL query to run.
        :param request_timeout: The timeout before the request fails.
        :param runtime_mappings: Defines one or more runtime fields in the search request.
            These fields take precedence over mapped fields with the same name.
        :param time_zone: ISO-8601 time zone ID for the search.
        :param wait_for_completion_timeout: Period to wait for complete results. Defaults
            to no timeout, meaning the request waits for complete search results. If
            the search doesn’t finish within this period, the search becomes async.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_sql"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if catalog is not None:
                __body["catalog"] = catalog
            if columnar is not None:
                __body["columnar"] = columnar
            if cursor is not None:
                __body["cursor"] = cursor
            if fetch_size is not None:
                __body["fetch_size"] = fetch_size
            if field_multi_value_leniency is not None:
                __body["field_multi_value_leniency"] = field_multi_value_leniency
            if filter is not None:
                __body["filter"] = filter
            if index_using_frozen is not None:
                __body["index_using_frozen"] = index_using_frozen
            if keep_alive is not None:
                __body["keep_alive"] = keep_alive
            if keep_on_completion is not None:
                __body["keep_on_completion"] = keep_on_completion
            if page_timeout is not None:
                __body["page_timeout"] = page_timeout
            if params is not None:
                __body["params"] = params
            if query is not None:
                __body["query"] = query
            if request_timeout is not None:
                __body["request_timeout"] = request_timeout
            if runtime_mappings is not None:
                __body["runtime_mappings"] = runtime_mappings
            if time_zone is not None:
                __body["time_zone"] = time_zone
            if wait_for_completion_timeout is not None:
                __body["wait_for_completion_timeout"] = wait_for_completion_timeout
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="sql.query",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("query", "fetch_size", "filter", "time_zone"),
    )
    def translate(
        self,
        *,
        query: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        fetch_size: t.Optional[int] = None,
        filter: t.Optional[t.Mapping[str, t.Any]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        time_zone: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Translates SQL into Elasticsearch queries

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/sql-translate-api.html>`_

        :param query: SQL query to run.
        :param fetch_size: The maximum number of rows (or entries) to return in one response.
        :param filter: Elasticsearch query DSL for additional filtering.
        :param time_zone: ISO-8601 time zone ID for the search.
        """
        if query is None and body is None:
            raise ValueError("Empty value passed for parameter 'query'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_sql/translate"
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
            if query is not None:
                __body["query"] = query
            if fetch_size is not None:
                __body["fetch_size"] = fetch_size
            if filter is not None:
                __body["filter"] = filter
            if time_zone is not None:
                __body["time_zone"] = time_zone
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="sql.translate",
            path_parts=__path_parts,
        )
