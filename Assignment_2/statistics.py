# Create a Python project to perform some simple statistics on a list of values.
# Sum:
def sum_(mylist):
    total = 0
    for i in mylist:
        total += i
    print(f'The sum of list  = {total}')
    return total

# Mean:
def mean_(mylist):
    total = 0
    for i in mylist:
        total += i
    avg = total / len(mylist)
    return avg
    print(f'The Mean  = {avg:.4f}')

# Maximum:
def max_(mylist):
    max=0
    for x in mylist:
        if x > max:
            max = x
    print(f'The Maximum number of list  = {max}')
    return max
# Minimum:
def min_(mylist):
    min=mylist[0]
    for x in range(len(mylist)):
        if mylist[x] < min:
            min = x
    print(f'The Minimum number of list  = {min}')
    return min


# Median:
def median_(mylist):

    count = len(mylist)
    middle_index = count // 2
    sorted_values = sorted(mylist)
    if count % 2 == 1:
        median = sorted_values[middle_index]
    else:
        lowmedian= sorted_values[middle_index - 1]
        highmedian = sorted_values[middle_index]
        median = (lowmedian + highmedian) / 2
    print(f'The Median  = {median}')
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
sum_(mylist)
mean_(mylist)
max_(mylist)
min_(mylist)
median_(mylist)
unimodal = modes_([4, 7, 4, 0, 3, 4, 7])
print(f'mode for unimodal ) = {unimodal}')
bimodal = modes_([5, 0, 5, 0, 3, 5, 0])
print(f'mode for bimodal) = {bimodal}')
std(mylist)
