import time as t
f1 = open("20k.txt")
data_ = f1.read()
data = data_.split('\n')
person_list = data[0:900]
person_list_bubble=person_list
person_list_quick=person_list
person_list_selection=person_list



def bubble(records):
    length = len(records)
    done = False
    while not done:
        done = True
        for i in range(length - 1):
            if len(records[i]) > len(records[i + 1]):
                records[i], records[i + 1] = records[i + 1], records[i]
                done = False

def partition(person_list, low, high):
    i = low - 1
    pivot = person_list[high]
    for j in range(low,high):
        if len(person_list[j]) <= len(pivot):
            i += 1
            person_list[i], person_list[j] = person_list[j], person_list[i]
    person_list[i+1], person_list[high] = person_list[high], person_list[i+1]
    return (i+1)

def quickSort(person_list, low, high):
    if low < high:
        pi = partition(person_list, low, high)
        quickSort(person_list, low, pi-1)
        quickSort(person_list, pi+1, high)

def selectionSort(person_list):
    for i in range(len(person_list)):
        min_index = i
        for j in range(i+1, len(person_list)):
            if len(person_list[min_index]) > len(person_list[j]):
                min_index = j
        person_list[i], person_list[min_index] = person_list[min_index], person_list[i]


start_time=t.time()
bubble(person_list_bubble)
end_time=t.time()
print(f'Bubble sort execution time:{end_time-start_time}')
print(f'Bubble sort result: {person_list_bubble}')
start_time=t.time()
quickSort(person_list_quick,0,(int(len(person_list_quick))-1))
end_time=t.time()
print(f'Quick sort execution time={end_time-start_time}')
print(f'Quick sort result: {person_list_quick}')
start_time=t.time()
selectionSort(person_list_selection)
end_time=t.time()
print(f'Selection sort execution time={end_time-start_time}')
print(f'Quick sort result: {person_list_selection}')