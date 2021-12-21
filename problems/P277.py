from typing import Optional

from libs.calculations.numbers_properties import is_int


def ans():
    min_start = 10 ** 15
    seq = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
    """
    first step is d, which applies (3 * i + 1) / 2. i must be odd = 2k-1, result is 3k
    second is D, which is ok. result is 9k
    third is U, -> (3 * 9k - 2) / 4 = (27k-2)/4 = 6k+(3k-2)/4. k = 4t+2 -> i = 8t+1. result is 36t+18
    fourth is U, -> (3 * (36t + 18) - 2) / 4 = (108t-52)/4 = 27t-13, ok. result is 27t-13
    fifth is d, -> (3 * (27 - 13t) + 1) / 2 = (82-39t)/2 = 41-19.5t. t must be even, t = 2s. result is 72s+18

    to conclude: i = 2k-1 = 8t+1 = 16s+1
    """
    i = 1
    while True:
        i += 16
        start = apply_sequence_backwards(i, seq)
        if start is None:
            continue
        if start > min_start:
            return start


def get_sequence(number: int) -> str:
    """
    :param number: an input number
    :return: the number's sequence to reach to 1
    """
    seq = ""
    while number != 1:
        if number % 3 == 0:
            seq += "D"
            number = number // 3
        elif number % 3 == 1:
            seq += "U"
            number = (4 * number + 2) // 3
        else:  # number%3==2
            seq += "d"
            number = (2 * number - 1) // 3
    return seq


def apply_sequence_backwards(number: int, sequence: str) -> Optional[int]:
    """
    :param number: a result number
    :param sequence: all steps that were taken
    :return: the origin number
    """
    sequence = sequence[::-1]
    for d in sequence:
        number = apply_step_backwards(number, d)
        if number is None:
            return None
    return number


def apply_step_backwards(number: int, step: str) -> Optional[int]:
    """
    :param number: a result number
    :param step: the step that was taken
    :return: the origin number
    """
    if step == "D":
        return 3 * number
    if step == "U":
        res = (3 * number - 2) / 4
        if is_int(res) and int(res) % 3 == 1:
            return int(res)
    if step == "d":
        res = (3 * number + 1) / 2
        if is_int(res) and int(res) % 3 == 2:
            return int(res)
    return None
