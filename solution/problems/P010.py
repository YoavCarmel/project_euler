from sympy import primerange


def ans():
    limit = 2000000
    return sum(primerange(2, limit + 1))
