from typing import List

import numpy as np
from tqdm import tqdm

from libs.calculations.general import power_mat

FIB_MAT = np.array([[1, 1], [1, 0]], dtype="object")  # the fibonacci matrix


def fibonacci_number_by_index(index: int, *, mod=None):
    """
    calculated fast using matrix multiplication and power, in log(n) time
    :param index: index of wanted fibonacci number
    :param mod: mod on the result
    :return: the number
    """
    if index == 0:
        return 0
    mat_n = power_mat(FIB_MAT, index - 1, mod=mod)
    res = np.sum(mat_n[1])
    if mod is not None:
        res = res % mod
    return res


def fibonacci_numbers_by_indices(indices: List[int], *, mod=None):
    """
        calculated fast using matrix multiplication and power, in log(n) time
        :param indices: indices of wanted fibonacci numbers
        :param mod: mod on the result
        :return: the number
        """
    nums = []
    first_index = indices[0]
    if first_index == 0:
        raise Exception("dont handle 0 index")
    mat = power_mat(FIB_MAT, first_index - 1, mod=mod)
    nums.append(np.sum(mat[1]))
    for prev, curr in zip(indices, indices[1:]):
        power_diff = curr - prev
        mat = mat @ power_mat(FIB_MAT, power_diff, mod=mod)
        if mod is not None:
            mat = mat % mod
            nums.append(np.sum(mat[1]) % mod)
        else:
            nums.append(np.sum(mat[1]))
    return nums
