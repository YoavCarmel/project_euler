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

    def slope(self) -> float:
        if self.p1.x == self.p2.x:
            return infinity
        else:
            return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
