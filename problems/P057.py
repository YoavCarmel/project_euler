from typing import List

from libs.numbers_properties import num_size


def ans():
    nums: List[int] = [3, 7]
    dens: List[int] = [2, 5]
    #calculate the fractions
    while len(nums) < 1000:
        nums.append(2 * nums[len(nums) - 1] + nums[len(nums) - 2])
        dens.append(2 * dens[len(dens) - 1] + dens[len(dens) - 2])
    count = 0
    for i in range(len(nums)):
        if num_size(nums[i]) > num_size(dens[i]):
            count += 1
    return count
