from typing import List, TextIO

import numpy as np

from libs.chars import is_any_case_letter, is_number_char


def ans():
    nums = np.array(load_file())
    return get_sum_for_solution_of_array(nums[0::3]) \
           + get_sum_for_solution_of_array(nums[1::3]) \
           + get_sum_for_solution_of_array(nums[2::3])


def get_sum_for_solution_of_array(nums: np.ndarray) -> int:
    """
    calculate the sum of the correct result for the input array
    """
    return int(np.sum(get_only_possible_value(nums)))


def get_only_possible_value(nums: np.ndarray) -> np.ndarray:
    """
    loop over the possible c keys, if found a valid xor result, return it
    """
    for c in range(ord('a'), ord('z') + 1):
        temp = np.bitwise_xor(nums, c)
        if check_all_letters(temp):
            return temp
    raise Exception("Something is wrong with the keys")


def check_all_letters(nums: List[int]) -> bool:
    """
    :param nums: a list of numbers
    :return: True if all chars are valid
    """
    return all(is_wanted_char(chr(c)) for c in nums)


def is_wanted_char(c: chr) -> bool:
    """
    :param c: input char
    :return: True if this char is valid
    """
    return is_any_case_letter(c) or is_number_char(c) or c in {" ", ".", ",", "(", ")", "'", '"', ";", "!", "?", "[",
                                                               "]", "/", "+", ":", "{", "}", "="}


def load_file() -> List[int]:
    """
    :return: input file split by commas, values converted to ints
    """
    with open("files//P059.txt") as f:
        return [int(i) for i in f.read().split(",")]
