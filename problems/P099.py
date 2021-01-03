from math import log2


def ans():
    numbers = load_powers()
    powers = []
    for pair in numbers:
        powers.append(pair[1] * log2(pair[0]))
    return powers.index(max(powers))+1


def load_powers():
    f = open("files//P099.txt")
    numbers = []
    for line in f.readlines():
        numbers.append([int(i) for i in line.strip("\n").split(",")])
    return numbers
