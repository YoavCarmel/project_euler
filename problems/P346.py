from math import sqrt


def ans():
    res = set()
    max_n = 10 ** 12
    max_b = (sqrt(4 * max_n - 3) - 1) / 2
    # all numbers equal 11 in base n-1. we just need to find numbers who are at least 3 1s in any other base.
    for b in range(2, int(max_b) + 1):
        biggest_dig = b * b
        num = biggest_dig + b + 1
        while num <= max_n:
            res.add(num)
            biggest_dig *= b
            num += biggest_dig
    # add 1 at the end because it is a solution for all b values but we only look at length 111+
    return sum(res) + 1
