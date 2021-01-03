from typing import List

from libs.types_converting import num_to_list, list_to_num


def replace_digits(num: int, digits_places: List[int], new_digit: int) -> int:
    s = num_to_list(num)
    for i in digits_places:
        s[i] = new_digit
    return list_to_num(s)


def reverse_num(x: int) -> int:
    return int(str(x)[::-1])


def concat_nums(x: int, y: int) -> int:
    return int(str(x) + str(y))


def add_digit_to_left(num: int, dig: int) -> int:
    return int(str(dig) + str(num))
