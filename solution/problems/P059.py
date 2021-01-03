from solution.libs.chars import is_any_case_letter, is_number_char


def ans():
    nums = load_file()
    for c1 in range(ord('a'), ord('z') + 1):
        for i in range(0, len(nums), 3):
            nums[i] = nums[i] ^ c1
        for c2 in range(ord('a'), ord('z') + 1):
            for i in range(1, len(nums), 3):
                nums[i] = nums[i] ^ c2
            for c3 in range(ord('a'), ord('z') + 1):
                for i in range(2, len(nums), 3):
                    nums[i] = nums[i] ^ c3
                if check_all_letters(nums):
                    return sum_ascii_values(nums)
                for i in range(2, len(nums), 3):
                    nums[i] = nums[i] ^ c3
            for i in range(1, len(nums), 3):
                nums[i] = nums[i] ^ c2
        for i in range(0, len(nums), 3):
            nums[i] = nums[i] ^ c1


def load_file():
    f = open("files//P059.txt")
    nums = f.read().split(",")
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return nums


def get_char_of_ascii(x):
    return chr(x)


def check_all_letters(nums):
    for i in range(len(nums)):
        if not is_wanted_char(chr(nums[i])):
            return False
    return True


def print_letters(nums):
    for i in range(len(nums)):
        nums[i] = chr(nums[i])
    print(nums)


def is_wanted_char(c):
    return is_any_case_letter(c) or c == ' ' or c == '.' or c == ',' or c == '(' or c == ')' or \
           is_number_char(c) or c == "'" or c == '"' or c == ';' or c == '!'


def sum_ascii_values(nums):
    s = 0
    for n in nums:
        s += n
    return s
