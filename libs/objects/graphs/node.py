from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(init=True, repr=True)
class Connection:
    other: Node
    length: float


class Node:
    def __init__(self, node_id: int, value: int):
        self.node_id: int = node_id
        self.__value: int = value
        self.__connections: List[Connection] = list()

    def add_child(self, child: Node, length: float = 1):
        self.__connections.append(Connection(child, length))

    def get_value(self) -> int:
        return self.__value

    def get_connections(self) -> List[Connection]:
        return self.__connections

    def clear_connections(self):
        """
        empty connections list
        """
        self.__connections = list()

    def __eq__(self, other: Node):
        return self.node_id == other.node_id

    def __hash__(self):
        return hash(self.node_id)

    def __repr__(self):
        s = f"{self.node_id}, value: {self.__value}, connections: [ "
        for con in self.__connections:
            s += f"({con.__repr__()}) "
        s += "]"
        return s
