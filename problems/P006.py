def ans():
    limit: int = 100
    # calculate the sum of all numbers between 1 and the limit, and square it
    sum_squared: int = sum([i for i in range(limit + 1)]) ** 2
    # calculate the sum of the squares of all numbers between 1 and the limit
    squares_sum: int = sum([i ** 2 for i in range(limit + 1)])
    return sum_squared - squares_sum
