from solution.libs.roman import *


def ans():
    f = open("files//P089.txt")
    nums = [i.strip('\n') for i in f.readlines()]
    count = 0
    for i in nums:
        count += len(i) - len(int_to_roman(roman_to_int(i)))
    return count
