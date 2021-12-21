from main_functions.solution_file_handler import add_solution_to_file

if __name__ == '__main__':
    """
    Use run() to run the solution and get the answer and runtime
    Use add_solution_to_file() to run the solution and save it to solution_file.csv.
        use override=True to edit existing solution
    """
    problem_num = 1
    # run(problem_num)
    add_solution_to_file(problem_num, override=True)
