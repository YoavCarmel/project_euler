from collections import defaultdict
from typing import Dict


def ans():
    """
    we will build the strings iteratively
    """
    n = 30
    days: Dict[int, Dict[int, Dict[int, int]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    days[0][0][0] = 1
    for day in range(1, n + 1):
        yesterday_dict: Dict[int, Dict[int, int]] = days[day - 1]
        today_dict: Dict[int, Dict[int, int]] = days[day]
        # L count = 0
        yesterday_dict_l0: Dict[int, int] = yesterday_dict[0]
        today_dict[0][0] += (yesterday_dict_l0[0] + yesterday_dict_l0[1] + yesterday_dict_l0[2])  # added "on time"
        today_dict[0][1] += yesterday_dict_l0[0]  # added "absent"
        today_dict[0][2] += yesterday_dict_l0[1]  # added "absent"
        today_dict[1][0] += (yesterday_dict_l0[0] + yesterday_dict_l0[1] + yesterday_dict_l0[2])  # added "late"
        # L count = 1
        yesterday_dict_l1: Dict[int, int] = yesterday_dict[1]
        today_dict[1][0] += (yesterday_dict_l1[0] + yesterday_dict_l1[1] + yesterday_dict_l1[2])  # added "on time"
        today_dict[1][1] += yesterday_dict_l1[0]  # added "absent"
        today_dict[1][2] += yesterday_dict_l1[1]  # added "absent"
    return sum([days[n][late][abs_count] for late in [0, 1] for abs_count in [0, 1, 2]])
