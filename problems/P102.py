from libs.files import get_file_lines
from objects.geometry import Triangle, Point, Line
from typing import List
from math import inf as infinity


def ans():
    lines = get_file_lines("P102")
    triangles = [create_triangle(line.split(",")) for line in lines]
    count = 0
    for t in triangles:
        if zz_inside_triangle(t):
            count += 1
    return count


def create_triangle(t: List[str]) -> Triangle:
    """
    :param t: a list of 6-n groups, representing coordinates of 3 points
    :return: a triangle from the points
    """
    p1 = Point(int(t[0]), int(t[1]))
    p2 = Point(int(t[2]), int(t[3]))
    p3 = Point(int(t[4]), int(t[5]))
    return Triangle(p1, p2, p3)


def zz_inside_triangle(t: Triangle) -> bool:
    """
    :param t: input triangle
    :return: True if (0,0) inside the triangle
    """
    return one_point_check(t.p1, t.p2, t.p3) and one_point_check(t.p2, t.p1, t.p3) and one_point_check(t.p3, t.p1, t.p2)


def one_point_check(check: Point, o1: Point, o2: Point) -> bool:
    """
    :param check: a base point
    :param o1: other point
    :param o2: other point 2
    :return: True if check if check is on the other side of (0,0) relative to the line o1,o2
    """
    if check.x == 0:
        if check.y == 0:
            return False
        s = Line(o1, o2).slope()
        if s == infinity:
            return False
        y = (-s) * o1.x + o1.y
        if check.y > 0:
            return 0 <= y <= check.y
        else:
            return 0 >= y >= check.y
    # else:
    s = Line(check, Point(0, 0)).slope()
    m = Line(o1, o2).slope()
    if m == infinity:
        y1 = (-(Line(check, o1)).slope()) * check.x + check.y
        y2 = (-(Line(check, o2)).slope()) * check.x + check.y
        return (y2 < 0 < y1) or (y1 < 0 < y2)
    if s == m:
        return False
    # else:
    x = (m * o1.x - o1.y) / (m - s)
    y = s * x
    return min(o1.x, o2.x) < x < max(o1.x, o2.x) and min(o1.y, o2.y) < y < max(o1.y, o2.y)
