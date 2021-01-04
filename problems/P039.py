from collections import defaultdict
from math import sqrt
from typing import Dict

from libs.numbers_properties import is_int


def ans():
    count_list: Dict[int, int] = defaultdict(int)
    # go over all possible lengths
    for a in range(1, 500):
        ap2 = a ** 2
        for b in range(1, a):
            c = sqrt(ap2 + b ** 2)
            if is_int(c):
                # we found a triple
                c = int(c)
                p = a + b + c
                if p <= 1000:
                    count_list[p] += 1
    return max(count_list, key=lambda k: count_list[k])
