def roman_to_int(r):
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    i = 0
    s = 0
    while i < len(r):
        if r[i] == 'M':
            s += values[r[i]]
        elif r[i] == 'D':
            s += values[r[i]]
        elif r[i] == 'C':
            if i == len(r) - 1:
                s += values[r[i]]
            elif r[i + 1] == 'D' or r[i + 1] == 'M':
                s += values[r[i + 1]] - values[r[i]]
                i += 1
            else:
                s += values[r[i]]
        elif r[i] == 'L':
            s += values[r[i]]
        elif r[i] == 'X':
            if i == len(r) - 1:
                s += values[r[i]]
            elif r[i + 1] == 'L' or r[i + 1] == 'C':
                s += values[r[i + 1]] - values[r[i]]
                i += 1
            else:
                s += values[r[i]]
        elif r[i] == 'V':
            s += values[r[i]]
        elif r[i] == 'I':
            if i == len(r) - 1:
                s += values[r[i]]
            elif r[i + 1] == 'V' or r[i + 1] == 'X':
                s += values[r[i + 1]] - values[r[i]]
                i += 1
            else:
                s += values[r[i]]
        elif r[i] == '\n':
            return s
        else:
            raise Exception("unknown number")
        i += 1
    return s


def int_to_roman(n):
    s = ""
    while n > 0:
        if n - 1000 >= 0:
            s += 'M'
            n -= 1000
        elif n - 900 >= 0:
            s += 'CM'
            n -= 900
        elif n - 500 >= 0:
            s += 'D'
            n -= 500
        elif n - 400 >= 0:
            s += 'CD'
            n -= 400
        elif n - 100 >= 0:
            s += 'C'
            n -= 100
        elif n - 90 >= 0:
            s += 'XC'
            n -= 90
        elif n - 50 >= 0:
            s += 'L'
            n -= 50
        elif n - 40 >= 0:
            s += 'XL'
            n -= 40
        elif n - 10 >= 0:
            s += 'X'
            n -= 10
        elif n - 9 >= 0:
            s += 'IX'
            n -= 9
        elif n - 5 >= 0:
            s += 'V'
            n -= 5
        elif n - 4 >= 0:
            s += 'IV'
            n -= 4
        elif n - 1 >= 0:
            s += 'I'
            n -= 1
    return s
