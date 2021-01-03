from libs.calculations import binom


def ans():
    count = 0
    for n in range(1, 101):
        for r in range(n):
            if binom(n, r) > 10 ** 6:
                count += 1
    return count
