from typing import List

from sympy import isprime


def ans():
    # a[i][j] is number of partitions with sum i and biggest number is j, and j must be there
    a: List[List[int]] = [[0]]
    n = 1
    while True:
        a.append([0] * (n + 1))  # create list
        # calculate list
        for j in range(1, n):
            if isprime(j):
                a[n][j] = sum(a[n - j][:min(j + 1, n - j + 1)])
        # stopping condition:
        if sum(a[-1]) > 5000:
            return n
        if isprime(n):
            a[n][n] = 1
        n += 1
