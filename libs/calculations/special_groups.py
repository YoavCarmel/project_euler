from typing import List, Set, Dict, Tuple

from libs.calculations.groups_theory import power_set


def is_special_sum_set(curr_nums: List[int], subsets_sums: Set[int] = None, is_sorted_big_to_small=False) -> bool:
    """
    :param curr_nums: the nums list to check if valid
    :param subsets_sums: all subsets sums, may be pre-calculated
    :param is_sorted_big_to_small: bool that says if we already have a sorted nums, sorted from biggest to smallest
    :return: True if the input nums list is a valid special sum set
    """
    if subsets_sums is None:
        subsets_sums = set([sum(subset) for subset in power_set(curr_nums)])
    if not is_sorted_big_to_small:
        curr_nums = sorted(curr_nums, reverse=True)
    """
    note: we can ignore the disjoint condition. is two subsets contain the same element, then after removing it
    the conditions are the same. we should just not check for non-disjoint, but it makes a calculation slower,
    so we ignore it and that's it.
    """
    # check for subsets sums condition
    if len(subsets_sums) != 2 ** len(curr_nums):
        return False
    # check for subsets sizes condition. first create the dict
    min_max: Dict[int, Tuple[int, int]] = dict()  # value = (min,max)
    for i in range(1, len(curr_nums)):
        min_max[i] = (sum(curr_nums[-i:]), sum(curr_nums[:i]))
    # now check for the dict.
    for i in range(1, len(curr_nums)):
        for j in range(1, i):
            if min_max[i][0] <= min_max[j][1]:  # there is a subset which is smaller but has a bigger sum
                return False
    return True
