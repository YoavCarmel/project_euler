# using diophantine equations
from typing import Tuple, List, Set


def ans():
    n = 10 ** 9
    sols: List[List[Tuple[int, int]]] = [[(1, 0)]]  # 4 solution paths:
    # first path of 3x^2-2x-1=0: the (x,x,x+1) solution
    while sols[0][-1][0] * 3 + 1 <= 4 * n:
        xn = sols[0][-1][0]
        yn = sols[0][-1][1]
        sols[0].append((-2 * xn - yn + 1, -3 * xn - 2 * yn + 1))
    # second path of 3x^2-2x-1=0: the (x,x,x+1) solution
    sols.append([(1, 0)])
    while sols[1][-1][0] * 3 + 1 <= 4 * n:
        xn = sols[1][-1][0]
        yn = sols[1][-1][1]
        sols[1].append((-2 * xn + yn + 1, 3 * xn - 2 * yn - 1))
    # first path of 3x^2+2x-1=0: the (x,x,x-1) solution
    sols.append([(-1, 0)])
    while sols[2][-1][0] * 3 - 1 <= 4 * n:
        xn = sols[2][-1][0]
        yn = sols[2][-1][1]
        sols[2].append((-2 * xn - yn - 1, -3 * xn - 2 * yn - 1))
    # second path of 3x^2+2x-1=0: the (x,x,x-1) solution
    sols.append([(-1, 0)])
    while sols[3][-1][0] * 3 - 1 <= 4 * n:
        xn = sols[3][-1][0]
        yn = sols[3][-1][1]
        sols[3].append((-2 * xn + yn - 1, 3 * xn - 2 * yn + 1))
    # got all solutions. sum perimeters:
    final_sols: Set[Tuple[int, int, int]] = set()
    for i in sols[:2]:  # (x,x,x+1)
        for j in i:
            if j[0] > 1 and ((j[0] + 1) * j[1]) % 8 == 0:
                final_sols.add((j[0], j[0], j[0] + 1))
    for i in sols[2:]:  # (x,x,x-1)
        for j in i:
            if j[0] > 1 and ((j[0] - 1) * j[1]) % 8 == 0:
                final_sols.add((j[0], j[0], j[0] - 1))
    p_sum = sum([sum(i) for i in final_sols if sum(i) <= n])
    return p_sum
