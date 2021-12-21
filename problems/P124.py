from dataclasses import dataclass
from typing import List

from sympy import primefactors

from libs.calculations.general import list_product


@dataclass(init=True, repr=True, order=True, frozen=True)
class RadNum:
    rad: int
    num: int


def ans():
    n = 10 ** 5
    res_index = 10 ** 4
    rad_nums: List[RadNum] = list(sorted(RadNum(list_product(primefactors(i)), i) for i in range(1, n + 1)))
    return rad_nums[res_index - 1].num
