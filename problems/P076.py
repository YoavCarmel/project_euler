from collections import defaultdict
from typing import Dict


def ans():
    # a[i][j] is number of partitions with sum i and biggest number is j
    n = 100
    a: Dict[int, Dict[int, int]] = defaultdict(dict)
    a[0][0] = 1
    for i in range(1, n + 1):
        a[i][0] = 0
        for j in range(1, i + 1):
            # either put j and handle the rest, or dont put j and lower it by 1
            a[i][j] = a[i - j][min(i - j, j)] + a[i][j - 1]
    return a[n][n] - 1
