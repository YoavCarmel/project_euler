from typing import List

import numpy as np


def list_to_num(li: List[int]) -> int:
    return int("".join(map(str, li)))


def num_to_list(n: int) -> List[int]:
    return list(map(int, str(n)))


def string_to_list(s: str) -> List[str]:
    return list(s)


def list_to_string(li: List) -> str:
    return "".join(map(str, li))
