import time

from problems.P024 import ans

start_time = int(round(time.time() * 1000))
print(ans())
# add_problem_solution(277)
print((int(round(time.time() * 1000)) - start_time) / 1000, "seconds")
