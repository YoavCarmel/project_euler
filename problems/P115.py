from typing import Dict


def ans():
    n = 3
    m = 50
    values: Dict[int, int] = {0: 0, 1: 0, 2: 0}
    while True:
        values[n] = rec(n, m, values)
        if values[n] > 10 ** 6:
            return n - 2
        n += 1


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
    s += values[length_left - 1]
    # red with any length that does not end at the end
    for i in range(m, length_left):
        s += values[length_left - i - 1]
    s += 1  # red that ends at the end
    return s
