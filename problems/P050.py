from sympy import primerange


def ans():
    limit = 10 ** 6
    primes = list(primerange(1, limit + 1))
    window = 0
    s = 0
    while s < limit:
        s += primes[window]
        window += 1
    while True:
        m = -1
        for i in range(len(primes) - window + 1):
            primes_window = primes[i:i + window]
            spw = sum(primes_window)
            if spw > limit:
                break
            if spw in primes:
                m = max(m, spw)
        if m != -1:
            return m
        window -= 1
