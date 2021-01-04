from typing import List, TextIO

from libs.chars import is_any_case_letter, is_number_char


def ans():
    nums: List[int] = load_file()
    # go over indices indices in jumps of 3
    for c1 in range(ord('a'), ord('z') + 1):
        nums_c1 = nums.copy()
        # apply the XOR
        for i in range(0, len(nums), 3):
            nums_c1[i] = nums_c1[i] ^ c1
        # go to next c only if valid
        if not check_all_letters(nums_c1[0::3]):
            continue
        for c2 in range(ord('a'), ord('z') + 1):
            nums_c2 = nums_c1.copy()
            # apply the XOR
            for i in range(1, len(nums), 3):
                nums_c2[i] = nums_c2[i] ^ c2
            # go to next c only if valid
            if not check_all_letters(nums_c2[1::3]):
                continue
            for c3 in range(ord('a'), ord('z') + 1):
                nums_c3 = nums_c2.copy()
                # apply the XOR
                for i in range(2, len(nums), 3):
                    nums_c3[i] = nums_c3[i] ^ c3
                if check_all_letters(nums_c3):
                    # we found a solution
                    return sum(nums_c3)


def load_file() -> List[int]:
    """
    :return: input file split by commas, values converted to ints
    """
    f: TextIO = open("files//P059.txt")
    nums: List[str] = f.read().split(",")
    return [int(i) for i in nums]


def check_all_letters(nums: List[int]) -> bool:
    """
    :param nums: a list of numbers
    :return: True if all chars are valid
    """
    for i in range(len(nums)):
        if not is_wanted_char(chr(nums[i])):
            return False
    return True


def is_wanted_char(c: chr) -> bool:
    """
    :param c: input char
    :return: True if this char is valid
    """
    return is_any_case_letter(c) or c == ' ' or c == '.' or c == ',' or c == '(' or c == ')' or is_number_char(
        c) or c == "'" or c == '"' or c == ';' or c == '!'
