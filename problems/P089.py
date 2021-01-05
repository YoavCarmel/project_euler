from typing import List

from libs.roman import *


def ans():
    f = open("files//P089.txt")
    nums: List[str] = [i.strip('\n') for i in f.readlines()]  # a list of roman numbers
    count = 0
    for i in nums:
        # add the difference between the number and the optimal form of the number
        count += len(i) - len(int_to_roman(roman_to_int(i)))
    return count
