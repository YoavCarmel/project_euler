import math
from typing import List

from libs.calculations.numbers_properties import is_int


def polygonal_number(num: int, shape: int) -> int:
    # x=(n^2*(s-2)-n*(s-4))/2
    polygon = (num * num * (shape - 2) - num * (shape - 4)) // 2
    return polygon


def is_polygonal_number(num: int, shape: int) -> bool:
    # n=(sqrt(8x(s-2)+(s-4)^2)+s-4)/2
    n = (math.sqrt(8 * num * (shape - 2) + (shape - 4) ** 2) + shape - 4) / (2 * (shape - 2))
    return is_int(n)


def is_any_polygon_number(num: int, polygons: List[int]) -> bool:
    return len(all_polygons_fit_to_number(num, polygons)) != 0


def all_polygons_fit_to_number(num: int, polygons: List[int]) -> List[int]:
    return [i for i in polygons if is_polygonal_number(num, i)]


def all_polygons_of_number(num: int, polygons: List[int]) -> List[int]:
    return [polygonal_number(num, i) for i in polygons]


def triangle_number(n):
    return (n * (n + 1)) // 2
