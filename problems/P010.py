from sympy import primerange


def ans():
    limit: int = 2000000
    # return the sum of all primes in the range
    return sum(primerange(2, limit + 1))
