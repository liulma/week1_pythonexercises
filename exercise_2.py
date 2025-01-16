import math
import statistics
import sys

arglist = sys.argv[1:]
arglist_int = [int(x) for x in arglist]

sum = sum(arglist_int)

min_value = min(arglist_int)
max_value = max(arglist_int)
mean_value = statistics.mean(arglist_int)
mode_value = statistics.mode(arglist_int)

print(f"Sum of values: {sum}")
print(f"Minimun value: {min_value}")
print(f"Maximum value: {max_value}")
print(f"Mean: {mean_value}")
print(f"Mode: {mode_value}")