from typing import List


def ans():
    text: List[str] = load_text()
    s = 0
    # calculate the score relative to the index
    for i in range(len(text)):
        s += (i + 1) * score(text[i])
    return s


def load_text() -> List[str]:
    """
    load the text from the file
    """
    line: str = open("files//P022.txt").read()
    names: List[str] = [i.strip('"') for i in line.split(",")]
    names.sort()
    return names


def score(name: str) -> int:
    """
    :param name: input name
    :return: the score of the name
    """
    s: int = 0
    for c in range(len(name)):
        s += ord(name[c]) - 64
    return s
