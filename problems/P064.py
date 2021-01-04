from libs.calculations import continued_fraction_of_sqrt


def ans():
    count = 0
    for i in range(10001):
        if len(continued_fraction_of_sqrt(i)) % 2 == 1:
            count += 1
    return count
