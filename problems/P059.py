from typing import List, TextIO

import numpy as np

from libs.chars import is_any_case_letter, is_number_char


def ans():
    nums = np.array(load_file())
    # go over indices indices in jumps of 3
    possibles1 = get_only_possible_value(nums[0::3])
    possibles2 = get_only_possible_value(nums[1::3])
    possibles3 = get_only_possible_value(nums[2::3])
    # now there should only be 1 possible value for each of them
    nums[0::3] = np.bitwise_xor(nums[0::3], possibles1)
    nums[1::3] = np.bitwise_xor(nums[1::3], possibles2)
    nums[2::3] = np.bitwise_xor(nums[2::3], possibles3)
    return np.sum(nums)


def load_file() -> List[int]:
    """
    :return: input file split by commas, values converted to ints
    """
    with open("files//P059.txt") as f:
        return [int(i) for i in f.read().split(",")]


def check_all_letters(nums: List[int]) -> bool:
    """
    :param nums: a list of numbers
    :return: True if all chars are valid
    """
    for c in nums:
        if not is_wanted_char(chr(c)):
            return False
    return True


def is_wanted_char(c: chr) -> bool:
    """
    :param c: input char
    :return: True if this char is valid
    """
    return is_any_case_letter(c) or is_number_char(c) or c in {" ", ".", ",", "(", ")", "'", '"', ";", "!", "?", "[",
                                                               "]", "/", "+", ":"}


def get_only_possible_value(nums: np.ndarray) -> int:
    for c in range(ord('a'), ord('z') + 1):
        # apply the XOR
        temp = np.bitwise_xor(np.copy(nums), c)
        if check_all_letters(temp):
            return c
