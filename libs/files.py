from typing import List, Union


def create_matrix_from_file(file_name: str, delimiter: str, to_int=True) -> Union[List[List[str]], List[List[int]]]:
    f = open(file_name)
    if to_int:
        mat: List[List[int]] = []
        for line in f.readlines():
            mat.append([int(i) for i in line.strip("\n").split(delimiter)])
    else:
        mat: List[List[str]] = []
        for line in f.readlines():
            mat.append([i for i in line.strip("\n").split(delimiter)])
    return mat


def get_file_lines(python_file_name: str) -> List[str]:
    file_name = "files//" + python_file_name + ".txt"
    lines: List[str] = []
    f = open(file_name)
    for line in f.readlines():
        lines.append(line.strip("\n"))
    return lines
