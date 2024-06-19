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
from .utils import _rewrite_parameters


class XPackClient(NamespacedClient):
    def __getattr__(self, attr_name: str) -> t.Any:
        return getattr(self.client, attr_name)

    # AUTO-GENERATED-API-DEFINITIONS #

    @_rewrite_parameters()
    def info(
        self,
        *,
        accept_enterprise: t.Optional[bool] = None,
        categories: t.Optional[t.Sequence[str]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves information about the installed X-Pack features.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/info-api.html>`_

        :param accept_enterprise: If this param is used it must be set to true
        :param categories: A comma-separated list of the information categories to include
            in the response. For example, `build,license,features`.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_xpack"
        __query: t.Dict[str, t.Any] = {}
        if accept_enterprise is not None:
            __query["accept_enterprise"] = accept_enterprise
        if categories is not None:
            __query["categories"] = categories
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
            endpoint_id="xpack.info",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def usage(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves usage information about the installed X-Pack features.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/usage-api.html>`_

        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_xpack/usage"
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
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="xpack.usage",
            path_parts=__path_parts,
        )
