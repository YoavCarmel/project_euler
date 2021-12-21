from typing import List

from libs.files import create_matrix_from_file
from libs.objects.graphs.undirected_graph import UndirectedGraph


def ans():
    g = get_graph_from_matrix(create_matrix_from_file("P107", to_int=False))
    mst_g = g.mst()
    return g.weight() - mst_g.weight()


def get_graph_from_matrix(mat: List[List[str]]) -> UndirectedGraph:
    """
    :param mat: input matrix that represents the graph
    :return: the graph
    """
    g = UndirectedGraph()
    g.expand_graph(len(mat))
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != "-":
                g.add_connection(i, j, int(mat[i][j]))
    return g
