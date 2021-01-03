from typing import List, Union


def list_to_num(li: List[Union[str, int]]) -> int:
    return int("".join([str(i) for i in li]))


def num_to_list(n: int) -> List[int]:
    return list([int(i) for i in str(n)])


def string_to_list(s: str) -> List:
    return [i for i in s]


def list_to_string(li: List) -> str:
    return "".join([str(i) for i in li])
