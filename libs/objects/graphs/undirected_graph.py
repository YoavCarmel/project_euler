from __future__ import annotations

import heapq
import random
from math import inf
from typing import Union, List, Set, Dict, Optional

from libs.objects.graphs.graph import Graph
from libs.objects.graphs.node import Node


class UndirectedGraph(Graph):
    def add_connection(self, n1: int, n2: int, length: float = 1):
        if (n2, length) in {(con.other.node_id, con.length) for con in self.get_node(n1).get_connections()}:
            return
        self.get_node(n1).add_child(self._nodes[n2], length)
        self.get_node(n2).add_child(self._nodes[n1], length)

    def weight(self) -> Union[float, int]:
        return self.connections_lengths_sum() // 2  # each connection was counted twice

    def mst(self) -> UndirectedGraph:
        """
        calculate the minimum spanning tree of self
        :return: the graph with only edges found in the algorithm
        """

        class MSTNode:
            def __init__(self, self_node: Node, con_len: float):
                self.node: Node = self_node
                self.con_len: float = con_len
                self.parent: Optional[Node] = None

            def __lt__(self, other: MSTNode):
                return self.con_len < other.con_len

        # first, create a copy of self without connections.
        mst_result = self.__copy__()
        for node in mst_result.get_all_nodes():
            node.clear_connections()
        # start the algorithm: choose an arbitrary node and add to the heap
        node_to_mst: Dict[int, MSTNode] = {n.node_id: MSTNode(n, inf) for n in self.get_all_nodes()}
        heap: List[MSTNode] = list(node_to_mst.values())
        start = random.choice(heap)
        start.con_len = 0
        heapq.heapify(heap)
        while len(heap) != 0:
            curr: MSTNode = heapq.heappop(heap)
            if curr.parent is not None:
                mst_result.add_connection(curr.parent.node_id, curr.node.node_id, curr.con_len)
            in_heap: Set[int] = {mstn.node.node_id for mstn in heap}
            for connection in curr.node.get_connections():
                if connection.other.node_id in in_heap and \
                        connection.length < node_to_mst[connection.other.node_id].con_len:
                    node_to_mst[connection.other.node_id].con_len = connection.length
                    node_to_mst[connection.other.node_id].parent = curr.node
            heapq.heapify(heap)
        return mst_result
