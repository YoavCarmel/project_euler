from typing import List, Dict


def ans():
    f = open("files//P079.txt")
    nums: List[str] = [i.strip('\n') for i in f.readlines()]
    password = ""
    while len(nums) != 0:
        d: Dict[str, List[int]] = create_dict(nums)
        for k in d:  # for each char in the passcode
            if d[k][1] == d[k][2] == 0:  # if it only appears as first
                # then it is the next char
                password += k
                for i in range(len(nums)):
                    # remove the char from the first positions whre it was
                    if nums[i][0] == k:
                        nums[i] = nums[i][1:]
                # remove empty strings
                nums = [i for i in nums if i != ""]
                # continue to next char finding
                break
    return password


def create_dict(nums) -> Dict[str, List[int]]:
    """
    :param nums: a list of strings
    :return: a dict from each char to a triple of counters, the count of times it appeared in each position
    """
    order: Dict[str, List[int]] = dict()
    for i in nums:
        for j in range(len(i)):
            if i[j] in order:
                order[i[j]][j] += 1
            else:
                order[i[j]] = [0, 0, 0]
    return order
