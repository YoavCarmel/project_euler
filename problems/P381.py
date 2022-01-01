from tqdm import tqdm

from libs.calculations.numbers_theory import sieve_primes, inverse_mod


def ans():
    max_p = 10 ** 8
    primes = sieve_primes(max_p)
    res = 0
    for p in tqdm(primes[2:]):  # skip 2,3
        res += s(int(p))
    return res


def s(p):
    # we know that (n-1)=-1 for all n
    res = -1
    inv = p - 1
    for k in range(1, 4 + 1):
        # in each step remove (p-k) from the product
        inv = (inv * inverse_mod(p - k, p)) % p
        res += inv
    return res % p
