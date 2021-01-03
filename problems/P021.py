from sympy import divisors


def ans():
    sums = dict()
    n = 10000
    for i in range(1, n + 1):
        sums[i] = sum(divisors(i)) - i
    s = 0
    for i in range(1, n + 1):
        if sums[i] in sums and sums[i] != i and sums[sums[i]] == i:
            s += i
    return s
