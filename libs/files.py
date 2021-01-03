from typing import List


def create_matrix_from_file(file_name: str, delimiter: str) -> List[List]:
    mat = []
    f = open(file_name)
    for line in f.readlines():
        mat.append([int(i) for i in line.strip("\n").split(delimiter)])
    return mat


def get_file_lines(python_file_name: str) -> List[str]:
    file_name = "files//" + python_file_name + ".txt"
    lines = []
    f = open(file_name)
    for line in f.readlines():
        lines.append(line.strip("\n"))
    return lines