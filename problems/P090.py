from itertools import combinations, product
from typing import Set


def ans():
    count = 0
    # go over all possible pairs of cubes
    for c1, c2 in product(combinations(range(10), 6), repeat=2):
        if is_good_arrangement(set(c1), set(c2)):
            count += 1
    return count // 2  # it counts twice for each arrangement, one for each side


def is_good_arrangement(c1: Set[int], c2: Set[int]) -> int:  # 01, 04, 09, 16, 25, 36, 49, 64, 81
    """
    :param c1: first cube
    :param c2: second cube
    :return: True if this is a good pair of cubes
    """
    # 01:
    if not ((0 in c1 and 1 in c2) or (0 in c2 and 1 in c1)):
        return False
    # 04:
    if not ((0 in c1 and 4 in c2) or (0 in c2 and 4 in c1)):
        return False
    # 09:
    if not ((0 in c1 and 9 in c2) or (0 in c2 and 9 in c1) or (0 in c1 and 6 in c2) or (0 in c2 and 6 in c1)):
        return False
    # 16
    if not ((1 in c1 and 6 in c2) or (1 in c2 and 6 in c1) or (1 in c1 and 9 in c2) or (1 in c2 and 9 in c1)):
        return False
    # 25
    if not ((2 in c1 and 5 in c2) or (2 in c2 and 5 in c1)):
        return False
    # 36
    if not ((3 in c1 and 6 in c2) or (3 in c2 and 6 in c1) or (3 in c1 and 9 in c2) or (3 in c2 and 9 in c1)):
        return False
    # 49 and 64
    if not ((4 in c1 and 6 in c2) or (4 in c2 and 6 in c1) or (4 in c1 and 9 in c2) or (4 in c2 and 9 in c1)):
        return False
    # 81:
    if not ((8 in c1 and 1 in c2) or (8 in c2 and 1 in c1)):
        return False
    # the cubes passed all tests
    return True
