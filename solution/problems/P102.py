from collections import namedtuple

from solution.libs.files import get_file_lines
from typing import NamedTuple
from math import inf as infinity


class Point(NamedTuple):
    x: int
    y: int


class Triangle(NamedTuple):
    p1: Point
    p2: Point
    p3: Point


class Line(NamedTuple):
    p1: Point
    p2: Point


def ans():
    lines = get_file_lines("P102")
    triangles = [create_triangle(l.split(",")) for l in lines]
    count = 0
    for t in triangles:
        if zz_inside_triangle(t):
            count += 1
    return count


def create_triangle(t):
    p1 = Point(int(t[0]), int(t[1]))
    p2 = Point(int(t[2]), int(t[3]))
    p3 = Point(int(t[4]), int(t[5]))
    return Triangle(p1, p2, p3)


def slope(l: Line):
    if l.p1.x == l.p2.x:
        return infinity
    else:
        return (l.p1.y - l.p2.y) / (l.p1.x - l.p2.x)


def lines_cross(l1: Line, l2: Line):  # not finished
    if slope(l1) == slope(l2) == infinity:
        if l1.p1.x != l2.p1.x:
            return False


def zz_inside_triangle(t: Triangle):
    def one_point_check(check: Point, o1: Point, o2: Point):
        if check.x == 0:
            if check.y == 0:
                return False
            s = slope(Line(o1, o2))
            if s == infinity:
                return False
            y = (-s) * o1.x + o1.y
            if check.y > 0:
                return y >= 0 and y <= check.y
            else:
                return y <= 0 and y >= check.y
        # else:
        s = slope(Line(check, Point(0, 0)))
        m = slope(Line(o1, o2))
        if m == infinity:
            y1 = (-slope(Line(check, o1))) * check.x + check.y
            y2 = (-slope(Line(check, o2))) * check.x + check.y
            return (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0)
        if s == m:
            return False
        # else:
        x = (m * o1.x - o1.y) / (m - s)
        y = s * x
        return x > min(o1.x, o2.x) and x < max(o1.x, o2.x) and y > min(o1.y, o2.y) and y < max(o1.y, o2.y)

    return one_point_check(t.p1, t.p2, t.p3) and one_point_check(t.p2, t.p1, t.p3) and one_point_check(t.p3, t.p1, t.p2)
