from typing import List

from libs.types_converting import list_to_num


def ans():
    digs_limit = 100
    return smart_calc(digs_limit)


def brute_find_all(digs_limit):
    all_non_bouncy = []

    def non_bouncy_generator(going_up, curr_list):
        if len(curr_list) == digs_limit:
            all_non_bouncy.append(list_to_num(curr_list))
        else:
            if len(curr_list) == 0:
                for i in range(10):
                    non_bouncy_generator(going_up, curr_list + [i])
            else:
                if going_up:
                    for i in range(curr_list[-1], 10):
                        non_bouncy_generator(going_up, curr_list + [i])
                else:
                    if sum(curr_list) == 0:
                        for i in range(10):
                            non_bouncy_generator(going_up, curr_list + [i])
                    else:
                        for i in range(0, curr_list[-1] + 1):
                            non_bouncy_generator(going_up, curr_list + [i])

    non_bouncy_generator(False, [])
    non_bouncy_generator(True, [])
    all_non_bouncy = list(set(all_non_bouncy))
    all_non_bouncy.remove(0)
    return len(all_non_bouncy)


def smart_calc(digs_limit):
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
