from libs.calculations.general import fibonacci_number_by_index
from libs.calculations.numbers_properties import is_pandigital


def ans():
    curr = 1
    prev = 1
    k = 2
    last_ten_digs = 10 ** 9
    while True:
        prev, curr, k = curr, (prev + curr) % last_ten_digs, k + 1
        if is_pandigital(curr, 9):  # right-most digits
            full_fib_k = fibonacci_number_by_index(k)  # get full number
            if is_pandigital(int(str(full_fib_k)[:9]), 9):  # left-most digits
                return k
