from solution.libs.numbers_operations import reverse_num
from solution.libs.numbers_properties import is_palindrome


def ans():
    count = 0
    for i in range(10000):
        if is_lychrel_number(i):
            count += 1
    return count


def is_lychrel_number(x: int) -> int:
    for i in range(50):
        x = x + reverse_num(x)
        if is_palindrome(x):
            return False
    return True  # for number below 10,000