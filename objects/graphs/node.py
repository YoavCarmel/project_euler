from __future__ import annotations
from typing import NamedTuple, List


class Connection(NamedTuple):
    other: Node
    length: float


class Node(NamedTuple):
    node_id: int
    value: int
    connections: List[Connection]

    def add_child(self, child: Node, length: float = 1):
        self.connections.append(Connection(child, length))

    def __eq__(self, other: Node):
        return self.node_id == other.node_id

    def __hash__(self):
        return hash(self.node_id)
