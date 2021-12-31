from sympy import nextprime


def ans():
    p = 2
    n = 1
    limit = 10 ** 10
    while True:
        ps = p * p
        r = (pow(p - 1, n, ps) + pow(p + 1, n, ps)) % ps
        if r > limit:
            return n
        p = nextprime(p)
        n += 1
