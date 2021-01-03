from libs.numbers_properties import digits_sum


def ans():
    max_sum = 0
    for a in range(100):
        for b in range(100):
            p = a ** b
            max_sum = max(max_sum, digits_sum(p))
    return max_sum
