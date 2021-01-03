from libs.special_groups import is_special_sum_set


def ans():
    groups = list()
    f = open("files//P105.txt")
    for line in f.readlines():
        line = [int(i) for i in line.strip("\n").split(",")]
        groups.append(line)
    s = 0
    for l in groups:
        if is_special_sum_set(l):
            s += sum(l)
    return s
