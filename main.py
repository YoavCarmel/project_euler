from libs.calculations.numbers_theory import sieve_primes
from main_functions.problem_runner import run
from main_functions.solution_file_handler import add_solution_to_file, update_all_problems
from main_functions.solutions_analysis import worst_solutions

if __name__ == '__main__':
    """
    Use run() to run the solution and get the answer and runtime
    Use add_solution_to_file() to run the solution and save it to solution_file.csv.
        use override=True to edit existing solution
    Use worst_solution() to get the worst solutions runtime-wise
    """
    problem_num = 104
    run(problem_num)
    # add_solution_to_file(problem_num, override=True)
    # worst_solutions()
    # update_all_problems()
