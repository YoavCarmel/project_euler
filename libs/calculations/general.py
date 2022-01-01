import math
from typing import List, Set

import numpy as np

from libs.objects.frac import Frac
from libs.objects.frac_with_sqrt import QPair, FracWithSqrt


def base2(x: int) -> int:
    """
    :param x: an integer
    :return: the input number in base 2, as int
    """
    return int(bin(x)[2:])


def continued_fraction_of_sqrt(x: int) -> List[int]:
    """
    returns the coefficients cycle of the continued fraction of sqrt(input).
    empty list if input is perfect square
    :param x: number to get continued fraction of its square
    :return: the coefficients cycle of the continued fraction of sqrt(input)
    """
    sqrt_x: float = math.sqrt(x)
    if sqrt_x.is_integer():
        return []
    s: Set[QPair] = set()  # set of all pairs of QPairs
    l: List[QPair] = list()  # list of these pairs, the result cycle
    # create the initial pair
    start_value: FracWithSqrt = FracWithSqrt(Frac(1), Frac(0), x)
    pair: QPair = start_value.split_int_nonint()
    # calculate the continued fractions until we get a repetition
    while pair not in s:
        s.add(pair)
        l.append(pair)
        # get new pair
        r: FracWithSqrt = pair.rem.flip()
        pair = r.split_int_nonint()
    # the whole parts of the pairs until the repetition in the cycle
    return [i.whole for i in l[l.index(pair):]]


def power_mat(mat: np.ndarray, p: int, *, mod=None, dtype="object") -> np.ndarray:
    """
    calculate mat^p, where mat is a square matrix, and using matrix multiplication
    :param mat: the matrix
    :param p: the power
    :param mod: mod on all values
    :param dtype: the dtype of the matrix. default is object, for the case where numbers because too big for the int64,
        which is likely to happen in this function. If you know for sure that the values should not exceed a certain
        int size limit, you can make it much faster with this dtype (and also have this dtype in mat)
    :return: the result matrix
    """
    if p == 0:
        return np.identity(mat.shape[0], dtype=dtype)
    temp = power_mat(mat, p // 2, mod=mod)
    temp_s = temp @ temp
    if mod is None:
        if p % 2 == 0:
            return temp_s
        else:
            return temp_s @ mat
    else:
        temp_s = temp_s % mod
        if p % 2 == 0:
            return temp_s
        else:
            return (temp_s @ mat) % mod


def sum_first_n(max_n: int):
    """
    sum of first n numbers: [1,2,3,...,max_n]
    """
    return ((max_n + 1) * max_n) // 2


def pascal_triangle(n_rows: int, mod: int = None) -> np.ndarray:
    tri = np.zeros((n_rows, n_rows), dtype="uint64")
    tri[0][0] = 1
    for r in range(1, n_rows):
        tri[r] = tri[r - 1]
        tri[r, 1:] += tri[r - 1, :-1]
        if mod is not None:
            tri[r] %= mod
    return tri


def factorial_modulo(n, m) -> int:
    """
    :return: n!%m
    """
    res = 1
    for i in range(2, n + 1):
        res = (res * i) % m
    return res
