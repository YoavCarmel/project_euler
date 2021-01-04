from typing import List


def ans():
    one_thousand: int = 3 + 8
    hundred_and: int = 7 + 3
    hundred: int = 7
    ten: int = 3
    ones: List[int] = [3, 3, 5, 4, 4, 3, 5, 5, 4]
    tens: List[int] = [6, 6, 5, 5, 5, 7, 6, 6]
    eleven_to_nineteen: int = 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
    s1to99: int = 9 * sum(ones) + 10 * sum(tens) + eleven_to_nineteen + ten
    s: int = 100 * sum(ones) + 10 * s1to99 + 9 * hundred + 891 * hundred_and + one_thousand
    return s
