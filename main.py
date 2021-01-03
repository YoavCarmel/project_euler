import time

from solution_file.solution_file_creator import add_problem_solution
from problems.P001 import ans

start_time = int(round(time.time() * 1000))
# print(ans())
add_problem_solution(277)
print((int(round(time.time() * 1000)) - start_time) / 1000, "seconds")
