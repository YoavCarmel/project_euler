import math


def ans():
    wanted_number_of_rectangles = 2 * 10 ** 6
    m = good_mat(wanted_number_of_rectangles)
    # find the closest to 2 million
    closest = None
    for i in range(len(m)):
        for j in range(len(m[i])):
            if closest is None:
                closest = (i, j)
            else:
                if abs(m[closest[0]][closest[1]] - wanted_number_of_rectangles) > abs(
                        m[i][j] - wanted_number_of_rectangles):
                    closest = (i, j)
    return closest[0] * closest[1]


def calc(r, c):
    return r * c * (r + 1) * (c + 1) // 4


def bad_mat(wanted_number_of_rectangles):
    """
    calc diagonals until all diagonal values are biggest than wanted_number_of_rectangles
    """
    m = [[0]]
    d = 1
    # calc grid with solution
    while True:
        m.append([0])
        diag_min = math.inf
        for k in range(1, d):
            t = calc(k, d - k)
            diag_min = min(t, diag_min)
            m[k].append(t)
        if diag_min > wanted_number_of_rectangles and diag_min != math.inf:
            break
        d += 1
    return m


def good_mat(wanted_number_of_rectangles):
    """
    calc each line until it exceeds wanted_number_of_rectangles
    """
    m = [[0]]
    d = 1
    while len(m[-1]) > 2 or len(m) == 1:
        dd = d * (d + 1) // 2
        m.append([0, dd])
        while m[-1][-1] < wanted_number_of_rectangles:
            m[-1].append(m[-1][-1] + m[-1][1] * len(m[-1]))
        d += 1
    return m
