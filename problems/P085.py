from typing import List


def ans():
    wanted_number_of_rectangles = 2 * 10 ** 6
    m: List[List[int]] = good_mat(wanted_number_of_rectangles)
    # find the closest to 2 million
    closest: (int, int) = (0, 0)
    for i in range(len(m)):
        for j in range(len(m[i])):
            # if got a number closer to wanted_number_of_rectangles
            if abs(m[closest[0]][closest[1]] - wanted_number_of_rectangles) > abs(
                    m[i][j] - wanted_number_of_rectangles):
                closest = (i, j)
    return closest[0] * closest[1]


def good_mat(wanted_number_of_rectangles: int) -> List[List[int]]:
    """
    calc each line until it exceeds wanted_number_of_rectangles.
    m[i][j] is number of triangles in a box of size ixj
    """
    m: List[List[int]] = [[0]]
    d = 1
    while len(m[-1]) > 2 or len(m) == 1:
        dd = d * (d + 1) // 2
        m.append([0, dd])
        while m[-1][-1] < wanted_number_of_rectangles:
            m[-1].append(m[-1][-1] + m[-1][1] * len(m[-1]))
        d += 1
    return m
