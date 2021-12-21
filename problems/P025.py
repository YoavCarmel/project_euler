from libs.calculations.numbers_properties import num_size


def ans():
    prev: int = 1
    before_prev: int = 1
    index: int = 2
    limit: int = 1000
    # count numbers until we get a number with at least 1000 digits
    while num_size(prev) < limit:
        index += 1
        before_prev, prev = prev, before_prev + prev
    return index
