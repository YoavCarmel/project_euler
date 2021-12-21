from typing import Dict, List

from sympy import isprime

from libs.calculations.numbers_operations import replace_digits
from libs.calculations.numbers_properties import num_size
from libs.types_converting import num_to_list


def ans():
    wanted_family_size: int = 8
    i: int = 11  # starting number to calc
    comb: List[List[int]] = [[0]]  # starting value for power set
    primes_checked: Dict[int, bool] = dict()  # primes/non primes dict
    valid_units_digs: Dict[int, int] = {1: 3, 3: 7, 7: 9, 9: 11}  # only valid units digits, each dig point to the next
    while True:
        for digits in comb:  # for each subset of the digits indices
            if need_check(i, digits):  # if this is the smallest number possible
                if family_size(i, digits, wanted_family_size, primes_checked) == wanted_family_size:
                    # we found a solution
                    return first_prime_in_family(i, digits, primes_checked)
        # increment i to the next number with a valid units digit
        temp: int = i
        i = (i - i % 10) + valid_units_digs[i % 10]
        if num_size(i) > num_size(temp):  # if i is now a digit longer
            # extend the power set
            comb = sum([[c, c + [num_size(i) - 2]] for c in comb], [[num_size(i) - 2]])


def family_size(num: int, digits: List[int], wanted: int, primes_checked: Dict[int, bool]):
    """
    get family size from starting number num, replacing the indices in digits
    :param num: starting number
    :param digits: indices of digits to replace
    :param wanted: the wanted family size, for optimization
    :param primes_checked: primes/non primes dict
    :return: 0 if family size is smaller than wanted, else return the size of the family
    """
    count = 0
    for i in range(10):
        # go over possible digits to place
        if i == 0:
            if 0 not in digits:
                # then 0 is valid
                if is_prime_check(replace_digits(num, digits, i), primes_checked):
                    count += 1
        else:
            if is_prime_check(replace_digits(num, digits, i), primes_checked):
                count += 1

        if (wanted - count) > (9 - i):
            # not possible to reach the wanted, dont waste time
            return 0
    return count


def first_prime_in_family(num: int, digits: List[int], primes_checked: Dict[int, bool]):
    """
    get first prime of the family
    :param num: num in the family
    :param digits: digits to replace
    :param primes_checked: primes/non primes dict
    :return: the first prime in the family
    """
    for i in range(10):
        # i is the current min valid dig for the family
        if i == 0:
            if 0 not in digits:
                # the 0 is valid
                if is_prime_check(replace_digits(num, digits, i), primes_checked):
                    return replace_digits(num, digits, i)
        else:
            if is_prime_check(replace_digits(num, digits, i), primes_checked):
                return replace_digits(num, digits, i)


def need_check(num: int, digits: List[int]) -> bool:
    """
    check if this is the min number of this family.
    we want the min value for each digit: the left digit must be 1, all others must be 0
    :param num: num to check
    :param digits: digits of family
    :return: True if valid
    """
    ntl: List[int] = num_to_list(num)
    for i in digits:
        if i == 0:
            if ntl[0] != 1:
                return False
        else:
            if ntl[i] != 0:
                return False
    return True


def is_prime_check(n: int, primes_checked: Dict[int, bool]):
    """
    smart prime check to prevent repeated calculations
    :param n: the number to check if prime
    :param primes_checked: all of the already checked numbers
    :return: True if n is prime
    """
    if n in primes_checked:
        return primes_checked[n]
    if isprime(n):
        primes_checked[n] = True
        return True
    primes_checked[n] = False
    return False
