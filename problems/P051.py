from sympy import isprime

from libs.numbers_operations import replace_digits
from libs.numbers_properties import num_size
from libs.types_converting import num_to_list


def ans():
    wanted_family_size = 8
    i = 11
    comb = combinations(2)
    while True:
        for digits in comb:
            if need_check(i, digits):
                if family_size(i, digits, wanted_family_size) == wanted_family_size:
                    return first_prime_in_family(i, digits)
        temp = i
        i = (i - i % 10) + next_units_dig(i % 10)
        if num_size(i) > num_size(temp):
            comb = combinations(num_size(i))


def family_size(num, digits, wanted):
    count = 0
    for i in range(10):
        if i == 0:
            if 0 not in digits:
                if isprime(replace_digits(num, digits, i)):
                    count += 1
        else:
            if isprime(replace_digits(num, digits, i)):
                count += 1

        if (wanted - count) > (9 - i):
            # break out
            return 0
    return count


def print_family(num, digits):
    for i in range(10):
        if i == 0:
            if 0 not in digits:
                if isprime(replace_digits(num, digits, i)):
                    print(replace_digits(num, digits, i))
        else:
            if isprime(replace_digits(num, digits, i)):
                print(replace_digits(num, digits, i))


def first_prime_in_family(num, digits):
    for i in range(10):
        if i == 0:
            if 0 not in digits:
                if isprime(replace_digits(num, digits, i)):
                    return replace_digits(num, digits, i)
        else:
            if isprime(replace_digits(num, digits, i)):
                return replace_digits(num, digits, i)


def combinations(size):
    all = []

    def add_combination(i, curr):
        if i == size - 1:
            # dont combination the units digit
            if len(curr) != 0:
                all.append(curr)
        else:
            add_combination(i + 1, curr.copy())
            curr.append(i)
            add_combination(i + 1, curr.copy())

    add_combination(0, [])
    return all


def next_units_dig(i):
    if i == 1:
        return 3
    if i == 3:
        return 7
    if i == 7:
        return 9
    if i == 9:
        return 11


def need_check(num, digits):
    for i in digits:
        if i == 0:
            if num_to_list(num)[0] != 1:
                return False
        else:
            if num_to_list(num)[i] != 0:
                return False
    return True
