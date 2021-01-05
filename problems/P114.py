from typing import Dict


def ans():
    n = 50
    values: Dict[int, int] = dict()
    return rec(n, values)


def rec(length_left: int, values: Dict[int, int]) -> int:
    """
    :param length_left: the length of the row left to fill
    :param values: the current values
    :return: number of possibilities to fill length_left
    """
    if length_left < 3:
        return 1  # finished an option
    # in each step, choose between one more grey, or a new red with any length from 3 to the end
    s = 0
    # one more grey
    if length_left - 1 in values:
        s += values[length_left - 1]
    else:
        res = rec(length_left - 1, values)
        values[length_left - 1] = res
        s += res
    # red with any length that does not end at the end
    for i in range(3, length_left):
        # minus 1 for the grey between this and the next
        if length_left - i - 1 in values:
            s += values[length_left - i - 1]
        else:
            res = rec(length_left - i - 1, values)
            values[length_left - i - 1] = res
            s += res
    s += 1  # red that ends at the end
    return s
