from sympy import divisor_count


def ans():
    div = 500
    s = 0
    i = 1
    while True:
        s += i
        if divisor_count(s) > div:
            return s
        i += 1

