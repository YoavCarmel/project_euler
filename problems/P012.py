from sympy import divisor_count


def ans():
    div: int = 500
    s: int = 0
    i: int = 1
    # continue until we find a number with more than 500 divisors
    while True:
        s += i
        if divisor_count(s) > div:
            return s
        i += 1
