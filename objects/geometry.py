from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Union, NewType
from math import inf

from objects.frac import Frac

EPSILON = 1e-6

Number = NewType("Number", Union[int, float, Frac, None])


class Point:
    def __init__(self, x: Number, y: Number):
        self.x: Number = x
        self.y: Number = y

    def __repr__(self):
        """
        :return: a representation form of the point
        """
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other: Point):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


class Line:
    def __init__(self, p1: Point, p2: Point, should_calc_mb=True):
        self.p1: Point = p1
        self.p2: Point = p2
        self.min_x = min(p1.x, p2.x)
        self.max_x = max(p1.x, p2.x)
        self.min_y = min(p1.y, p2.y)
        self.max_y = max(p1.y, p2.y)
        if should_calc_mb:
            m, b = self.get_mb()
            self.m: float = m
            self.b: float = b

    def get_mb(self) -> (float, float):
        """
        :return: m,b values for the line equation, such that y=mx+b
        """
        if self.p1.x == self.p2.x:
            m = inf
        else:
            m = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        b = (self.p1.y - self.p1.x * m)
        return m, b

    def is_in_y_range(self, y: float):
        """
        :param y: input y value
        :return: True if y is between the min y and max y of the line
        """
        return self.min_y - EPSILON <= y <= self.max_y + EPSILON

    def is_in_x_range(self, x: float):
        """
        :param x: input y value
        :return: True if x is between the min x and max x of the line
        """
        return self.min_x - EPSILON <= x <= self.max_x + EPSILON

    def is_in_range(self, x: float, y: float):
        """
        :param x: input x value
        :param y: input y value
        :return: True if the point represented by (x,y) is in the range of the line
        """
        return self.is_in_x_range(x) and self.is_in_y_range(y)

    def contains_point(self, p: Point):
        """
        :param p: a point
        :return: True if the point is on the line
        """
        if not self.is_in_range(p.x, p.y):
            return False
        if self.m == inf:
            return True
        return p.y == self.m * p.x + self.b

    def is_intersecting(self, other: Line) -> bool:
        """
        :param other: another line
        :return: True if the lines intersect
        """
        if self.m == other.m:
            # they are parallel, so they are either no connected at all, or have a certain overlap
            return self.contains_point(other.p1) or self.contains_point(other.p2) \
                   or other.contains_point(self.p1) or other.contains_point(self.p2)
        # else, they are not parallel, they either intersect in a single point, or do not intersect
        # if self is parallel to the y axis. we know other is for sure not, because they are not parallel
        if self.m == inf:
            # get the y of the other line at the x value of the inf line
            line1_x = self.p1.x
            inter_y = other.m * line1_x + other.b
            return self.is_in_range(line1_x, inter_y) and other.is_in_range(line1_x, inter_y)
        # if other is parallel to the y axis. we know self is for sure not, because they are not parallel
        elif other.m == inf:
            # get the y of the other line at the x value of the inf line
            line2_x = other.p1.x
            inter_y = self.m * line2_x + self.b
            return self.is_in_range(line2_x, inter_y) and other.is_in_range(line2_x, inter_y)
        # calculate the x,y of the intersection based on the known formula, but the point may be anywhere in the grid
        inter_x: float = (other.b - self.b) / (self.m - other.m)
        inter_y: float = self.m * inter_x + self.b
        # return True if the point of intersection is exactly on the line cuts that are self and other
        return self.is_in_range(inter_x, inter_y) and other.is_in_range(inter_x, inter_y)

    def is_self_infinite_line_intersecting(self, other: Line) -> bool:
        """
        returns True if there is intersection when self is extended to infinity,
        other stays the same with limits on both sides
        :param other: other Line
        """
        if self.m == other.m:
            return self.b == other.b
        # else, they are not parallel, they either intersect in a single point, or do not intersect
        if self.m == inf:
            # True if other has a value in self's x
            self_x = self.p1.x
            return other.is_in_x_range(self_x)
        # if other is parallel to the y axis. we know self is for sure not, because they are not parallel
        elif other.m == inf:
            # True if self's y value at other's x is in other's y range
            other_x = other.p1.x
            inter_y = self.m * other_x + self.b
            return other.is_in_y_range(inter_y)
        # calculate the x,y of the intersection based on the known formula, but the point may be anywhere in the grid
        inter_x: float = (other.b - self.b) / (self.m - other.m)
        inter_y: float = self.m * inter_x + self.b
        # return True if the point of intersection is exactly on the line cut of other
        return other.is_in_range(inter_x, inter_y)

    def intersection_point(self, other: Line) -> Optional[Point]:
        """
        intersecting point between lines.
        uses the code od intersection check for speed-up: if we called the is_intersecting func
        we would calculate basically the same thing twice
        :param other: other line
        :return: intersecting point of the lines. None if no intersection
        """
        if self.m == other.m:
            if self.b == other.b:
                return None
            if self.p1 in {other.p1, other.p2}:
                return self.p1
            if self.p2 in {other.p1, other.p2}:
                return self.p2
            return None
        # else, they are not parallel, they either intersect in a single point, or do not intersect
        # if self is parallel to the y axis. we know other is for sure not, because they are not parallel
        if self.m == inf:
            # get the y of the other line at the x value of the inf line
            line1_x = self.p1.x
            inter_y = other.m * line1_x + other.b
            if self.is_in_range(line1_x, inter_y) and other.is_in_range(line1_x, inter_y):
                return Point(line1_x, inter_y)
            return None
        # if other is parallel to the y axis. we know self is for sure not, because they are not parallel
        elif other.m == inf:
            # get the y of the other line at the x value of the inf line
            line2_x = other.p1.x
            inter_y = self.m * line2_x + self.b
            if self.is_in_range(line2_x, inter_y) and other.is_in_range(line2_x, inter_y):
                return Point(line2_x, inter_y)
            return None
        # calculate the x,y of the intersection based on the known formula, but the point may be anywhere in the grid
        inter_x: float = (other.b - self.b) / (self.m - other.m)
        inter_y: float = self.m * inter_x + self.b
        # return True if the point of intersection is exactly on the line cuts that are self and other
        if self.is_in_range(inter_x, inter_y) and other.is_in_range(inter_x, inter_y):
            return Point(inter_x, inter_y)
        return None

    def __repr__(self):
        return repr(self.p1) + "<->" + repr(self.p2)

    def exists_in_rectangle(self, diag: QLine) -> bool:
        # if the infinite line does not intersect with the rectangle at all, no need to further check
        rec_sides = [
            QLine(Point(diag.min_x, diag.min_y), Point(diag.min_x, diag.max_y)),
            QLine(Point(diag.min_x, diag.min_y), Point(diag.max_x, diag.min_y)),
            QLine(Point(diag.max_x, diag.max_y), Point(diag.min_x, diag.max_y)),
            QLine(Point(diag.max_x, diag.max_y), Point(diag.max_x, diag.min_y))
        ]
        for side in rec_sides:
            if self.is_self_infinite_line_intersecting(side):
                break
        else:
            return False
        # if it does, we need to check if the non-infinite line is in the ranges of the rectangle
        if self.max_x < diag.min_x or self.min_x > diag.max_x or self.max_y < diag.min_y or self.min_y > diag.max_y:
            # for sure outside of ranges
            return False
        # else, it must at some point have a real intersection with the rectangle,
        # since the infinite line intersects the rectangle, and the line exists in the rectangle's range -
        # which must be where the intersection is
        return True


class QLine(Line):
    """
    line with rational m,b
    """

    def __init__(self, p1: Point, p2: Point):
        super().__init__(p1, p2, should_calc_mb=False)
        self.p1 = Point(Frac(p1.x), Frac(p1.y))
        self.p2 = Point(Frac(p2.x), Frac(p2.y))
        m, b = self.get_mb()
        self.m: Frac = m
        self.b: Frac = b

    def is_in_y_range(self, y: Number):
        """
        :param y: input y value
        :return: True if y is between the min y and max y of the line
        """
        return self.min_y <= y <= self.max_y

    def is_in_x_range(self, x: Number):
        """
        :param x: input y value
        :return: True if x is between the min x and max x of the line
        """
        return self.min_x <= x <= self.max_x


@dataclass(init=True, repr=True)
class Triangle:
    p1: Point
    p2: Point
    p3: Point
