from functools import reduce
from typing import List
from operator import mul

import numpy as np


def list_product(nums: List[int]):
    return reduce(mul, nums, 1)


def diffs_list(lst: List[int]) -> List[int]:
    """
    :param lst: a list of numbers
    :return: a list of the differences between each adjacent pair
    """
    lst_np = np.array(lst)
    return list(lst_np[:-1] - lst_np[1:])
