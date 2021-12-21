import time

import pandas as pd

from main_functions.runs_helper import get_import_line, get_run_line

FILE_PATH = "solution_file.csv"

PROBLEM_NUM = "ProblemNumber"
SOLUTION = "Solution"
RUNTIME = "Runtime"
GRADE = "Grade"


def create_file():
    df = pd.DataFrame(columns=[PROBLEM_NUM, SOLUTION, RUNTIME, GRADE])
    df.to_csv(FILE_PATH, index=False)


def add_solution_to_file(problem_number, override=False):
    df = pd.read_csv(FILE_PATH)
    if not override and problem_number in df[PROBLEM_NUM].values:
        return
    # run the solution
    exec(get_import_line(problem_number))
    start_time = time.time()
    answer = eval(get_run_line(problem_number))
    end_time = time.time()
    runtime = round(end_time - start_time, 3)
    # add to file
    new_line = [problem_number, answer, runtime, _get_grade(runtime)]
    if override and problem_number in df[PROBLEM_NUM].values:
        df[df[PROBLEM_NUM] == problem_number] = new_line
    else:
        df.loc[-1] = new_line
        df = df.sort_values(by=PROBLEM_NUM)
    df.to_csv(FILE_PATH, index=False)


def _get_grade(t):
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
