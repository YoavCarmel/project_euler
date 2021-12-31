from math import log, sqrt

import numpy as np

from libs.calculations.numbers_theory import sieve_primes


def ans():
    max_n = 10 ** 7
    primes = sieve_primes(max_n)
    primes_sqrt = primes[:np.searchsorted(primes, sqrt(max_n)) + 1]
    s = 0
    for i, p in enumerate(primes_sqrt):
        primes_to_iterate = primes[i + 1:np.searchsorted(primes, max_n // p) + 1]
        for q in primes_to_iterate:
            s += m(p, q, max_n)
    return s


def m(p, q, n) -> int:
    max_ns = list()
    q_powered = q
    n_div_p = n // p
    while q_powered <= n_div_p:
        p_power = int(round(log(n // q_powered, p), 6))  # round because of float issues
        max_ns.append(q_powered * (p ** p_power))
        q_powered *= q
    if len(max_ns) == 0:
        return 0
    return max(max_ns)
