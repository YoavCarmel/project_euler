from typing import List


def ans():
    digs_limit = 100
    details_list: List[List[(List[int], List[int])]] = []
    # detail is number of numbers with this number of digits with this left digit that go up(0)/down(1)
    n = 1
    while n <= digs_limit:
        details_list.append([[], []])
        if n == 1:
            for i in range(1, 10):
                details_list[-1][0].append(1)
                details_list[-1][1].append(1)
        else:
            for i in range(1, 10):
                details_list[-1][0].append(sum(k for k in details_list[-2][0][i - 1:]))
                details_list[-1][1].append(sum(k for k in details_list[-2][1][:i]) + 1)
        n += 1
    return sum(k for n in range(digs_limit) for i in [0, 1] for k in details_list[n][i]) - digs_limit * 9
