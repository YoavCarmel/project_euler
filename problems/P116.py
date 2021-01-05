from typing import Dict


def ans():
    n = 50
    return sum([rec(n, m, dict()) - 1 for m in [2, 3, 4]])


def rec(length_left: int, m: int, values: Dict[int, int]) -> int:
    """
    :param length_left: length left to fill
    :param m: size of block
    :param values: current values
    :return: number of possibilities for number_left with block size m
    """
    if length_left < m:
        return 1  # finished an option
    # in each step, choose between one more grey, or a new red with any length from 3 to the end
    s = 0
    # one more grey
    if length_left - 1 in values:
        s += values[length_left - 1]
    else:
        res = rec(length_left - 1, m, values)
        values[length_left - 1] = res
        s += res
    # one more tile of size m
    if length_left - m in values:
        s += values[length_left - m]
    else:
        res = rec(length_left - m, m, values)
        values[length_left - m] = res
        s += res
    return s
