from collections import defaultdict
from typing import List, Dict

from libs.numbers_properties import digs_count


def ans():
    # digs count of number is a frozenset of pairs:(num,count)
    cubes: Dict[frozenset, List[int]] = defaultdict(list)
    i = 1
    target_size = 5
    while True:
        # for each number, update the count of its digs count. if found count=5, return the min
        i3 = i ** 3
        digs_count_i3: frozenset = digs_count_frozenset(i3)
        cubes[digs_count_i3].append(i3)
        if len(cubes[digs_count_i3]) == target_size:
            return min(cubes[digs_count_i3])
        i += 1


def digs_count_frozenset(x: int) -> frozenset:
    """
    :param x: input number
    :return: input number's digits count as a frozenset
    """
    d = digs_count(x)
    return frozenset([(k, d[k]) for k in d])
