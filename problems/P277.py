from typing import Union

from libs.numbers_properties import is_int


def ans():
    min_start = 10 ** 15
    seq = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
    i = 0
    while True:
        i += 1
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


def apply_sequence_backwards(number: int, sequence: str) -> Union[int, None]:
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


def apply_step_backwards(number: int, step: str) -> Union[int, None]:
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
        res = (3 * number + 1) // 2
        if is_int(res) and int(res) % 3 == 2:
            return int(res)
    return None
