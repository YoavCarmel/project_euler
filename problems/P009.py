import math


def ans():
    target: int = 1000
    # for each a,b in this range, calculate the matching c and check if sum is target
    for a in range(1, target // 2 + 1):
        for b in range(1, a):
            c = math.sqrt(a * a + b * b)
            if a + b + c == target:
                return int(a * b * c)
