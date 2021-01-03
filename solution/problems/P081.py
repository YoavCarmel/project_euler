from solution.libs.files import create_matrix_from_file
from solution.objects.graph import Graph


def ans():
    mat = create_matrix_from_file("files//P081.txt", ",")
    g, source, target = create_graph_from_matrix(mat)
    return g.shortest_distance(source, target)[0]


def create_graph_from_matrix(mat):
    g = Graph()
    source = None
    target = None
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            g.add_node(mat[i][j])
            if i == j == 0:
                source = g.get_node(g.next_id - 1)
            if i == len(mat) - 1 and j == len(mat[len(mat) - 1]) - 1:
                target = g.get_node(g.next_id - 1)
    for n in range(len(g.nodes)):
        if n == len(g.nodes) - 1:
            continue
        if n % len(mat[0]) == len(mat[0]) - 1:  # end of row
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
        elif n // len(mat) == len(mat) - 1:  # last row
            g.get_node(n).add_child(g.get_node(n + 1))
        else:
            g.get_node(n).add_child(g.get_node(n + 1))
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
    return g, source, target
