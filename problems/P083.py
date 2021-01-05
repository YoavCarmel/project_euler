from typing import List

from libs.files import create_matrix_from_file
from objects.graph import Graph


def ans():
    mat: List[List[int]] = create_matrix_from_file("files//P083.txt", ",")
    g, source, target = create_graph_from_matrix(mat)
    return Graph.shortest_distance(source, target)[0]


def create_graph_from_matrix(mat: List[List[int]]) -> (Graph, int, int):
    """
    :param mat: matrix that represents a graph
    :return: a graph object from the input matrix, and source and target for the distance calculation
    """
    g = Graph()
    source = None
    target = None
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            g.add_node(mat[i][j])
            if i == j == 0:
                source = g.get_node(g.next_id - 1)
            if i == len(mat) - 1 and j == len(mat[- 1]) - 1:
                target = g.get_node(g.next_id - 1)
    for n in range(len(g.nodes)):
        # corners
        if n == g.next_id - 1:  # bottom right
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - 1))
        elif n == (len(mat) - 1) * len(mat[0]):  # bottom left:
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
        elif n == len(mat[0]) - 1:  # top right
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - 1))
        elif n == 0:  # top left
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
        # edges
        elif n % len(mat[0]) == len(mat[0]) - 1:  # right
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - 1))
        elif n % len(mat[0]) == 0:  # left
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
        elif n < len(mat[0]):  # top
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
            g.get_node(n).add_child(g.get_node(n - 1))
        elif n > (len(mat) - 1) * len(mat[0]):  # bottom
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
            g.get_node(n).add_child(g.get_node(n - 1))
        # middle
        else:
            g.get_node(n).add_child(g.get_node(n + 1))
            g.get_node(n).add_child(g.get_node(n - 1))
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
    return g, source, target
