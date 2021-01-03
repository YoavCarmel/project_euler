from typing import Dict

from solution.problems import *
from solution.libs.numbers_properties import num_size
import time
import pandas as pd
import numpy as np


def create_file():
    df = pd.DataFrame(columns=["Problem Number", "Solution", "Runtime", "Grade"])
    df.to_csv("solution_file//solution_file.csv", index=False)


def add_problem_solution(problem_number, override=False):
    df = pd.read_csv("solution_file//solution_file.csv")
    if not override and problem_number in df["Problem Number"].values:
        return
    s = "from solution.problems import P" + get_file_number(problem_number)
    exec(s)
    start_time = int(round(time.time() * 1000))
    answer = []
    s = "answer.append(P" + get_file_number(problem_number) + ".ans())"
    exec(s)
    end_time = int(round(time.time() * 1000))
    runtime = (end_time - start_time) / 1000
    # add to file
    df.loc[problem_number] = [problem_number, answer[0], runtime, get_grade(runtime)]
    df.sort_values(by=["Problem Number"], inplace=True)
    df.to_csv("solution_file//solution_file.csv", index=False)


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
