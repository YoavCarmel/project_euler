from libs.files import get_file_lines
from libs.numbers_operations import list_to_num
from tqdm import tqdm


def ans():
    lines = get_file_lines("P096")
    sudokus = []
    for i in range(0, len(lines), 10):
        sudokus.append(convert_line_to_sudoku(lines[i + 1:i + 10]))
    # return available_nums(sudokus[0], 3, 4)
    three_digs_sum = 0
    for i in tqdm(sudokus):
        solve_sudoku(i)
        first_three_digs = i[0][:3]
        three_digs_sum += list_to_num(first_three_digs)
    return three_digs_sum


def convert_line_to_sudoku(lines):
    s = []
    for line in lines:
        s.append([int(i) for i in line])
    return s


def solve_sudoku(sudoku, i=0, j=0):
    if i == j == 8:
        avs = available_nums(sudoku, i, j)
        if len(avs) != 0:
            sudoku[i][j] = avs[0]
        return True
    if sudoku[i][j] != 0:
        solved = solve_sudoku(sudoku, i + (j + 1) // 9, (j + 1) % 9)
        if solved:
            return True
    else:
        avs = available_nums(sudoku, i, j)
        for k in avs:
            sudoku[i][j] = k
            solved = solve_sudoku(sudoku, i + (j + 1) // 9, (j + 1) % 9)
            if solved:
                return True
        sudoku[i][j] = 0  # clean up
        return False


def available_nums(sudoku, i, j):
    if sudoku[i][j] != 0:
        return []
    avs = set([k for k in range(1, 10)])
    for k in sudoku[i]:  # row
        if k in avs:
            avs.remove(k)
    for k in sudoku:  # columns
        if k[j] in avs:
            avs.remove(k[j])
    for ki in range((i // 3) * 3, (i // 3) * 3 + 3):  # squares
        for kj in range((j // 3) * 3, (j // 3) * 3 + 3):
            if sudoku[ki][kj] in avs:
                avs.remove(sudoku[ki][kj])
    return list(avs)
