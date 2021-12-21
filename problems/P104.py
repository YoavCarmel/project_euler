from libs.calculations.numbers_properties import is_pandigital
from libs.calculations.general import fibonacci_number_by_index


def ans():
    curr = 1
    prev = 1
    k = 3
    last_ten_digs = 10 ** 9
    while True:
        # work only on small numbers
        prev, curr = curr, (prev + curr) % last_ten_digs
        if is_pandigital(curr, 9):
            full_fib_k = fibonacci_number_by_index(k)  # get full number
            if is_pandigital(curr, 9) and is_pandigital(int(str(full_fib_k)[:9]), 9):
                return k
        k += 1
