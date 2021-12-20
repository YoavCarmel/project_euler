from typing import List

from libs.files import create_matrix_from_file
from libs.objects.graphs.directed_graph import DirectedGraph


def ans():
    mat: List[List[int]] = create_matrix_from_file("files//P082.txt", ",")
    g, source, target = create_graph_from_matrix(mat)
    return DirectedGraph.shortest_distance(source, target)[0]


def create_graph_from_matrix(mat: List[List[int]]) -> (DirectedGraph, int, int):
    """
    length of a connection is the value of the "other"
    the idea is to have a source that points to the left column and target that is pointed from the right column,
    both having a 0 value.
    :param mat: matrix that represents a graph
    :return: a graph object from the input matrix, and source and target for the distance calculation
    """
    g = DirectedGraph()
    row_length = len(mat[0])
    column_length = len(mat)

    for i in range(column_length):
        for j in range(row_length):
            g.add_node(mat[i][j])
    source = g.add_node(0)
    target = g.add_node(0)

    for n in range(row_length * column_length):
        if n == row_length - 1:  # top right corner
            g.add_connection(n, n + row_length, g.get_node(n + row_length).get_value())
            g.add_connection(n, target.node_id, 0)  # point to target
        elif n == row_length * column_length - 1:  # bottom left corner
            g.add_connection(n, n - row_length, g.get_node(n - row_length).get_value())
            g.add_connection(n, target.node_id, 0)  # point to target
        elif n % row_length == row_length - 1:  # right but not corner:
            g.add_connection(n, n + row_length, g.get_node(n + row_length).get_value())
            g.add_connection(n, n - row_length, g.get_node(n - row_length).get_value())
            g.add_connection(n, target.node_id, 0)  # point to target
        elif n < row_length - 1:  # top but not top right
            g.add_connection(n, n + row_length, g.get_node(n + row_length).get_value())
            g.add_connection(n, n + 1, g.get_node(n + 1).get_value())
        elif (column_length - 1) * row_length <= n < row_length * column_length - 1:  # bottom but not bottom right
            g.add_connection(n, n - row_length, g.get_node(n - row_length).get_value())
            g.add_connection(n, n + 1, g.get_node(n + 1).get_value())
        else:
            g.add_connection(n, n + row_length, g.get_node(n + row_length).get_value())
            g.add_connection(n, n - row_length, g.get_node(n - row_length).get_value())
            g.add_connection(n, n + 1, g.get_node(n + 1).get_value())

        if n % row_length == 0:  # left
            g.add_connection(source.node_id, n, g.get_node(n).get_value())  # pointed by source
    return g, source, target
