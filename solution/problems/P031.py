def ans():
    sizes = [200, 100, 50, 20, 10, 5, 2, 1]
    req_sum = 200
    count_options = []  # stupid, but won't let me add 1 as integer. will return size of count_options

    def loop(index, s):  # i want to make 8 loops inside each other
        while s < req_sum:
            if index < len(sizes) - 1:
                loop(index + 1, s)
            s += sizes[index]
        if s == req_sum:
            count_options.append(1)

    loop(0, 0)
    return len(count_options)
