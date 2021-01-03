from libs.numbers_properties import num_size


def ans():
    prev = 1
    before_prev = 1
    curr = prev + before_prev
    index = 3
    while num_size(curr) < 1000:
        index += 1
        before_prev = prev
        prev = curr
        curr = prev + before_prev
    return index
