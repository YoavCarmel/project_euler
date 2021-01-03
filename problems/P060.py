from typing import Dict

from libs.numbers_operations import concat_nums
from sympy import isprime, nextprime


def ans():
    a = 3
    primes = []
    pairs: Dict[frozenset, bool] = dict()
    while True:
        primes.append(a)
        for ib in range(len(primes) - 1):
            if concated_primes(a, primes[ib], pairs):
                for ic in range(ib):
                    if concated_triple(a, primes[ib], primes[ic], pairs):
                        for id in range(ic):
                            if concated_four(a, primes[ib], primes[ic], primes[id], pairs):
                                for ie in range(id):
                                    if concated_five(a, primes[ib], primes[ic], primes[id], primes[ie], pairs):
                                        return a + primes[ib] + primes[ic] + primes[id] + primes[ie]
        a = nextprime(a)


def concated_primes(x, y, pairs: Dict):
    fxy = frozenset([x, y])
    if fxy in pairs:
        return pairs[fxy]
    res = isprime(concat_nums(x, y)) and isprime(concat_nums(y, x))
    pairs[fxy] = res
    return res


def concated_triple(a, b, c, pairs: Dict):
    # already checked (a,b)
    return concated_primes(a, c, pairs) and concated_primes(b, c, pairs)


def concated_four(a, b, c, d, pairs: Dict):
    # already checked (a,b,c)
    return concated_primes(a, d, pairs) and concated_primes(b, d, pairs) and concated_primes(c, d, pairs)


def concated_five(a, b, c, d, e, pairs: Dict):
    # already checked (a,b,c,d)
    return concated_primes(a, e, pairs) and concated_primes(b, e, pairs) and \
           concated_primes(c, e, pairs) and concated_primes(d, e, pairs)
