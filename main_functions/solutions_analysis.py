import pandas as pd

from main_functions.solution_file_handler import SOLUTION_FILE_PATH, RUNTIME, PROBLEM_NUM, GRADE


def worst_solutions(n=10):
    df = pd.read_csv(SOLUTION_FILE_PATH)
    df = df.sort_values(by=RUNTIME)[::-1]
    df = df.head(n)
    df = df[[PROBLEM_NUM, RUNTIME, GRADE]]
    df = df.set_index(PROBLEM_NUM)
    print(df)
