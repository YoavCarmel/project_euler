from main_functions.solution_file_handler import RUNTIME, PROBLEM_NUM, GRADE, read_solutions_file


def worst_solutions(n=10):
    df = read_solutions_file()
    df = df.sort_values(by=RUNTIME)[::-1]
    df = df.head(n)
    df = df[[PROBLEM_NUM, RUNTIME, GRADE]]
    df = df.set_index(PROBLEM_NUM)
    print(df)
