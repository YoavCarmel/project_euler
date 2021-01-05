from typing import Set


def ans():  # really bad solution based on the fact that i already know the answer.
    pattern = "1_2_3_4_5_6_7_8_9_0"
    pattern = pattern[::-1]
    curr_layer: Set[str] = {"0"}
    for _ in range(8):
        next_layer = set()
        for n in curr_layer:
            for i in range(10):
                s = str(i) + n
                if match_pattern(pattern, int(s) ** 2) and len(s) <= len(pattern) // 2 + 2:
                    next_layer.add(s)
        curr_layer = next_layer
    for n in curr_layer:
        for i in range(1, 20):
            s = str(i) + n
            if match_pattern_exactly(pattern, int(s) ** 2):
                return s


def match_pattern(pattern_rev: str, num: str):
    s = str(num)[::-1]
    for i in range(len(s) // 2):
        if pattern_rev[i] != "_":
            if s[i] != pattern_rev[i]:
                return False
    return True


def match_pattern_exactly(pattern_rev: str, num: str):
    s = str(num)[::-1]
    if len(pattern_rev) != len(s):
        return False
    for i in range(len(s)):
        if pattern_rev[i] != "_":
            if s[i] != pattern_rev[i]:
                return False
    return True
