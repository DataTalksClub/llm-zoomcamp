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

import warnings
from typing import Any, Dict, Optional, Union

from elastic_transport import AsyncTransport, Transport  # noqa: F401

# This file exists for backwards compatibility.
warnings.warn(
    "Importing from the 'elasticsearch.transport' module is deprecated. "
    "Instead import from 'elastic_transport'",
    category=DeprecationWarning,
    stacklevel=2,
)


def get_host_info(
    node_info: Dict[str, Any], host: Dict[str, Union[int, str]]
) -> Optional[Dict[str, Union[int, str]]]:
    """
    Simple callback that takes the node info from `/_cluster/nodes` and a
    parsed connection information and return the connection information. If
    `None` is returned this node will be skipped.
    Useful for filtering nodes (by proximity for example) or if additional
    information needs to be provided for the :class:`~elasticsearch.Connection`
    class. By default master only nodes are filtered out since they shouldn't
    typically be used for API operations.
    :arg node_info: node information from `/_cluster/nodes`
    :arg host: connection information (host, port) extracted from the node info
    """

    warnings.warn(
        "The 'get_host_info' function is deprecated. Instead "
        "use the 'sniff_node_callback' parameter on the client",
        category=DeprecationWarning,
        stacklevel=2,
    )

    # ignore master only nodes
    if node_info.get("roles", []) == ["master"]:
        return None
    return host
