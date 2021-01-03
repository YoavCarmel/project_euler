def ans():
    max_cycle = 0
    found_d = 0
    for i in range(1, 1000):
        ldc = long_division_cycle(i)
        if max_cycle < ldc:
            max_cycle = ldc
            found_d = i
    return found_d


def long_division_cycle(x):
    count = 0
    num = 1
    result = []
    rem = []
    while num != 0 and loop_detected(result, rem) == 0:
        while num < x:
            num *= 10
            result.append(num // x)
            rem.append(num % x)
        num -= x * (num // x)
        count += 1
    return loop_detected(result, rem)


def loop_detected(div, rem):
    if len(div) < 2:
        return False
    curr_rem = rem[len(rem) - 1]
    curr_div = div[len(div) - 1]
    for i in range(len(div) - 2, 0, -1):
        if curr_rem == rem[i] and curr_div == div[i]:
            return (len(div) - 1) - i
    return 0
