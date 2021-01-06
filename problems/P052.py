from libs.numbers_properties import same_digits


def ans():
    number_of_digits: int = 1
    while True:
        # divide by 6, because numbers above it will have more digit after being multiplied by 6
        for i in range(10 ** number_of_digits, int(10 ** (number_of_digits + 1) / 6) + 1):
            if is_result(i):
                return i
        number_of_digits += 1


def is_result(x: int) -> bool:
    """
    :param x: input number
    :return: True if it is the answer
    """
    return same_digits(x, 2 * x) and same_digits(x, 3 * x) and same_digits(x, 4 * x) and \
           same_digits(x, 5 * x) and same_digits(x, 6 * x)
