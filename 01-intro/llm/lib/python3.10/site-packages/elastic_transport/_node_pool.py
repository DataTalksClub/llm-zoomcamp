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

import logging
import random
import threading
import time
from collections import defaultdict
from queue import Empty, PriorityQueue
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
    overload,
)

from ._compat import Lock, ordered_dict
from ._models import NodeConfig
from ._node import BaseNode

if TYPE_CHECKING:
    from typing import Literal

_logger = logging.getLogger("elastic_transport.node_pool")


class NodeSelector:
    """
    Simple class used to select a node from a list of currently live
    node instances. In init time it is passed a dictionary containing all
    the nodes options which it can then use during the selection
    process. When the ``select()`` method is called it is given a list of
    *currently* live nodes to choose from.

    The selector is initialized with the list of seed nodes that the
    NodePool was initialized with. This list of seed nodes can be used
    to make decisions within ``select()``

    Example of where this would be useful is a zone-aware selector that would
    only select connections from it's own zones and only fall back to other
    connections where there would be none in its zones.
    """

    def __init__(self, node_configs: List[NodeConfig]):
        """
        :arg node_configs: List of NodeConfig instances
        """
        self.node_configs = node_configs

    def select(self, nodes: Sequence[BaseNode]) -> BaseNode:  # pragma: nocover
        """
        Select a nodes from the given list.

        :arg nodes: list of live nodes to choose from
        """
        raise NotImplementedError()


class RandomSelector(NodeSelector):
    """Randomly select a node"""

    def select(self, nodes: Sequence[BaseNode]) -> BaseNode:
        return random.choice(nodes)


class RoundRobinSelector(NodeSelector):
    """Select a node using round-robin"""

    def __init__(self, node_configs: List[NodeConfig]):
        super().__init__(node_configs)
        self._thread_local = threading.local()

    def select(self, nodes: Sequence[BaseNode]) -> BaseNode:
        self._thread_local.rr = (getattr(self._thread_local, "rr", -1) + 1) % len(nodes)
        return nodes[self._thread_local.rr]


_SELECTOR_CLASS_NAMES: Dict[str, Type[NodeSelector]] = {
    "round_robin": RoundRobinSelector,
    "random": RandomSelector,
}


