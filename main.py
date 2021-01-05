import time

from solution_file.solution_file_creator import add_problem_solution
from problems.P092 import ans
from libs.calculations import get_co_primes,totient_euler

start_time = int(round(time.time() * 1000))
print(ans())
# add_problem_solution(91, override=True)
print((int(round(time.time() * 1000)) - start_time) / 1000, "seconds")
