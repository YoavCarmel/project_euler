def ans():
    text = load_text()
    s = 0
    for i in range(len(text)):
        s += (i + 1) * score(text[i])
    return s


def load_text():
    line = open("files//P022.txt").read()
    names = line.split(",")
    for i in range(len(names)):
        names[i] = names[i].strip('"')
    names.sort()
    return names


def score(name):
    s = 0
    for c in range(len(name)):
        s += ord(name[c]) - 64
    return s
