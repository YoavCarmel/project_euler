from typing import List


def ans():
    sizes: List[int] = [200, 100, 50, 20, 10, 5, 2, 1]
    req_sum: int = 200
    count_options = [0]  # stupid, but won't let me add 1 as integer. will return size of count_options

    def loop(index: int = 0, s: int = 0) -> None:  # i want to make 8 loops inside each other
        """
        loop on current coin
        :param index: the index of current coin
        :param s: current sum
        """
        if index == len(sizes) - 1:
            count_options[0] += 1
            return
        # else, increment the sum
        while s < req_sum:
            loop(index + 1, s)
            s += sizes[index]
        if s == req_sum:
            count_options[0] += 1

    loop()
    return count_options[0]
