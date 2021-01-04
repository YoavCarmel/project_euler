from typing import Dict

from sympy import primefactors


def ans():
    wanted: int = 4
    i: int = 1
    while True:
        # get skip size
        if len(primefactors(i + 3)) != wanted:
            i += 4
        elif len(primefactors(i + 2)) != wanted:
            i += 3
        elif len(primefactors(i + 1)) != wanted:
            i += 2
        elif len(primefactors(i)) != wanted:
            i += 1
        else:
            return i
