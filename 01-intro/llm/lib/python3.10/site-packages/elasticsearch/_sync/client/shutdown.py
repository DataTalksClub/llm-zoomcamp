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


class ShutdownClient(NamespacedClient):

    @_rewrite_parameters()
    def delete_node(
        self,
        *,
        node_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Removes a node from the shutdown list. Designed for indirect use by ECE/ESS and
        ECK. Direct use is not supported.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/current>`_

        :param node_id: The node id of node to be removed from the shutdown state
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if node_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'node_id'")
        __path_parts: t.Dict[str, str] = {"node_id": _quote(node_id)}
        __path = f'/_nodes/{__path_parts["node_id"]}/shutdown'
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
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="shutdown.delete_node",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_node(
        self,
        *,
        node_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieve status of a node or nodes that are currently marked as shutting down.
        Designed for indirect use by ECE/ESS and ECK. Direct use is not supported.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/current>`_

        :param node_id: Which node for which to retrieve the shutdown status
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        __path_parts: t.Dict[str, str]
        if node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_nodes/{__path_parts["node_id"]}/shutdown'
        else:
            __path_parts = {}
            __path = "/_nodes/shutdown"
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
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="shutdown.get_node",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("reason", "type", "allocation_delay", "target_node_name"),
    )
    def put_node(
        self,
        *,
        node_id: str,
        reason: t.Optional[str] = None,
        type: t.Optional[
            t.Union["t.Literal['remove', 'replace', 'restart']", str]
        ] = None,
        allocation_delay: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        target_node_name: t.Optional[str] = None,
        timeout: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Adds a node to be shut down. Designed for indirect use by ECE/ESS and ECK. Direct
        use is not supported.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/current>`_

        :param node_id: The node id of node to be shut down
        :param reason: A human-readable reason that the node is being shut down. This
            field provides information for other cluster operators; it does not affect
            the shut down process.
        :param type: Valid values are restart, remove, or replace. Use restart when you
            need to temporarily shut down a node to perform an upgrade, make configuration
            changes, or perform other maintenance. Because the node is expected to rejoin
            the cluster, data is not migrated off of the node. Use remove when you need
            to permanently remove a node from the cluster. The node is not marked ready
            for shutdown until data is migrated off of the node Use replace to do a 1:1
            replacement of a node with another node. Certain allocation decisions will
            be ignored (such as disk watermarks) in the interest of true replacement
            of the source node with the target node. During a replace-type shutdown,
            rollover and index creation may result in unassigned shards, and shrink may
            fail until the replacement is complete.
        :param allocation_delay: Only valid if type is restart. Controls how long Elasticsearch
            will wait for the node to restart and join the cluster before reassigning
            its shards to other nodes. This works the same as delaying allocation with
            the index.unassigned.node_left.delayed_timeout setting. If you specify both
            a restart allocation delay and an index-level allocation delay, the longer
            of the two is used.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param target_node_name: Only valid if type is replace. Specifies the name of
            the node that is replacing the node being shut down. Shards from the shut
            down node are only allowed to be allocated to the target node, and no other
            data will be allocated to the target node. During relocation of data certain
            allocation rules are ignored, such as disk watermarks or user attribute filtering
            rules.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if node_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'node_id'")
        if reason is None and body is None:
            raise ValueError("Empty value passed for parameter 'reason'")
        if type is None and body is None:
            raise ValueError("Empty value passed for parameter 'type'")
        __path_parts: t.Dict[str, str] = {"node_id": _quote(node_id)}
        __path = f'/_nodes/{__path_parts["node_id"]}/shutdown'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
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
        if not __body:
            if reason is not None:
                __body["reason"] = reason
            if type is not None:
                __body["type"] = type
            if allocation_delay is not None:
                __body["allocation_delay"] = allocation_delay
            if target_node_name is not None:
                __body["target_node_name"] = target_node_name
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="shutdown.put_node",
            path_parts=__path_parts,
        )
