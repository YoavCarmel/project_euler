from collections import defaultdict
from typing import Dict, Set, NamedTuple, List

from libs.polygon_numbers import polygonal_number


class Chain(NamedTuple):
    nums: List[int]
    shapes: List[int]


def ans():
    set_3: Set[int] = create_3()
    dict_other_shapes: Dict[int, Dict[int, Set[int]]] = create_dict_other_shapes()
    for num in set_3:
        res = get_chain(Chain([num], [3]), dict_other_shapes)
        if res != -1:
            return res
    return None


def create_3() -> Set[int]:
    """
    :return: create a set of all 4 digits triangle number
    """
    res: Set[int] = set()
    i = 1
    while polygonal_number(i, 3) < 1000:
        i += 1
    pn = polygonal_number(i, 3)
    while pn < 10000:
        res.add(pn)
        i += 1
        pn = polygonal_number(i, 3)
    return res


def create_dict_other_shapes() -> Dict[int, Dict[int, Set[int]]]:
    """
    creates dict with key shape, value is dict from 2 left digits to all 4 digits of this shape with these 2 left digits
    :return: the dict as stated
    """
    polygons = [4, 5, 6, 7, 8]
    res: Dict[int, Dict[int, Set[int]]] = dict()
    for poly in polygons:
        i = 1
        while polygonal_number(i, poly) < 1000:
            i += 1
        res[poly] = defaultdict(set)
        pn = polygonal_number(i, poly)
        while pn < 10000:
            res[poly][pn // 100].add(pn)
            i += 1
            pn = polygonal_number(i, poly)
    return res


def get_chain(chain: Chain, poly_dict: Dict[int, Dict[int, Set[int]]]) -> int:
    """
    calculates the only valid chain
    :param chain: the current chain
    :param poly_dict: the dict of values
    :return: the sum of the valid chain. -1 if not found
    """
    if len(chain.nums) == 6:
        # if the chain is complete, check if the end matches the beginning
        if chain.nums[0] // 100 == chain.nums[-1] % 100:
            return sum(chain.nums)
        return -1  # else return -1, not found
    for shape in {3, 4, 5, 6, 7, 8}.difference(chain.shapes):
        for next_in_chain in poly_dict[shape][chain.nums[-1] % 100]:
            # go over all possible numbers to continue with, and continue with each of them
            res = get_chain(Chain(chain.nums + [next_in_chain], chain.shapes + [shape]), poly_dict)
            if res != -1:
                return res
    return -1
