from __future__ import annotations

from abc import ABC, abstractmethod
import heapq
from typing import Dict, List, Set, NamedTuple, Tuple, Union, Optional

from objects.graphs.node import Node


class Graph(ABC):
    def __init__(self):
        self._nodes: Dict[int, Node] = dict()  # the graph
        self.__next_id: int = 0  # the next id to add

    def add_node(self, value=None) -> Node:
        """
        create a new node, add it to the dict with the current id, increment the id, and return the new nod
        :param value: value of the node
        :return: the new node
        """
        new_node = Node(self.__next_id, value)
        self._nodes[self.__next_id] = new_node
        self.__next_id += 1
        return new_node

    def get_node(self, node_id: int) -> Node:
        """
        :param node_id: id of a wanted node
        :return: the node with the input id
        """
        return self._nodes[node_id]

    def get_all_nodes(self) -> List[Node]:
        """
        :return: a list of all nodes in graph
        """
        return list(self._nodes.values())

    @abstractmethod
    def add_connection(self, n1: int, n2: int, length: float = 1):
        """
        add a connection between n1 and n2
        :param n1: source id
        :param n2: target id
        :param length: length of edge
        :return: None
        """
        pass

    def connections_lengths_sum(self) -> float:
        """
        :return: sum of lengths of all connections
        """
        s = 0
        for node in self.get_all_nodes():
            for connection in node.get_connections():
                s += connection.length
        return s

    @abstractmethod
    def weight(self) -> Union[float, int]:
        """
        :return: weight of the graph
        """
        pass

    def __len__(self):
        return len(self._nodes)

    def __copy__(self) -> Graph:
        g = type(self)()
        g._nodes = {node.node_id: Node(node.node_id, node.get_value()) for node in self.get_all_nodes()}
        for node in self.get_all_nodes():
            for connection in node.get_connections():
                g.add_connection(node.node_id, connection.other.node_id, connection.length)
        g.__next_id = self.__next_id
        return g

    @staticmethod
    def shortest_distance(source: Node, target: Node) -> Tuple[float, List[int]]:
        """
        calculate the shortest distance between input source and target
        :param source: source of path
        :param target: target of path
        :return: the length of the shortest path, and list of ids of all nodes in path from source to target (inclusive)
        """

        class SearchNode(NamedTuple):
            node: Node
            total_dist: float
            parent: Optional[SearchNode]

            def __lt__(self, other: SearchNode):
                return self.total_dist < other.total_dist

        def find_search_node_index_in_heap(h: List[SearchNode], node: Node) -> Optional[int]:
            """
            :param h: heap
            :param node: wanted node
            :return: the index in heap of the SearchNode that contains the node
            """
            for index, sn in enumerate(h):
                if sn.node.node_id == node.node_id:
                    return index
            return None

        # run dijkstra's algorithm
        heap: List[SearchNode] = list()
        heapq.heappush(heap, SearchNode(source, 0, None))
        closed: Set[int] = {source.node_id}
        result_sn: SearchNode = ...
        while len(heap) != 0:
            head = heapq.heappop(heap)
            if head.node.node_id == target.node_id:
                # we got to the target. we finished the run
                result_sn = head
                break
            closed.add(head.node.node_id)
            in_heap: Set[int] = {sn.node.node_id for sn in heap}
            # go over all connections of current node (head)
            for connection in head.node.get_connections():
                if connection.other.node_id not in closed and connection.other.node_id not in in_heap:
                    # add a new unseen node to the heap
                    heapq.heappush(heap, SearchNode(connection.other, head.total_dist + connection.length, head))
                elif connection.other.node_id in in_heap and head.total_dist + connection.length < \
                        heap[find_search_node_index_in_heap(heap, connection.other)].total_dist:
                    # update an existing node to a smaller distance
                    i = find_search_node_index_in_heap(heap, connection.other)
                    heap[i] = SearchNode(connection.other, head.total_dist + connection.length, head)
        # now we have the target SearchNode
        result_distance = result_sn.total_dist
        # get the path back
        path: List[int] = list()
        while result_sn.node.node_id != source.node_id:
            path.append(result_sn.node.node_id)
            result_sn = result_sn.parent
        path.append(result_sn.node.node_id)
        path.reverse()
        return result_distance, path

    def __eq__(self, other: Graph):
        if other._nodes.keys() != self._nodes.keys():
            return False
        for node in self.get_all_nodes():
            other_node = other.get_node(node.node_id)
            if node.get_value() != other_node.get_value():
                return False
            if len(node.get_connections()) != len(other_node.get_connections()):
                return False
            connections_ids = {(con.other.node_id, con.length) for con in node.get_connections()}
            for con in other_node.get_connections():
                if (con.other.node_id, con.length) not in connections_ids:
                    print("X")
                    return False
            other_connections_ids = {(con.other.node_id, con.length) for con in other_node.get_connections()}
            for con in node.get_connections():
                if (con.other.node_id, con.length) not in other_connections_ids:
                    return False
        return True

    def __str__(self):
        s = "Graph:\n"
        for node in self.get_all_nodes():
            s += f"id:{node.node_id},value:{node.get_value()},connections: [ "
            for con in node.get_connections():
                s += f"({con.other.node_id},{con.length}) "
            s += "]\n"
        return s

    def expand_graph(self, size: int, nodes_values=None):
        """
        add nodes to the graph
        :param size: number of nodes to add
        :param nodes_values: value of nodes
        """
        for _ in range(size):
            self.add_node(nodes_values)
