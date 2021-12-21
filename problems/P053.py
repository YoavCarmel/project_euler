from libs.calculations.general import binom


def ans():
    count: int = 0
    # brute force
    for n in range(1, 101):
        for r in range(n):
            if binom(n, r) > 10 ** 6:
                # found another one
                count += 1
    return count
