from typing import Set, List

from libs.numbers_properties import num_size
from libs.types_converting import num_to_list


def ans():
    # create all numbers this way
    digits: Set[int] = set(range(10))
    primes_list: List[int] = [2, 3, 5, 7, 11, 13, 17]
    all_numbers: Set[int] = set()

    def create_nums(num=0) -> None:
        """
        create all numbers with this property
        :param num: current number
        :return: None
        """
        if num_size(num) == 10:
            # stop
            all_numbers.add(num)
        if num == 0:
            # add digs
            for i in range(1, 10):
                create_nums(i)
        else:
            for i in digits.difference(num_to_list(num)):
                # add possible digits
                if num_size(num * 10 + i) <= 3 or ((num * 10 + i) % 1000) % primes_list[num_size(num * 10) - 4] == 0:
                    create_nums(num * 10 + i)

    create_nums()
    return sum(all_numbers)
