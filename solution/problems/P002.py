def ans():
    prev = 1
    before_prev = 1
    curr = 0  # just from init
    s = 0
    while prev + before_prev <= 4000000:
        curr = prev + before_prev
        before_prev = prev
        prev = curr
        if curr % 2 == 0:
            s += curr
    return s
