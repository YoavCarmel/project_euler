from tqdm import tqdm

from libs.calculations.numbers_theory import sieve_primes, inverse_mod
from libs.calculations.general import factorial_modulo


def ans():
    max_p = 10 ** 8
    primes = sieve_primes(max_p)
    primes = [int(p) for p in primes[2:]]  # skip 2,3
    res = 0
    for p in tqdm(primes):
        res += s(p)
    return res


def s(p):
    # we know that (n-1)=-1 for all n
    res = (p - 1)
    inv = 1
    for k in range(2, 5 + 1):
        inv = (inv * inverse_mod(p - k + 1, p)) % p
        res += (p - 1) * inv
    return res % p
