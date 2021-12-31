from cachetools import cached
from cachetools.keys import hashkey

from libs.calculations.numbers_theory import sieve_primes, totient_euler_range


def ans():
    max_n = 4 * 10 ** 7
    primes = sieve_primes(max_n)
    totient_of_all = totient_euler_range(max_n, primes=primes)
    d = {i: totient_chain_length(i, totient_of_all) for i in primes}
    wanted_chain_length = 25
    return sum([p for p, v in d.items() if v == wanted_chain_length])


@cached(cache={}, key=lambda n, totient_of_all: hashkey(n))
def totient_chain_length(n, totient_of_all):
    if n == 1:
        return 1
    return 1 + totient_chain_length(totient_of_all[n], totient_of_all)
