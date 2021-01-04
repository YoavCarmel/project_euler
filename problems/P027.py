from typing import Set

from sympy import isprime


def ans():
    max_primes: int = 0
    p: int = 0
    primes_found: Set[int] = set()
    """
    if a is even and b is odd, then every odd n will result in an even result, so remove these options
    if a is odd and b is even, then every n will result in an even result, so remove these options
    if a is even and b is even, then every even n will result in an even result, so remove these options
    
    in conclusion: work only on odd a,b values
    """
    for a in range(-999, 1000, 2):
        for b in range(-999, 1001, 2):
            n = get_max_n(a, b, primes_found)
            if n > max_primes:
                max_primes = n
                p = a * b
    return p


def apply_quadratic(n: int, a: int, b: int) -> int:
    """
    apply the formula
    """
    return n * n + a * n + b


def get_max_n(a: int, b: int, primes_found: Set[int]) -> int:
    """
    :param a: a of the formula
    :param b: b of the formula
    :param primes_found: set of already found primes to prevent repeated computations
    :return: number of consecutive primes
    """
    n: int = 0  # n is also counter
    f: int = apply_quadratic(n, a, b)
    while f in primes_found or isprime(f):
        primes_found.add(f)
        n += 1
        f = apply_quadratic(n, a, b)
    return n
