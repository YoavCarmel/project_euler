from typing import Set, Tuple


def ans():
    max_cycle: int = 0
    found_d: int = 0
    for i in range(1, 1000):
        ldc = long_division_cycle(i)
        if max_cycle < ldc:
            max_cycle = ldc
            found_d = i
    return found_d


def long_division_cycle(x):
    """
    :param x: denominator
    :return: length of cycle of decimal representation of 1/x
    """
    num: int = 1
    result_rem: Set[Tuple[int, int]] = set()
    while num != 0:
        while num < x:
            num *= 10
            curr_len = len(result_rem)
            result_rem.add((num // x, num % x))
            if len(result_rem) == curr_len:  # we got a loop
                return curr_len
        num -= x * (num // x)
    return 0
