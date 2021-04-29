# Create a Python project to perform some simple statistics on a list of values.
# Sum:
from functools import reduce


def sum_(mylist):
    sum = reduce(lambda x,y: x+y, mylist)
    return sum
# my decorator function
def mydiv(func):
    def inner_func(x,y):
        print(f'Dividing {x} and {y}')
        if y==0:
            print("Division by zero is not possible")
            return
        return func(x,y)
    return inner_func

@mydiv
def divide(a,b):
    return a/b

# Mean:
def mean_(mylist):
    avg = sum_(mylist) / len(mylist)
    return avg

# Maximum:
def max_(mylist):
    max = reduce(lambda a,b: a if a > b else b, mylist[1:], mylist[0])
    return max
# Minimum:
def min_(mylist):
    min= reduce(lambda a,b: a if a < b else b, mylist[1:], mylist[0])
    return min

# Median:
def median_(mylist):

    count = len(mylist)
    middle = count // 2
    sorted_values = sorted(mylist)
    if count % 2 == 1:
        median = sorted_values[middle]
    else:
        low= sorted_values[middle - 1]
        high = sorted_values[middle]
        median = (low + high) / 2
    return median

# Mode:
def modes_(mylist):
    count = len(mylist)
    modes = [];

    if count == 0:
        return []

    sorted_values = sorted(mylist)
    longest_length = 0
    current_length = 1
    previous_value = sorted_values[0]

    for i in range(1, count + 1):
        if (i == count) or (sorted_values[i] != previous_value):
            if current_length == longest_length:
                modes.append(previous_value)
            elif current_length > longest_length:
                longest_length = current_length
                modes = [previous_value]

            if i < count:
                previous_value = sorted_values[i]
                current_length = 1
        else:
            current_length += 1

    return modes

# Variance and Standard deviation
import math
def std(mylist):
    sum_of_squares = 0
    mean = mean_(mylist)

    for x in mylist:
        diff = x - mean
        sum_of_squares += diff * diff


    variance = sum_of_squares / len(mylist)
    stdev = math.sqrt(variance)

    print(f'Variance= {variance:.4f}')
    print(f'Standard deviation= {stdev:.4f}')
    return variance,stdev



mylist = [7, 9, 3, 5, 2, 8]
print("Sum of the list:{} ".format(sum_(mylist)))
print(f'The Mean = {mean_(mylist):.2f}')
print(f'The Maximum number of list  = {max_(mylist)}')
print(f'The Minimum number of list  = {min_(mylist)}')
print(f'The Median  = {median_(mylist)}')
unimodal = modes_([4, 7, 4, 0, 3, 4, 7])
print(f'mode for unimodal  = {unimodal}')
bimodal = modes_([5, 0, 5, 0, 3, 5, 0])
print(f'mode for bimodal = {bimodal}')
std(mylist)
print(divide(10,2))
