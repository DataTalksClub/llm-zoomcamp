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


class AutoscalingClient(NamespacedClient):

    @_rewrite_parameters()
    async def delete_autoscaling_policy(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an autoscaling policy. Designed for indirect use by ECE/ESS and ECK.
        Direct use is not supported.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/autoscaling-delete-autoscaling-policy.html>`_

        :param name: the name of the autoscaling policy
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_autoscaling/policy/{__path_parts["name"]}'
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
            endpoint_id="autoscaling.delete_autoscaling_policy",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_autoscaling_capacity(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Gets the current autoscaling capacity based on the configured autoscaling policy.
        Designed for indirect use by ECE/ESS and ECK. Direct use is not supported.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/autoscaling-get-autoscaling-capacity.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_autoscaling/capacity"
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
            endpoint_id="autoscaling.get_autoscaling_capacity",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_autoscaling_policy(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves an autoscaling policy. Designed for indirect use by ECE/ESS and ECK.
        Direct use is not supported.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/autoscaling-get-autoscaling-capacity.html>`_

        :param name: the name of the autoscaling policy
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_autoscaling/policy/{__path_parts["name"]}'
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
            endpoint_id="autoscaling.get_autoscaling_policy",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="policy",
    )
    async def put_autoscaling_policy(
        self,
        *,
        name: str,
        policy: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a new autoscaling policy. Designed for indirect use by ECE/ESS and ECK.
        Direct use is not supported.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/autoscaling-put-autoscaling-policy.html>`_

        :param name: the name of the autoscaling policy
        :param policy:
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        if policy is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'policy' and 'body', one of them should be set."
            )
        elif policy is not None and body is not None:
            raise ValueError("Cannot set both 'policy' and 'body'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_autoscaling/policy/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __body = policy if policy is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="autoscaling.put_autoscaling_policy",
            path_parts=__path_parts,
        )
