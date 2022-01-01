from typing import Tuple, Set

from tqdm import trange

Point = Tuple[int,int]


def ans():
    n = 50
    return naive(n)


def naive(n):
    sols: Set[Tuple[Point, Point]] = set()
    for x1 in trange(0, n + 1):
        # set x2>=x1, without loss of generality
        for x2 in range(x1, n + 1):
            for y1 in range(1, n + 1):
                # can be improved as there are only 4 y2 possible values for each (x1,y1,x2)
                # but i dont want to spend time on this
                for y2 in range(0, n + 1):
                    if right_angle(x1, y1, x2, y2):
                        sols.add(((x1, y1), (x2, y2)))
    return len(sols)


def right_angle(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    gets two points
    :return: True if the two points together with (0,0) create a right angle triangle
    """
    if y1 * x2 == y2 * x1:  # on same line
        return False
    a_s = x1 ** 2 + y1 ** 2
    b_s = x2 ** 2 + y2 ** 2
    c_s = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return a_s + b_s == c_s or a_s + c_s == b_s or b_s + c_s == a_s
