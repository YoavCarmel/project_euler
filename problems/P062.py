from typing import List, Dict

from libs.numbers_properties import digs_count


def ans():
    # digs count of number is a frozenset of pairs:(num,count)
    cubes: Dict[frozenset, List[int]] = dict()
    i = 1
    target_size = 5
    while True:
        i3 = i ** 3
        digs_count_i3 = digs_count_frozenset(i3)
        if digs_count_i3 in cubes:
            cubes[digs_count_i3].append(i3)
            if len(cubes[digs_count_i3]) == target_size:
                return min(cubes[digs_count_i3])
        else:
            cubes[digs_count_i3] = [i3]
        i += 1


def digs_count_frozenset(x) -> frozenset:
    d = digs_count(x)
    return frozenset([(k, d[k]) for k in d])
