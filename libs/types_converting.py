from typing import List, Union

import numpy as np


def list_to_num(li: List[int]) -> int:
    powers = np.power(10, np.arange(len(li), dtype="int64")[::-1])
    return int(np.dot(powers, li))


def num_to_list(n: int) -> List[int]:
    return list(int(i) for i in str(n))


def string_to_list(s: str) -> List[str]:
    return list(s)


def list_to_string(li: List) -> str:
    return "".join(str(i) for i in li)
