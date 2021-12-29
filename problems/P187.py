import math

import numpy as np
from tqdm import tqdm

from libs.calculations.numbers_theory import sieve_primes


def ans():
    max_n = 10 ** 8
    primes = sieve_primes(max_n // 2)
    s = 0
    primes_to_iterate = primes[:np.searchsorted(primes, math.sqrt(max_n))]
    for i, p in tqdm(enumerate(primes_to_iterate)):
        less = np.searchsorted(primes, max_n / p)
        s += less - i
        primes = primes[:less + 1]
    return s
