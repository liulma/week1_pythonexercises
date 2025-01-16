import math
import statistics

def create_list(input_value):
    list_values = [int(x) for x in input_value.split(",")]

    return list_values

def min_max(input_value):
    list_values = create_list(input_value)

    min_value = min(list_values)
    max_value = max(list_values)

    return min_value, max_value

def mean(input_value):
    list_values = create_list(input_value)

    mean_value = sum(list_values) / len(list_values)

    return mean_value

def median(input_value):
    list_values = create_list(input_value)

    median_value = statistics.median(list_values)

    return median_value

def mode(input_value):
    list_values = create_list(input_value)

    mode_value = statistics.mode(list_values)

    return mode_value


user_value = input("Please enter values: ")
min_value, max_value = min_max(user_value)
mean_value = mean(user_value)
median_value = median(user_value)
mode_value = mode(user_value)
print(f"The minimum value is {min_value} and the maximum value is {max_value}. The mean is {mean_value}, the median is {median_value} and the mode is {mode_value}.")