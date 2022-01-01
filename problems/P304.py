from sympy import nextprime
from tqdm import tqdm

from libs.calculations.general import fibonacci_number_by_index


def ans():
    s = 0
    p = nextprime(10 ** 14)
    m = 1234567891011
    for _ in tqdm(range(10 ** 5)):
        s += fibonacci_number_by_index(p, mod=m)
        p = nextprime(p)
    return s % m
