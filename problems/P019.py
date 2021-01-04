from typing import List


def ans():
    # from 1.1.1901 to 31.12.2000
    # 1.1.1901 was tuesday
    months: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_leap: List[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day: int = 2  # 1 to 7, first is 3, will be added on first day
    count: int = 0
    # loop on years and months
    for year in range(1901, 2001):
        for m in range(12):
            # split by leap year or not
            if year % 4 != 0:
                for d in range(months[m]):
                    day = (day + 1) % 7
                    if d == 0 and day == 1:
                        count += 1
            else:
                for d in range(months_leap[m]):
                    day = (day + 1) % 7
                    if d == 0 and day == 1:
                        count += 1
    return count
