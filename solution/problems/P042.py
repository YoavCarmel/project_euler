from solution.libs.polygon_numbers import is_polygonal_number


def ans():
    count = 0
    words = words_list()
    for word in words:
        if is_polygonal_number(score(word),3):
            count += 1
    return count


def words_list():
    l=open("files//P042.txt").read()
    words=l.split(",")
    for i in range(len(words)):
         words[i] = words[i].strip('"')
    words.sort()
    return words


def score(word):
    s = 0
    for c in range(len(word)):
        s += ord(word[c]) - 64
    return s
