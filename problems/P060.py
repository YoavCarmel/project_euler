from typing import Dict, Set, List

from sympy import isprime, nextprime

from libs.calculations.numbers_operations import concat_nums


def ans():
    a = 3
    primes: List[int] = []
    valids: Dict[int, Set[int]] = dict()
    while True:
        valids[a] = {smaller_prime for smaller_prime in primes if concatenated_primes(smaller_prime, a)}
        primes.append(a)
        valids_a = valids[a]
        for b in valids_a:
            valids_ab = valids_a.intersection(valids[b])
            for c in valids_ab:
                valids_abc = valids_ab.intersection(valids[c])
                for d in valids_abc:
                    valids_abcd = valids_abc.intersection(valids[d])
                    for e in valids_abcd:
                        return a + b + c + d + e
        a = nextprime(a)


def concatenated_primes(x: int, y: int) -> bool:
    """
    :param x: first number, prime
    :param y: second number, prime
    :return: True if x,y is a concatenated primes pair
    """
    return isprime(concat_nums(x, y)) and isprime(concat_nums(y, x))