class NodePool:
    """
    Container holding the :class:`~elastic_transport.BaseNode` instances,
    managing the selection process (via a
    :class:`~elastic_transport.NodeSelector`) and dead connections.

    It's only interactions are with the :class:`~elastic_transport.Transport` class
    that drives all the actions within ``NodePool``.

    Initially nodes are stored on the class as a list and, along with the
    connection options, get passed to the ``NodeSelector`` instance for
    future reference.

    Upon each request the ``Transport`` will ask for a ``BaseNode`` via the
    ``get_node`` method. If the connection fails (it's `perform_request`
    raises a `ConnectionError`) it will be marked as dead (via `mark_dead`) and
    put on a timeout (if it fails N times in a row the timeout is exponentially
    longer - the formula is `default_timeout * 2 ** (fail_count - 1)`). When
    the timeout is over the connection will be resurrected and returned to the
    live pool. A connection that has been previously marked as dead and
    succeeds will be marked as live (its fail count will be deleted).
    """

    def __init__(
        self,
        node_configs: List[NodeConfig],
        node_class: Type[BaseNode],
        dead_node_backoff_factor: float = 1.0,
        max_dead_node_backoff: float = 30.0,
        node_selector_class: Union[str, Type[NodeSelector]] = RoundRobinSelector,
        randomize_nodes: bool = True,
    ):
        """
        :arg node_configs: List of initial NodeConfigs to use
        :arg node_class: Type to use when creating nodes
        :arg dead_node_backoff_factor: Number of seconds used as a factor in
            calculating the amount of "backoff" time we should give a node
            after an unsuccessful request. The formula is calculated as
            follows where N is the number of consecutive failures:
            ``min(dead_backoff_factor * (2 ** (N - 1)), max_dead_backoff)``
        :arg max_dead_node_backoff: Maximum number of seconds to wait
            when calculating the "backoff" time for a dead node.
        :arg node_selector_class: :class:`~elastic_transport.NodeSelector`
            subclass to use if more than one connection is live
        :arg randomize_nodes: shuffle the list of nodes upon instantiation
            to avoid dog-piling effect across processes
        """
        if not node_configs:
            raise ValueError("Must specify at least one NodeConfig")
        node_configs = list(
            node_configs
        )  # Make a copy so we don't have side-effects outside.
        if any(not isinstance(node_config, NodeConfig) for node_config in node_configs):
            raise TypeError("NodePool must be passed a list of NodeConfig instances")

        if isinstance(node_selector_class, str):
            if node_selector_class not in _SELECTOR_CLASS_NAMES:
                raise ValueError(
                    "Unknown option for selector_class: '%s'. "
                    "Available options are: '%s'"
                    % (
                        node_selector_class,
                        "', '".join(sorted(_SELECTOR_CLASS_NAMES.keys())),
                    )
                )
            node_selector_class = _SELECTOR_CLASS_NAMES[node_selector_class]

        if randomize_nodes:
            # randomize the list of nodes to avoid hammering the same node
            # if a large set of clients are created all at once.
            random.shuffle(node_configs)

        # Initial set of nodes that the NodePool was initialized with.
        # This set of nodes can never be removed.
        self._seed_nodes: Tuple[NodeConfig, ...] = tuple(set(node_configs))
        if len(self._seed_nodes) != len(node_configs):
            raise ValueError("Cannot use duplicate NodeConfigs within a NodePool")

        self._node_class = node_class
        self._node_selector = node_selector_class(node_configs)

        # Maintain insert order
        self._all_nodes: Dict[NodeConfig, BaseNode] = ordered_dict()
        for node_config in node_configs:
            self._all_nodes[node_config] = self._node_class(node_config)

        # Lock that is used to protect writing to 'all_nodes'
        self._all_nodes_write_lock = Lock()
        # Flag which tells NodePool.get() that there's only one node
        # which allows for optimizations. Setting this flag is also
        # protected by the above write lock.
        self._all_nodes_len_1 = len(self._all_nodes) == 1

        # Collection of currently-alive nodes. This is an ordered
        # dict so round-robin actually works.
        self._alive_nodes: Dict[NodeConfig, BaseNode] = ordered_dict(self._all_nodes)

        # PriorityQueue for thread safety and ease of timeout management
        self._dead_nodes: PriorityQueue[Tuple[float, BaseNode]] = PriorityQueue()
        self._dead_consecutive_failures: Dict[NodeConfig, int] = defaultdict(lambda: 0)

        # Nodes that have been marked as 'removed' to be thread-safe.
        self._removed_nodes: Set[NodeConfig] = set()

        # default timeout after which to try resurrecting a connection
        self._dead_node_backoff_factor = dead_node_backoff_factor
        self._max_dead_node_backoff = max_dead_node_backoff

    @property
    def node_class(self) -> Type[BaseNode]:
        return self._node_class

    @property
    def node_selector(self) -> NodeSelector:
        return self._node_selector

    @property
    def dead_node_backoff_factor(self) -> float:
        return self._dead_node_backoff_factor

    @property
    def max_dead_node_backoff(self) -> float:
        return self._max_dead_node_backoff

    def mark_dead(self, node: BaseNode, _now: Optional[float] = None) -> None:
        """
        Mark the node as dead (failed). Remove it from the live pool and put it on a timeout.

        :arg node: The failed node.
        """
        now: float = _now if _now is not None else time.time()
        try:
            del self._alive_nodes[node.config]
        except KeyError:
            pass
        consecutive_failures = self._dead_consecutive_failures[node.config] + 1
        self._dead_consecutive_failures[node.config] = consecutive_failures
        try:
            timeout = min(
                self._dead_node_backoff_factor * (2 ** (consecutive_failures - 1)),
                self._max_dead_node_backoff,
            )
        except OverflowError:
            timeout = self._max_dead_node_backoff
        self._dead_nodes.put((now + timeout, node))
        _logger.warning(
            "Node %r has failed for %i times in a row, putting on %i second timeout",
            node,
            consecutive_failures,
            timeout,
        )

    def mark_live(self, node: BaseNode) -> None:
        """
        Mark node as healthy after a resurrection. Resets the fail counter for the node.

        :arg node: The ``BaseNode`` instance to mark as alive.
        """
        try:
            del self._dead_consecutive_failures[node.config]
        except KeyError:
            # race condition, safe to ignore
            pass
        else:
            self._alive_nodes.setdefault(node.config, node)
            _logger.warning(
                "Node %r has been marked alive after a successful request",
                node,
            )

    @overload
    def resurrect(self, force: "Literal[True]" = ...) -> BaseNode: ...

    @overload
    def resurrect(self, force: "Literal[False]" = ...) -> Optional[BaseNode]: ...

    def resurrect(self, force: bool = False) -> Optional[BaseNode]:
        """
        Attempt to resurrect a node from the dead queue. It will try to
        locate one (not all) eligible (it's timeout is over) node to
        return to the live pool. Any resurrected node is also returned.

        :arg force: resurrect a node even if there is none eligible (used
            when we have no live nodes). If force is 'True'' resurrect
            always returns a node.
        """
        node: Optional[BaseNode]
        mark_node_alive_after: float = 0.0
        try:
            # Try to resurrect a dead node if any.
            mark_node_alive_after, node = self._dead_nodes.get(block=False)
        except Empty:  # No dead nodes.
            if force:
                # If we're being forced to return a node we randomly
                # pick between alive and dead nodes.
                return random.choice(list(self._all_nodes.values()))
            node = None

        if node is not None and not force and mark_node_alive_after > time.time():
            # return it back if not eligible and not forced
            self._dead_nodes.put((mark_node_alive_after, node))
            node = None

        # either we were forced or the node is eligible to be retried
        if node is not None:
            self._alive_nodes[node.config] = node
            _logger.info("Resurrected node %r (force=%s)", node, force)
        return node

    def add(self, node_config: NodeConfig) -> None:
        try:  # If the node was previously removed we mark it as "in the pool"
            self._removed_nodes.remove(node_config)
        except KeyError:
            pass

        with self._all_nodes_write_lock:
            # We don't error when trying to add a duplicate node
            # to the pool because threading+sniffing can call
            # .add() on the same NodeConfig.
            if node_config not in self._all_nodes:
                node = self._node_class(node_config)
                self._all_nodes[node.config] = node

                # Update the flag to disable optimizations. Also ensures that
                # .resurrect() starts getting called so our added node makes
                # it way into the alive nodes.
                self._all_nodes_len_1 = False

                # Start the node as dead because 'dead_nodes' is thread-safe.
                # The node will be resurrected on the next call to .get()
                self._dead_consecutive_failures[node.config] = 0
                self._dead_nodes.put((time.time(), node))

    def remove(self, node_config: NodeConfig) -> None:
        # Can't mark a seed node as removed.
        if node_config not in self._seed_nodes:
            self._removed_nodes.add(node_config)

    def get(self) -> BaseNode:
        """
        Return a node from the pool using the ``NodeSelector`` instance.

        It tries to resurrect eligible nodes, forces a resurrection when
        no nodes are available and passes the list of live nodes to
        the selector instance to choose from.
        """
        # Even with the optimization below we want to participate in the
        # dead/alive cycle in case more nodes join after sniffing, for example.
        self.resurrect()

        # Flag that short-circuits the extra logic if we have only one node.
        # The only way this flag can be set to 'True' is if there were only
        # one node defined within 'seed_nodes' so we know this good to do.
        if self._all_nodes_len_1:
            return self._all_nodes[self._seed_nodes[0]]

        # Filter nodes in 'alive_nodes' to ones not marked as removed.
        nodes = [
            node
            for node_config, node in self._alive_nodes.items()
            if node_config not in self._removed_nodes
        ]

        # No live nodes, resurrect one by force and return it
        if not nodes:
            return self.resurrect(force=True)

        # Only call selector if we have a choice to make
        if len(nodes) > 1:
            return self._node_selector.select(nodes)
        return nodes[0]

    def all(self) -> List[BaseNode]:
        return list(self._all_nodes.values())

    def __repr__(self) -> str:
        return "<NodePool>"

    def __len__(self) -> int:
        return len(self._all_nodes)
