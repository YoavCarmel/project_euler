from collections import Counter
from typing import Union, Dict, Collection

import gmpy2 as gmpy2

from libs.types_converting import num_to_list


def is_int(x: Union[int, float]) -> bool:
    return isinstance(x, int) or (isinstance(x, float) and x.is_integer())


def is_square(x: int) -> bool:
    return gmpy2.is_square(x)


def num_size(x: int) -> int:
    return len(str(x))


def is_pandigital(x: int, digits: int) -> bool:
    if num_size(x) != digits:
        return False
    digits_set = set(range(1, digits + 1))
    if digits == 10:
        digits_set.remove(10)
        digits_set.add(0)
    return set(num_to_list(x)) == digits_set


def all_same_digits(x: int):
    return len(set(num_to_list(x))) == 1


def contains_any_of_digits(x: int, digits: Collection) -> bool:
    return len(set(num_to_list(x)).intersection(digits)) != 0


def contains_all_of_digits(x: int, digits: Collection) -> bool:
    return set(digits) <= set(num_to_list(x))


def digs_count(x: int) -> Dict[int, int]:
    return Counter(num_to_list(x))


def same_digits(x: int, y: int) -> bool:
    return digs_count(x) == digs_count(y)
