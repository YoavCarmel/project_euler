from libs.numbers_properties import co_primes


def ans():
    low = 1 / 3
    high = 1 / 2
    max_d = 12000
    count = 0
    for d in range(1, max_d + 1):
        for n in range(d // 3, d // 2 + 1):
            # add all numbers that are coprimes to d, so each fraction will be counted once
            if low < n / d < high and co_primes(d, n):
                count += 1
    return count
