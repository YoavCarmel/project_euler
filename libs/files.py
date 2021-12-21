from typing import List

import numpy as np


def get_associated_txt(python_file_name: str) -> str:
    return "files//" + python_file_name + ".txt"


def create_matrix_from_file(python_file_name: str, delimiter: str = ",", to_int=True) -> np.ndarray:
    """
    read a matrix-like file
    """
    file_name = get_associated_txt(python_file_name)
    dtype = "int64" if to_int else "object"
    return np.loadtxt(file_name, delimiter=delimiter, dtype=dtype)


def get_file_lines(python_file_name: str) -> List[str]:
    """
    returns lines of the txt file associated with the input python file
    """
    file_name = get_associated_txt(python_file_name)
    with open(file_name) as f:
        return [line.strip() for line in f.readlines()]
