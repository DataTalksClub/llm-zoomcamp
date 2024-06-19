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


class MonitoringClient(NamespacedClient):

    @_rewrite_parameters(
        body_name="operations",
    )
    def bulk(
        self,
        *,
        interval: t.Union["t.Literal[-1]", "t.Literal[0]", str],
        operations: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        system_api_version: str,
        system_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Used by the monitoring features to send monitoring data.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/monitor-elasticsearch-cluster.html>`_

        :param interval: Collection interval (e.g., '10s' or '10000ms') of the payload
        :param operations:
        :param system_api_version:
        :param system_id: Identifier of the monitored system
        """
        if interval is None:
            raise ValueError("Empty value passed for parameter 'interval'")
        if operations is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'operations' and 'body', one of them should be set."
            )
        elif operations is not None and body is not None:
            raise ValueError("Cannot set both 'operations' and 'body'")
        if system_api_version is None:
            raise ValueError("Empty value passed for parameter 'system_api_version'")
        if system_id is None:
            raise ValueError("Empty value passed for parameter 'system_id'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_monitoring/bulk"
        __query: t.Dict[str, t.Any] = {}
        if interval is not None:
            __query["interval"] = interval
        if system_api_version is not None:
            __query["system_api_version"] = system_api_version
        if system_id is not None:
            __query["system_id"] = system_id
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __body = operations if operations is not None else body
        __headers = {
            "accept": "application/json",
            "content-type": "application/x-ndjson",
        }
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="monitoring.bulk",
            path_parts=__path_parts,
        )
