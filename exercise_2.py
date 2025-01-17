import statistics as st
import argparse
import numpy as np

parser = argparse.ArgumentParser(description ='Count the sum of integers.')
parser.add_argument('integers', metavar ='N', 
                    type = int, nargs ='+',
                    help ='Integers for the program')

args = parser.parse_args()
add = np.sum(args.integers)
max_val = np.max(args.integers)
min_val = np.min(args.integers)
mean_val = add / len(args.integers)
median_val = np.median(args.integers)
mode_val = st.mode(args.integers)

print(f"The sum is: {add}")
print(f"The maximum value is: {max_val}")
print(f"The minimum value is: {min_val}")
print(f"The mean is: {mean_val}")
print(f"The median is: {median_val}")
print(f"The mode is: {mode_val}")