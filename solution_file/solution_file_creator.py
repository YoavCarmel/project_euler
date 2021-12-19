import time

import pandas as pd

from libs.numbers_properties import num_size

FILE_PATH = "solution_file//solution_file.csv"

PROBLEM_NUM = "ProblemNumber"
SOLUTION = "Solution"
RUNTIME = "Runtime"
GRADE = "Grade"


def create_file():
    df = pd.DataFrame(columns=[PROBLEM_NUM, SOLUTION, RUNTIME, GRADE])
    df.to_csv(FILE_PATH, index=False)


def add_problem_solution(problem_number, override=False):
    pd.options.mode.chained_assignment = None

    df = pd.read_csv(FILE_PATH)
    if not override and problem_number in df[PROBLEM_NUM].values:
        return
    s = "from problems import P" + get_file_number(problem_number)
    exec(s)
    start_time = int(round(time.time() * 1000))
    answer = eval(f"P{get_file_number(problem_number)}.ans()")
    end_time = int(round(time.time() * 1000))
    runtime = (end_time - start_time) / 1000
    # add to file
    if override and problem_number in df[PROBLEM_NUM].values:
        index = df.index[df[PROBLEM_NUM] == problem_number][0]
        df.at[index, SOLUTION] = answer
        df.at[index, RUNTIME] = runtime
        df.at[index, GRADE] = get_grade(runtime)
    else:
        df.loc[-1] = [problem_number, answer, runtime, get_grade(runtime)]
        df.sort_values(by=[PROBLEM_NUM], inplace=True)
    df.to_csv(FILE_PATH, index=False)


def get_file_number(n: int) -> str:
    return "0" * (3 - num_size(n)) + str(n)


def get_grade(t):
    if t < 0.1:
        return "A"
    if t < 1:
        return "B"
    if t < 10:
        return "C"
    if t < 60:
        return "D"
    if t < 300:
        return "E"
    return "F"
