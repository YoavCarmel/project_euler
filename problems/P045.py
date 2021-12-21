from math import sqrt

from libs.calculations.numbers_properties import is_int
from libs.calculations.polygon_numbers import polygonal_number


def ans():
    # all hexagon numbers are also triangle numbers
    i: int = 144  # we should find the next after 143
    while True:
        if is_int(hex_and_pent_number(i)):
            return polygonal_number(i, 6)
        i += 1


def hex_and_pent_number(n: int) -> float:
    """
    hexagon number is at form 2n^2-n
    pentagon number is at form (3x^2-x)/2
    index of a pentagon number using the hexagon number:
    (3x^2-x)/2=2n^2-n
    3x^2-x-(4n^2-2n)=0
    x=(1+sqrt(48n^2-24n+1))/6
    """
    return (1 + sqrt(48 * (n ** 2) - 24 * n + 1)) / 6
