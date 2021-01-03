import math
from collections import defaultdict
from typing import Union, List, Dict, Collection

from sympy import factorint

from libs.types_converting import num_to_list


def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


def is_int(x: Union[int, float]) -> bool:
    return type(x) is int or (type(x) is float and float(x).is_integer())


def is_square(x: Union[int, float]) -> bool:
    return math.sqrt(x).is_integer()


def num_size(x: int) -> int:
    return len(str(x))


def digits_sum(x: int) -> int:
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def is_pandigital(x: int, digits: int) -> bool:
    if num_size(x) != digits:
        return False
    digits = set([i for i in range(1, digits + 1)])
    if digits == 10:
        digits.remove(10)
        digits.add(0)
    return set(num_to_list(x)) == digits


def all_same_digits(x: int):
    num_list = num_to_list(x)
    for d in num_list:
        if d != num_list[0]:
            return False
    return True


def contains_digits(x: int, digits: Collection) -> bool:
    return len(set(num_to_list(x)).intersection(digits)) != 0


def digs_count(x: int) -> Dict[int, int]:
    x_dict = defaultdict(int)
    for d in num_to_list(x):
        x_dict[d] += 1
    return x_dict


def same_digits(x: int, y: int) -> bool:
    x = str(x)
    y = str(y)
    if len(x) != len(y):
        return False
    x_dict = defaultdict(int)
    y_dict = defaultdict(int)
    for i in x:
        x_dict[i] += 1
    for i in y:
        if i not in x_dict:
            return False
        y_dict[i] += 1
    return x_dict == y_dict


def co_primes(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1


def lcm_list(nums: List[int]) -> int:
    factors = dict()
    for i in nums:
        i_factors = factorint(i)
        for k in i_factors:
            if k in factors:
                factors[k] = max(factors[k], i_factors[k])
            else:
                factors[k] = i_factors[k]
    p = 1
    for k in factors:
        p *= (k ** factors[k])
    return p
