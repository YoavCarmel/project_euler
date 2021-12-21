from libs.calculations.numbers_properties import digits_sum


def ans():
    max_sum: int = 0
    power_start: int = 80
    for a in range(100):
        p: int = a ** power_start
        for b in range(power_start, 100):
            p *= a
            max_sum = max(max_sum, digits_sum(p))
    return max_sum
