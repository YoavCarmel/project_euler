def ans():
    one_thousand = 3 + 8
    hundred_and = 7 + 3
    hundred = 7
    ten = 3
    ones = [3, 3, 5, 4, 4, 3, 5, 5, 4]
    tens = [6, 6, 5, 5, 5, 7, 6, 6]
    eleven_to_nineteen = 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
    s1to99 = 9 * sum(ones) + 10 * sum(tens) + eleven_to_nineteen + ten
    s = 100 * sum(ones) + 10 * s1to99 + 9 * hundred + 891 * hundred_and + one_thousand
    return s
