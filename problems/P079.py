def ans():
    f = open("files//P079.txt")
    nums = [i.strip('\n') for i in f.readlines()]
    password = ""
    while len(nums) != 0:
        d = create_dict(nums)
        for k in d.keys():
            if d[k][1] == d[k][2] == 0:
                password += k
                for i in range(len(nums)):
                    if nums[i][0] == k:
                        nums[i] = nums[i][1:]
                nums = [i for i in nums if i != ""]
                break
    return password


def create_dict(nums):
    order = dict()
    for i in nums:
        for j in range(len(i)):
            if i[j] in order:
                order[i[j]][j] += 1
            else:
                order[i[j]] = [0, 0, 0]
    return order
