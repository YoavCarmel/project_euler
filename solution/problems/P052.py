from solution.libs.numbers_properties import same_digits


def ans():
    i = 1
    while True:
        if res(i):
            return i
        i += 1


def res(x):
    return same_digits(x, 2 * x) and same_digits(x, 3 * x) and same_digits(x, 4 * x) and \
           same_digits(x, 5 * x) and same_digits(x, 6 * x)
