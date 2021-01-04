from libs.numbers_properties import num_size


def ans():
    count = 0
    for i in range(1, 10):
        n = 1
        while num_size(i ** n) >= n:  # number of digits sort of decreases the higher the power
            if num_size(i ** n) == n:
                count += 1
            n += 1
    return count
