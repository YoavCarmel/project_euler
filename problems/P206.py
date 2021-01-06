from typing import Set


def ans():
    pattern = "1_2_3_4_5_6_7_8_9_0"
    pattern = pattern[::-1]
    # only the first i digits of n affect the first i digits of n**2.
    # first digit must be 0, but then add 2 digits each time and see if matcehs the next number in pattern
    possible_n: Set[int] = set()
    possible_n.add(0)
    level = 1
    while True:
        # continue addign numbers that match
        next_level: Set[int] = set()
        for n in possible_n:
            for i in range(1, 100):
                # add the digits to the left
                new_n = n + i * (10 ** (2 * level - 1))
                new_n_squared_str_reversed = str(new_n ** 2)[::-1]
                if len(new_n_squared_str_reversed) > len(pattern):
                    # do not continue with bigger numbers
                    break
                if matches_pattern(pattern, new_n_squared_str_reversed, level):
                    # if after the addition it still matches the pattern, add to next level
                    next_level.add(new_n)
                if perfect_match(pattern, new_n_squared_str_reversed):
                    # if perfect match, return. we got the answer
                    return new_n
        possible_n = next_level
        level += 1


def matches_pattern(pat: str, num: str, level: int):
    """
    :param pat: pattern to match
    :param num: the num to check if matches
    :param level: number of levels in pattern to match
    :return: True if num matches pattern for this level
    """
    for i in range(0, level * 2 + 1, 2):
        if pat[i] != num[i]:
            return False
    return True


def perfect_match(pat: str, num: str):
    """
    :param pat: a pattern to match
    :param num: a number to check if matches
    :return: True if the number matches completely the pattern, and this is the result of the problem
    """
    if len(num) != len(pat):
        return False
    for i in range(0, len(pat) + 1, 2):
        if pat[i] != num[i]:
            return False
    return True
