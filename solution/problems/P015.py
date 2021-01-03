from solution.libs.calculations import binom


def ans():
    # the number of ways for nXn gird is 2n choose n,
    # because you have this amount of different series of down and right
    n = 20
    return binom(2 * n, n)
