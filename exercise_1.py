import math
import statistics

def create_list(input_value):
    list_values = [int(x) for x in input_value.split(",")]

    return list_values

def min_max(data_list):
    min_value = min(data_list)
    max_value = max(data_list)
def min_max(data_list):
    min_value = min(data_list)
    max_value = max(data_list)

    return min_value, max_value

def mean(data_list):
    mean_value = sum(data_list) / len(data_list)
def mean(data_list):
    mean_value = sum(data_list) / len(data_list)

    return mean_value

def median(data_list):
    median_value = statistics.median(data_list)
def median(data_list):
    median_value = statistics.median(data_list)

    return median_value

def mode(data_list):
    mode_value = statistics.mode(data_list)
def mode(data_list):
    mode_value = statistics.mode(data_list)

    return mode_value


user_value = input("Please enter values: ")
data_list = create_list(user_value)
min_value, max_value = min_max(data_list)
mean_value = mean(data_list)
median_value = median(data_list)
mode_value = mode(data_list)
data_list = create_list(user_value)
min_value, max_value = min_max(data_list)
mean_value = mean(data_list)
median_value = median(data_list)
mode_value = mode(data_list)
print(f"The minimum value is {min_value} and the maximum value is {max_value}. The mean is {mean_value}, the median is {median_value} and the mode is {mode_value}.")
