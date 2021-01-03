from libs.special_groups import is_special_sum_set


def ans():
    lines = list()
    f = open("files//P105.txt")
    for line in f.readlines():
        line = [int(i) for i in line.strip("\n").split(",")]
        lines.append(line)
    s = 0
    for line in lines:
        if is_special_sum_set(line):
            s += sum(line)
    return s
