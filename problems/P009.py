import math


def ans():
    target = 1000
    for a in range(1, target // 2 + 1):
        for b in range(1, a):
            c = math.sqrt(a * a + b * b)
            if a + b + c == target:
                return int(a * b * c)
