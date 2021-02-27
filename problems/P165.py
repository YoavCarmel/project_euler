from collections import defaultdict
from typing import List, Optional, Set, Dict, Tuple

from tqdm import tqdm

from libs.calculations import power_set
from objects.geometry import Line, Point, QLine


def ans():
    limit = 5000
    tns = get_all_tns(limit * 4)
    lines = get_lines_list(tns)
    points = get_intersections2(lines, 5)
    return len(points)


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
    result: List[int] = [290797]
    for i in range(limit):
        result.append(next_sn(result[-1]))
    # convert to tns
    for i in range(len(result)):
        result[i] = tn(result[i])
    return result[1:]


def get_lines_list(tns_list) -> List[Line]:
    """
    converts tns list to lines list
    :param tns_list: tns list
    :return: the lines list
    """
    result: List[Line] = list()
    for i in range(0, len(tns_list), 4):
        result.append(QLine(Point(tns_list[i], tns_list[i + 1]), Point(tns_list[i + 2], tns_list[i + 3])))
    return result


def single_true_inter_point(line1: Line, line2: Line) -> Optional[Point]:
    """
    :param line1: input line
    :param line2: input line
    :return: a valid non-end point intersection of the lines. None if does not exist
    """
    p = line1.intersection_point(line2)
    if p is None:
        return None
    if p in {line1.p1, line1.p2, line2.p1, line2.p2}:
        return None
    return p


def get_intersections1(lines: List[Line]) -> Set[Point]:
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


def get_intersections2(lines: List[Line], grid_size) -> Set[Point]:
    """
    :param lines: lines to get true intersections of
    :param grid_size: number of mini squares to split each side (total grid_size^2)
    :return: a set of true intersection points
    """
    points: Set[Point] = set()
    lines_of_segments: Dict[int, Set[Line]] = defaultdict(set)
    segments_of_lines: Dict[Line, Set[int]] = defaultdict(set)
    min_coor = 0
    max_coor = 500
    values = [(max_coor - min_coor) * i // grid_size for i in range(grid_size + 1)]
    rectangles = [(Point(values[i], values[j]), Point(values[i + 1], values[j + 1])) for i in range(grid_size) for j in
                  range(grid_size)]
    for line in lines:
        for i, rectangle in enumerate(rectangles):
            if line.exists_in_rectangle(QLine(rectangle[0], rectangle[1])):
                lines_of_segments[i].add(line)
                segments_of_lines[line].add(i)

    for i1, line1 in tqdm(enumerate(lines)):
        for i2, line2 in enumerate(lines[i1 + 1:]):
            if len(segments_of_lines[line1].intersection(segments_of_lines[line2])) == 0:
                continue
            p = single_true_inter_point(line1, line2)
            if p is not None:
                points.add(p)

    return points


def get_intersections3(lines: List[Line], grid_size) -> Set[Point]:
    """
    :param lines: lines to get true intersections of
    :param grid_size: number of mini squares to split each side (total grid_size^2)
    :return: a set of true intersection points
    """
    points: Set[Point] = set()
    lines_of_segments: Dict[int, Set[Line]] = defaultdict(set)
    segments_of_lines: Dict[Line, Set[int]] = defaultdict(set)
    min_coor = 0
    max_coor = 500
    values = [(max_coor - min_coor) * i // grid_size for i in range(grid_size + 1)]
    rectangles = [(Point(values[i], values[j]), Point(values[i + 1], values[j + 1])) for i in range(grid_size) for j in
                  range(grid_size)]
    for line in lines:
        for i, rectangle in enumerate(rectangles):
            if line.exists_in_rectangle(QLine(rectangle[0], rectangle[1])):
                lines_of_segments[i].add(line)
                segments_of_lines[line].add(i)

    lines_of_segments_power_set: Dict[Tuple[int], Set[Line]] = dict()
    for ps in tqdm(power_set(range(len(rectangles)), with_empty=False, as_iterable=True)):
        lines_of_segments_power_set[ps] = set.union(*[lines_of_segments[grid] for grid in ps])

    checked: Dict[Line, Set[Line]] = dict()
    for line in lines:
        checked[line] = set()

    for line in tqdm(lines):
        segments_of_line = tuple(sorted(segments_of_lines[line]))
        for line2 in lines_of_segments_power_set[segments_of_line].difference(checked[line]):
            checked[line2].add(line)
            p = single_true_inter_point(line, line2)
            if p is not None:
                points.add(p)

    return points
