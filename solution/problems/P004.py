from solution.libs.numbers_properties import is_palindrome


def ans():
    m=-1
    for i in range(900,1000):
        for j in range(i,1000):
            if is_palindrome(i*j):
                m=max(m,i*j)
    return m
