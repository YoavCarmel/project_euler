from libs.numbers_properties import is_int
from libs.polygon_numbers import polygonal_number
from math import sqrt


def ans():
    for i in range(1, 100000):
        for j in range(1, i):
            if is_int(pent_difference(i, j)) and is_int(pent_sum(i, j)):
                return polygonal_number(pent_difference(i, j), 5)


def pent_difference(i, j):
    """
    pent number look like (3x^2-x)/2
    pent difference looks like (3*(n^2-k^2)-(n-k))/2=(n-k)*(3n+3k-1)/2
    3x^2-x-(3(n^2-k^2)-(n-k))=0
    x=(1+sqrt(1+36n^2-36k^2-12n+12k))/6
    """
    return (1 + sqrt(1 + 36 * (i ** 2) - 36 * (j ** 2) - 12 * i + 12 * j)) / 6


def pent_sum(i, j):
    """
    pent number look like (3x^2-x)/2
    pent difference looks like (3*(n^2+k^2)-(n+k))/2=(n-k)*(3n+3k-1)/2
    3x^2-x-(3(n^2+k^2)-(n+k))=0
    x=(1+sqrt(1+36n^2+36k^2-12k-12k))/6
    """
    return (1 + sqrt(1 + 36 * (i ** 2) + 36 * (j ** 2) - 12 * i - 12 * j)) / 6
