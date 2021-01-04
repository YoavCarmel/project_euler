def ans():
    # first fibonacci numbers
    before_prev: int = 1
    prev: int = 1
    s: int = 0
    while prev + before_prev <= 4000000:
        # move one step forward
        before_prev, prev = prev, prev + before_prev
        # if even, add to sum
        if prev % 2 == 0:
            s += prev
    return s
