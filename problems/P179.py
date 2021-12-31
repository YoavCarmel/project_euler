import numpy as np

from libs.calculations.general import divisors_count


def ans():
    divs = divisors_count(10 ** 7 + 1)
    pairs = divs[1:] == divs[:-1]
    return np.sum(pairs)
