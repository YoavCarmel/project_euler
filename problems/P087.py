from sympy import primerange
from math import pow, sqrt


def ans():
    limit = 5 * 10 ** 7
    nums = set()
    # get all primes smaller than the sqrt of limit
    primes = list(primerange(2, int(sqrt(limit)) + 2))
    # get primes valid for 4th power
    p4_limit = int(pow(limit, (1 / 4)))
    p4_range = [i for i in primes if i <= p4_limit]
    for p4 in p4_range:
        # get primes valid for 3rd power, based on the p4 prime
        p3_limit = int(pow(limit - p4 ** 4, 1 / 3))
        p3_range = [i for i in primes if i <= p3_limit]
        for p3 in p3_range:
            # get primes valid for 2nd power, based on the p4,p3 primes
            p2_limit = int(pow(limit - p4 ** 4 - p3 ** 3, 1 / 2))
            p2_range = [i for i in primes if i <= p2_limit]
            for p2 in p2_range:
                nums.add(p4 ** 4 + p3 ** 3 + p2 ** 2)
    return len(nums)
