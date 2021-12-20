from collections import defaultdict
from typing import List, Optional, Set, Dict, Tuple, Union

import pytest
from sortedcontainers import SortedList
from tqdm import tqdm

from libs.objects.geometry import Line, Point, QLine

"""
tried 3 solution:
1. using QLine get the exact points
2. using Line get the intersecting lines and then convert to QLine and calc again for these pairs to remove duplicates
3. (deleted) using Line get intersection points, remove points that are too close to each other (just does not work)

both 1 and 2 run in about 60 seconds :(
"""


def ans():
    return solve2(limit=100)


def solve(limit=5000):
    tns = get_all_tns(limit * 4)
    lines = get_lines_list(tns, qline=True)
    points = get_intersections_minmax_constraints(lines, points=True)
    return len(points)


def solve2(limit=5000):
    tns = get_all_tns(limit * 4)
    lines = get_lines_list(tns, qline=False)
    intersections = get_intersections_minmax_constraints(lines, points=False)
    lines_q: Dict[Line, QLine] = {line: QLine(Point(line.p1.x, line.p1.y), Point(line.p2.x, line.p2.y))
                                  for line in lines}
    final_points: Set[Point] = set()
    for pair in tqdm(intersections):
        p = single_true_inter_point(lines_q[pair[0]], lines_q[pair[1]])
        if p is not None:
            final_points.add(p)
    return len(final_points)


@pytest.mark.parametrize("limit, output", [(100, 1112), (500, 29496), (1000, 113849)])
def test1(limit, output):
    assert solve(limit) == output


@pytest.mark.parametrize("limit, output", [(100, 1112), (500, 29496), (1000, 113849)])
def test2(limit, output):
    assert solve2(limit) == output


def next_sn(curr) -> int:
    """
    :param curr: current sn
    :return: s[n+1]
    """
    return (curr * curr) % 50515093


def tn(sn) -> int:
    """
    :param sn: current sn
    :return: tn from sn
    """
    return sn % 500


def get_all_tns(limit) -> List[int]:
    """
    :param limit: max n value
    :return: a list of tn values
    """
    result: List[int] = list()
    sn = 290797
    for i in range(limit):
        sn = next_sn(sn)
        result.append(tn(sn))
    return result


def get_lines_list(tns_list, qline=False) -> List[Line]:
    """
    converts tns list to lines list
    :param tns_list: tns list
    :return: the lines list
    """
    result: List[Line] = list()
    for i in range(0, len(tns_list), 4):
        if qline:
            result.append(QLine(Point(tns_list[i], tns_list[i + 1]), Point(tns_list[i + 2], tns_list[i + 3])))
        else:
            result.append(Line(Point(tns_list[i], tns_list[i + 1]), Point(tns_list[i + 2], tns_list[i + 3])))
    return result


def single_true_inter_point(line1: QLine, line2: QLine, is_qline=True) -> Optional[Point]:
    """
    :param line1: input line
    :param line2: input line
    :return: a valid non-end point intersection of the lines. None if does not exist
    """
    if is_qline:
        p = line1.intersection_point(line2, possible_parallel=False)
    else:
        p = line1.intersection_point(line2)
    if p is None:
        return None
    if p in {line1.p1, line1.p2, line2.p1, line2.p2}:
        return None
    return p


# Naive
def get_intersections_naive(lines: List[QLine]) -> Set[Point]:
    """
    :param lines: lines to get true intersections of
    :return: a set of true intersection points
    """
    points: Set[Point] = set()
    for i1, line1 in tqdm(enumerate(lines)):
        for i2, line2 in enumerate(lines[i1 + 1:]):
            p = single_true_inter_point(line1, line2)
            if p is not None:
                points.add(p)
    return points


# MinMax constraints
def get_intersections_minmax_constraints(lines: List[Line], points: bool) -> Union[Set[Point], Set[Tuple[List, List]]]:
    """

    :param lines: lines to get true intersections of
    :param points: True if want to return points, False if want to return pairs of intersecting lines
    :return: a set of results based on points
    """
    m_dict = get_m_dict(lines)
    max_x = SortedList(lines, key=lambda l: -l.max_x)  # The minus sign is so all slices are done the same direction
    min_x = SortedList(lines, key=lambda l: l.min_x)
    max_y = SortedList(lines, key=lambda l: -l.max_y)  # The minus sign is so all slices are done the same direction
    min_y = SortedList(lines, key=lambda l: l.min_y)
    if points:
        res: Set = set()
    else:
        res: Set = set()
    for i1, line1 in tqdm(enumerate(lines)):
        for i2, line2 in enumerate(
                get_x_fit_lines(line1, lines[i1 + 1:], max_x, min_x, max_y, min_y).difference(m_dict[line1.m])):
            p = single_true_inter_point(line1, line2, is_qline=points)
            if p is not None:
                if points:
                    res.add(p)
                else:
                    res.add((line1, line2))
    return res


def get_x_fit_lines(line, lines_left, max_x, min_x, max_y, min_y):
    max_bigger_than_my_min = QLine(Point(0, 0), Point(line.min_x, line.min_y))  # its max is my min
    min_smaller_than_my_max = QLine(Point(line.max_x, line.max_y), Point(500, 500))  # its min is my max
    l_max_x = max_x[:max_x.bisect_right(max_bigger_than_my_min)]
    l_min_x = min_x[:min_x.bisect_right(min_smaller_than_my_max)]
    l_max_y = max_y[:max_y.bisect_right(max_bigger_than_my_min)]
    l_min_y = min_y[:min_y.bisect_right(min_smaller_than_my_max)]
    # dont use all of the 4. the last 2 remove about 5 lines, better to just calc intersections for them
    # but do use lines_left to prevent repeated calculations!
    groups: List = sorted([l_max_x, l_min_x, l_max_y, l_min_y], key=len)[:2]
    groups.append(lines_left)
    groups.sort(key=len)
    groups[0] = set(groups[0])
    s = set.intersection(*groups)
    return s


def get_m_dict(lines: List[Line]) -> Dict:
    d = defaultdict(set)
    for line in lines:
        d[line.m].add(line)
    return d
