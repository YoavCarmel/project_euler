from collections import defaultdict
from math import sqrt
from typing import Dict, Set, Tuple


def ans():
    max_big_l = 1.5 * 10 ** 6
    solutions: Dict[int, Set[Tuple[int, ...]]] = defaultdict(set)
    # create pythagorean triplets
    for s in range(1, int((sqrt(1 + 2 * max_big_l) - 1) / 2) + 1):
        for t in range(1, s):
            big_l = 2 * s * s + 2 * s * t
            if big_l > max_big_l:
                break
            solutions[big_l].add(tuple(sorted([2 * s * t, s * s - t * t])))
    # add more triplets
    for i in list(solutions):
        for k in range(2, int(max_big_l / i) + 1):
            for t in solutions[i]:
                solutions[i * k].add(tuple(sorted([t[0] * k, t[1] * k])))
    count = 0
    # get L values with exactly one triangle
    for i in solutions:
        if len(solutions[i]) == 1:
            count += 1
    return count
