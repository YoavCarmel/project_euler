from sympy import nextprime

from libs.calculations.fibonacci import fibonacci_numbers_by_indices


def ans():
    p = nextprime(10 ** 14)
    m = 1234567891011
    primes = [p]
    for _ in range(10 ** 5 - 1):
        primes.append(nextprime(primes[-1]))
    return sum(fibonacci_numbers_by_indices(primes, mod=m)) % m
