from typing import Dict

from libs.numbers_operations import concat_nums
from sympy import isprime, nextprime


def ans():
    a = 3
    primes = []
    pairs: Dict[frozenset, bool] = dict()
    while True:
        primes.append(a)
        for i_b in range(len(primes) - 1):
            if concatenated_primes(a, primes[i_b], pairs):
                for i_c in range(i_b):
                    if concatenated_triple(a, primes[i_b], primes[i_c], pairs):
                        for i_d in range(i_c):
                            if concatenated_four(a, primes[i_b], primes[i_c], primes[i_d], pairs):
                                for i_e in range(i_d):
                                    if concatenated_five(a, primes[i_b], primes[i_c], primes[i_d], primes[i_e], pairs):
                                        return a + primes[i_b] + primes[i_c] + primes[i_d] + primes[i_e]
        a = nextprime(a)


def concatenated_primes(x, y, pairs: Dict):
    fxy = frozenset([x, y])
    if fxy in pairs:
        return pairs[fxy]
    res = isprime(concat_nums(x, y)) and isprime(concat_nums(y, x))
    pairs[fxy] = res
    return res


def concatenated_triple(a, b, c, pairs: Dict):
    # already checked (a,b)
    return concatenated_primes(a, c, pairs) and concatenated_primes(b, c, pairs)


def concatenated_four(a, b, c, d, pairs: Dict):
    # already checked (a,b,c)
    return concatenated_primes(a, d, pairs) and concatenated_primes(b, d, pairs) and concatenated_primes(c, d, pairs)


def concatenated_five(a, b, c, d, e, pairs: Dict):
    # already checked (a,b,c,d)
    return concatenated_primes(a, e, pairs) and concatenated_primes(b, e, pairs) and \
           concatenated_primes(c, e, pairs) and concatenated_primes(d, e, pairs)
