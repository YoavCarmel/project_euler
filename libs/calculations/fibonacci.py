import numpy as np

from libs.calculations.general import power_mat


def fibonacci_number_by_index(index: int, *, mod=None):
    """
    calculated fast using matrix multiplication and power, in log(n) time
    :param index: index of wanted fibonacci number
    :param mod: mod on the result
    :return: the number

    NOTE: cant use numpy here because numbers are too big
    """
    if index == 0:
        return 0
    if index == 1 or index == 2:
        return 1

    fib_mat = np.array([[1, 1], [1, 0]])  # the fibonacci matrix
    mat_n = power_mat(fib_mat, index - 2, mod=mod)
    res = np.sum(mat_n[0])
    if mod is not None:
        res = res % mod
    return res
