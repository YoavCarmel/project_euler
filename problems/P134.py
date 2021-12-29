from tqdm import tqdm

from libs.calculations.numbers_theory import inverse_mod, sieve_primes
from libs.calculations.numbers_properties import num_size

from sympy import nextprime


def ans():
    max_n = 10 ** 6
    primes = sieve_primes(max_n)
    # for (2,3)-> 12, for (3,5)-> no solution, start from (5,7):
    primes = [int(p) for p in primes[2:]]
    # add one more prime because the given limit is for p1
    primes.append(nextprime(primes[-1]))
    s_sum = 0
    for p1, p2 in zip(primes, primes[1:]):
        """
        let tp = 10**(number of digits of p1)
        so we want smallest s s.t.:
        s = k * tp + p1, and s % p2 = 0
        ->
        k * tp = -p1 (mod p2)
        k * tp = p2 - p1 (mod p2)
        k = (tp ^ -1) * (p2 - p1)  (mod p2)
        """
        power_10 = 10 ** num_size(p1)
        k = (inverse_mod(power_10, p2) * (p2 - p1)) % p2
        s = k * power_10 + p1
        s_sum += s
    return s_sum
