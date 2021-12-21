from collections import defaultdict
from itertools import combinations
from math import sqrt
from typing import List, Dict, Set

from libs.calculations.numbers_properties import is_square
from libs.files import get_file_lines
from libs.types_converting import list_to_string, string_to_list, num_to_list, list_to_num


def ans():
    words_list = get_all_words()
    # get only words that have matching anagram
    anagrams = get_repeated_anagrams(words_list)
    anagrams_pairs = []
    for i in anagrams:
        anagrams_pairs += combinations(i, 2)
    # now handle each order
    result = -1
    for pair in anagrams_pairs:
        result = max(result, max_value_from_pair(pair))
    return result


def get_all_words():
    """
    :return: load words from file, for each word returns a pair (the word sorted,the word)
    """
    words_list = get_file_lines("P098")[0].split(",")
    return [(list_to_string(sorted(string_to_list(i.strip("\"")))), i.strip("\"")) for i in words_list]


def get_repeated_anagrams(words_list):
    """
    :param words_list: a list of words
    :return: a list of repeated anagrams
    """
    anagrams: Dict[str, List[str]] = defaultdict(list)
    for i in words_list:
        anagrams[i[0]].append(i[1])
    return [anagrams[k] for k in anagrams if len(anagrams[k]) > 1]


def max_value_from_pair(p: (str, str)) -> int:
    """
    :param p: a pair of words
    :return: all values gotten from the pair
    """
    result = -1
    w1: str = p[0]
    w2: str = p[1]
    number_of_chars = len(w1)
    for i in range(int(sqrt(10 ** (number_of_chars - 1))) + 1, int(sqrt(10 ** number_of_chars)) + 1):
        # map digits to letters:
        digits = num_to_list(i ** 2)
        # calculate for both sides
        w1w2 = handle_one_side(w1, w2, digits)
        w2w1 = handle_one_side(w2, w1, digits)
        # if we found a result
        if w2w1 != -1 or w1w2 != -1:
            result = max([result, i, w1w2, w2w1])
    return result


def handle_one_side(w1: str, w2: str, digits: List[int]) -> int:
    """
    use w1 to create a number for w2
    :param w1: first word
    :param w2: second word
    :param digits: digits list
    :return: a number found, -1 if not
    """
    letters_values: Dict[str, int] = dict()
    digs_used: Set[int] = set()
    for index, c in enumerate(w1):
        dig = digits[index]
        # now set the value for the letter in c.
        # if there is already a letter with this value, or c already has a value different than dig, break
        if c in letters_values and letters_values[c] != dig:
            return -1
        if c not in letters_values and dig in digs_used:
            return -1
        # else, it is ok
        letters_values[c] = dig
        digs_used.add(dig)
    else:
        # if we did not break, calculate the value for the other word:
        other_word_num_list = [letters_values[c] for c in w2]
        # if it has a leading zero, go to next
        if other_word_num_list[0] == 0:
            return -1
        other_word_num = list_to_num(other_word_num_list)
        if is_square(other_word_num):
            return other_word_num
    return -1
