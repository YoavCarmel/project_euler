from typing import NamedTuple
from math import inf as infinity


class Point(NamedTuple):
    x: int
    y: int


class Triangle(NamedTuple):
    p1: Point
    p2: Point
    p3: Point


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1: Point = p1
        self.p2: Point = p2

    def slope(self) -> float:
        if self.p1.x == self.p2.x:
            return infinity
        else:
            return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
