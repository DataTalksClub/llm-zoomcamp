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


class DanglingIndicesClient(NamespacedClient):

    @_rewrite_parameters()
    def delete_dangling_index(
        self,
        *,
        index_uuid: str,
        accept_data_loss: bool,
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
        Deletes the specified dangling index

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-gateway-dangling-indices.html>`_

        :param index_uuid: The UUID of the dangling index
        :param accept_data_loss: Must be set to true in order to delete the dangling
            index
        :param master_timeout: Specify timeout for connection to master
        :param timeout: Explicit operation timeout
        """
        if index_uuid in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index_uuid'")
        if accept_data_loss is None:
            raise ValueError("Empty value passed for parameter 'accept_data_loss'")
        __path_parts: t.Dict[str, str] = {"index_uuid": _quote(index_uuid)}
        __path = f'/_dangling/{__path_parts["index_uuid"]}'
        __query: t.Dict[str, t.Any] = {}
        if accept_data_loss is not None:
            __query["accept_data_loss"] = accept_data_loss
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
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="dangling_indices.delete_dangling_index",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def import_dangling_index(
        self,
        *,
        index_uuid: str,
        accept_data_loss: bool,
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
        Imports the specified dangling index

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-gateway-dangling-indices.html>`_

        :param index_uuid: The UUID of the dangling index
        :param accept_data_loss: Must be set to true in order to import the dangling
            index
        :param master_timeout: Specify timeout for connection to master
        :param timeout: Explicit operation timeout
        """
        if index_uuid in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index_uuid'")
        if accept_data_loss is None:
            raise ValueError("Empty value passed for parameter 'accept_data_loss'")
        __path_parts: t.Dict[str, str] = {"index_uuid": _quote(index_uuid)}
        __path = f'/_dangling/{__path_parts["index_uuid"]}'
        __query: t.Dict[str, t.Any] = {}
        if accept_data_loss is not None:
            __query["accept_data_loss"] = accept_data_loss
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
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="dangling_indices.import_dangling_index",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def list_dangling_indices(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns all dangling indices.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/modules-gateway-dangling-indices.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_dangling"
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
            endpoint_id="dangling_indices.list_dangling_indices",
            path_parts=__path_parts,
        )
