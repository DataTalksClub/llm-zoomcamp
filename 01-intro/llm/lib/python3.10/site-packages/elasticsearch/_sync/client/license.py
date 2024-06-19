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


class LicenseClient(NamespacedClient):

    @_rewrite_parameters()
    def delete(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes licensing information for the cluster

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-license.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license"
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
            endpoint_id="license.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get(
        self,
        *,
        accept_enterprise: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves licensing information for the cluster

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-license.html>`_

        :param accept_enterprise: If `true`, this parameter returns enterprise for Enterprise
            license types. If `false`, this parameter returns platinum for both platinum
            and enterprise license types. This behavior is maintained for backwards compatibility.
            This parameter is deprecated and will always be set to true in 8.x.
        :param local: Specifies whether to retrieve local information. The default value
            is `false`, which means the information is retrieved from the master node.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license"
        __query: t.Dict[str, t.Any] = {}
        if accept_enterprise is not None:
            __query["accept_enterprise"] = accept_enterprise
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="license.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_basic_status(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves information about the status of the basic license.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-basic-status.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license/basic_status"
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
            endpoint_id="license.get_basic_status",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_trial_status(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves information about the status of the trial license.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-trial-status.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license/trial_status"
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
            endpoint_id="license.get_trial_status",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("license", "licenses"),
    )
    def post(
        self,
        *,
        acknowledge: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        license: t.Optional[t.Mapping[str, t.Any]] = None,
        licenses: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates the license for the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/update-license.html>`_

        :param acknowledge: Specifies whether you acknowledge the license changes.
        :param license:
        :param licenses: A sequence of one or more JSON documents containing the license
            information.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if acknowledge is not None:
            __query["acknowledge"] = acknowledge
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if license is not None:
                __body["license"] = license
            if licenses is not None:
                __body["licenses"] = licenses
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="license.post",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def post_start_basic(
        self,
        *,
        acknowledge: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Starts an indefinite basic license.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/start-basic.html>`_

        :param acknowledge: whether the user has acknowledged acknowledge messages (default:
            false)
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license/start_basic"
        __query: t.Dict[str, t.Any] = {}
        if acknowledge is not None:
            __query["acknowledge"] = acknowledge
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
            endpoint_id="license.post_start_basic",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def post_start_trial(
        self,
        *,
        acknowledge: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        type_query_string: t.Optional[str] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        starts a limited time trial license.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/start-trial.html>`_

        :param acknowledge: whether the user has acknowledged acknowledge messages (default:
            false)
        :param type_query_string:
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license/start_trial"
        __query: t.Dict[str, t.Any] = {}
        if acknowledge is not None:
            __query["acknowledge"] = acknowledge
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if type_query_string is not None:
            __query["type_query_string"] = type_query_string
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="license.post_start_trial",
            path_parts=__path_parts,
        )
