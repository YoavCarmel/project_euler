from typing import List

from libs.files import create_matrix_from_file
from libs.objects.graphs.directed_graph import DirectedGraph


def ans():
    mat: List[List[int]] = create_matrix_from_file("P081")
    g, source, target = create_graph_from_matrix(mat)
    return DirectedGraph.shortest_distance(source, target)[0] + g.get_node(0).get_value()


def create_graph_from_matrix(mat: List[List[int]]) -> (DirectedGraph, int, int):
    """
    length of a connection is the value of the "other"
    :param mat: matrix that represents a graph
    :return: a graph object from the input matrix, and source and target for the distance calculation
    """
    g = DirectedGraph()
    row_length = len(mat[0])
    column_length = len(mat)
    for i in range(column_length):
        for j in range(row_length):
            g.add_node(mat[i][j])
    for n in range(len(g) - 1):
        if n % row_length == row_length - 1:  # end of row
            g.add_connection(n, n + row_length, g.get_node(n + row_length).get_value())
        elif n // column_length == column_length - 1:  # last row
            g.add_connection(n, n + 1, g.get_node(n + 1).get_value())
        else:
            g.add_connection(n, n + row_length, g.get_node(n + row_length).get_value())
            g.add_connection(n, n + 1, g.get_node(n + 1).get_value())
    # source is the first added node (top left), target is the last added node (bottom right)
    return g, g.get_node(0), g.get_node(len(g) - 1)
