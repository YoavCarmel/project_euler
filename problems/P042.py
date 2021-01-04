from typing import List

from libs.polygon_numbers import is_polygonal_number


def ans():
    count: int = 0
    words: List[str] = words_list()
    for word in words:
        if is_polygonal_number(score(word), 3):
            count += 1
    return count


def words_list() -> List[str]:
    """
    read the file and return the words list
    :return: sorted words list from file
    """
    file_read: str = open("files//P042.txt").read()
    words: List[str] = file_read.split(",")
    for i in range(len(words)):
        words[i] = words[i].strip('"')
    words.sort()
    return words


def score(word: str) -> int:
    """
    :param word: input word
    :return: score by chars
    """
    s: int = 0
    for c in range(len(word)):
        s += ord(word[c]) - 64
    return s
