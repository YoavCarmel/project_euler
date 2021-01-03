from solution.libs.files import create_matrix_from_file
from solution.objects.graph import Graph


def ans():
    mat = create_matrix_from_file("files//P082.txt", ",")
    g, source, target = create_graph_from_matrix(mat)
    return g.shortest_distance(source, target)[0]


def create_graph_from_matrix(mat):
    g = Graph()
    g.add_node(0)
    source = g.get_node(0)

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            g.add_node(mat[i][j])

    g.add_node(0)
    target = g.get_node(g.next_id - 1)

    for n in range(1, len(g.nodes) - 1):
        if n == len(mat[0]):  # right up corner
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(target)
        elif n == g.next_id - 2:  # right down corner
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(target)
        elif n % len(mat[0]) == 0:  # right but not corner:
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(target)
        elif n < len(mat[0]):  # top but not top right
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
        elif n // len(mat) == len(mat) - 1:  # bottom but not bottom right
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
        else:
            g.get_node(n).add_child(g.get_node(n + len(mat[0])))
            g.get_node(n).add_child(g.get_node(n - len(mat[0])))
            g.get_node(n).add_child(g.get_node(n + 1))
        if n % len(mat[0]) == 1:  # left
            g.get_node(0).add_child(g.get_node(n))

    return g, source, target
