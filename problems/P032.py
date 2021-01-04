from typing import Set, List
from itertools import combinations, permutations
from libs.numbers_properties import is_pandigital
from libs.types_converting import list_to_num


def ans():
    good_nums: Set[int] = get_good_nums()
    good_nums_smaller1000 = {i for i in good_nums if i < 1000}

    products: Set[int] = set()
    for a in good_nums:
        for b in good_nums_smaller1000:
            p: int = a * b
            if len(str(a) + str(b) + str(p)) > 9:
                break
            if p in good_nums and is_pandigital(int(str(a) + str(b) + str(p)), 9):
                products.add(p)
    return sum(products)


def get_good_nums() -> Set[int]:
    """
    numbers should not have 0's or repeated digits
    :return: set of good nums
    """
    digs: List[int] = list(range(1, 10))
    result: Set[int] = set()
    for d in range(1, 4 + 1):
        for p in permutations(digs, d):
            result.add(list_to_num(p))
    return result
