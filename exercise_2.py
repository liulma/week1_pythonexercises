#import math
import statistics as st
#import sys
import argparse
import numpy as np

#arglist = sys.argv[1:]
#arglist_int = [int(x) for x in arglist]

#sum = sum(arglist_int)

#min_value = min(arglist_int)
#max_value = max(arglist_int)
#mean_value = statistics.mean(arglist_int)
#mode_value = statistics.mode(arglist_int)

#print(f"Sum of values: {sum}")
#print(f"Minimun value: {min_value}")
#print(f"Maximum value: {max_value}")
#print(f"Mean: {mean_value}")
#print(f"Mode: {mode_value}")

parser = argparse.ArgumentParser(description ='Count the sum of integers.')
parser.add_argument('integers', metavar ='N', 
                    type = int, nargs ='+',
                    help ='an integer for the program')

parser.add_argument('sum', 
                    action ='store_const',
                    const = sum)

parser.add_argument('max', 
                    action ='store_const',
                    const = max)

parser.add_argument('min', 
                    action ='store_const',
                    const = min)

parser.add_argument('len', 
                    action ='store_const',
                    const = len)

args = parser.parse_args()
median = np.median(args.integers)
mode = st.mode(args.integers)
add = args.sum(args.integers)
max = args.max(args.integers)
min = args.min(args.integers)
mean = add / args.len(args.integers)
print(add)
print(max)
print(min)
print(mean)
print(median)
print(mode)