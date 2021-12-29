from functools import lru_cache
from typing import List
from sympy import isprime

from libs.objects.frac import Frac

P = "P"
N = "N"


def ans():
    seq = "PPPPNNPPPNPPNPN"[::-1]
    max_tile = 500
    probabilities: List[List[Frac]] = list()
    # first char
    probabilities.append([Frac(0)] + [get_prob(tile, seq[0]) for tile in range(1, max_tile + 1)])
    # next chars
    for i, c in enumerate(seq[1:]):
        probs_01 = [Frac(0), probabilities[i][2] * get_prob(1, c)]
        prob_500 = [probabilities[i][max_tile - 1] * get_prob(max_tile, c)]
        probs_others = [get_prob(tile, c) * Frac(1, 2) * (probabilities[i][tile - 1] + probabilities[i][tile + 1])
                        for tile in range(2, max_tile)]
        probabilities.append(probs_01 + probs_others + prob_500)
    return sum(probabilities[-1], Frac(0)) * Frac(1, max_tile)


def get_prob(tile, char):
    is_prime = isprime(tile)
    if (is_prime and char == P) or (not is_prime and char == N):
        return Frac(2, 3)
    elif (is_prime and char == N) or (not is_prime and char == P):
        return Frac(1, 3)
    raise Exception(f"no option, {tile=}, {char=}")
