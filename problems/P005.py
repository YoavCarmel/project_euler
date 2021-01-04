from libs.numbers_properties import lcm_list


def ans():
    limit: int = 20
    # return the lcm of all numbers from 1 to limit, this is the smallest number divisible by all of them by definition
    return lcm_list([i for i in range(1, limit + 1)])
