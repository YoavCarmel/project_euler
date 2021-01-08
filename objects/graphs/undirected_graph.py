from typing import Union

from objects.graphs.graph import Graph


class UndirectedGraph(Graph):
    def add_connection(self, n1: int, n2: int, length: float = 1):
        self.get_node(n1).add_child(self._nodes[n2], length)
        self.get_node(n2).add_child(self._nodes[n1], length)

    def weight(self) -> Union[float, int]:
        return self.connections_lengths_sum() // 2  # each connection was counted twice
