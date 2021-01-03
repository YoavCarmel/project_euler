from collections import namedtuple
from math import inf
from Lib import heapq
from typing import Dict, List, Set, NamedTuple


# just for the typing of edge
class Node:
    pass


class Edge(NamedTuple):
    source: Node
    target: Node
    length: float


class Node:
    def __init__(self, id, value):
        self.id: int = id
        self.value: int = value
        self.children: List[Edge] = []

    def add_child(self, child, length=1):
        self.children.append(Edge(self, child, length))

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __lt__(self, other):
        return self.value < other.value


class Graph:
    def __init__(self, is_directed=False):
        self.nodes: Dict[int, Node] = dict()
        self.next_id = 0
        self.is_directed: bool = is_directed

    def add_node(self, value=None):
        self.nodes[self.next_id] = Node(self.next_id, value)
        self.next_id += 1

    def add_edge(self, source: Node, target: Node, length=1):
        self.nodes[source.id].add_child(self.nodes[target.id], length)
        if not self.is_directed:
            self.nodes[target.id].add_child(self.nodes[source.id], length)

    def get_node(self, id):
        return self.nodes[id]

    def weight(self):
        s = 0
        for n in self.nodes.values():
            for e in n.children:
                s += e.length
        if self.is_directed:
            return s
        return s // 2  # each edge was counted twice

    def shortest_distance(self, source: Node, target: Node):
        class SearchNode(NamedTuple):
            dist: float
            node: Node
            path: List[Node]

        def find_node_in_heap(node: Node, heap):
            for i in range(len(heap)):
                if heap[i].node == node:
                    return i
            return None

        h: List[SearchNode] = []
        heapq.heappush(h, SearchNode(source.value, source, [source]))
        closed: Set[Node] = {source}

        while len(h) != 0:
            head = heapq.heappop(h)
            if head.node == target:
                return head.dist, head.path
            closed.add(head.node)
            in_heap: List[Node] = [n.node for n in h]
            for edge in head.node.children:
                if edge.target not in closed and edge.target not in in_heap:
                    heapq.heappush(h,
                                   SearchNode(head.dist + edge.target.value, edge.target, head.path + [edge.target]))
                elif edge.target in in_heap and head.dist + edge.target.value < h[
                    find_node_in_heap(edge.target, h)].dist:
                    i = find_node_in_heap(edge.target, h)
                    h[i] = SearchNode(head.dist + edge.target.value, edge.target, head.path + [edge.target])
        return None


"""class Node(NamedTuple):
    value: float
    id: int


class UndirectedGraph:
    class UndirectedEdge(NamedTuple):
        n1: Node
        n2: Node
        length: float

    def __init__(self, is_directed):
        self.nodes: Dict[Node, Set[Edge]] = dict()
        self.is_directed = is_directed

    def get_nodes(self):
        return self.nodes.keys()

    def get_edges(self):
        return set([e for n in self.nodes.keys() for e in self.nodes[n]])"""
