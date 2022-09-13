import numpy as np
import time
from math import prod


# constant function
def const_function(vector):
    return 1


# polynomial function - direct calculation
def direct_polinom(vector):
    x = 1.5
    f = 0.0
    length = len(vector)
    for i in range(length):
        f = f + vector[i] * np.power(x, i)
    return f


# polynomial function - Horner's method
def horner_polinom(vector):
    x = 1.5
    f = 0.0
    length = len(vector)
    for i in range(length):
        f = f * x + vector[length - 1 - i]
    return f


# bubble sort of the elements of vector
def bubble_sort(vector):
    length = len(vector)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if vector[j] > vector[j + 1]:
                temp = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = temp


# partition for quick sort
def partition(vector, start, end):
    pivot = vector[start]
    low = start + 1
    high = end

    while True:
        while low <= high and vector[high] >= pivot:
            high = high - 1
        while low <= high and vector[low] <= pivot:
            low = low + 1
        if low <= high:
            vector[low], vector[high] = vector[high], vector[low]
        else:
            break

    vector[start], vector[high] = vector[high], vector[start]

    return high


# quick sort of the elements of vector
def quick_sort(vector, start, end):
    if start >= end:
        return

    p = partition(vector, start, end)
    quick_sort(vector, start, p-1)
    quick_sort(vector, p+1, end)


# functions and algorithms analysis
def results(filename, function):
    file = open(filename, 'w')
    for n in range(1, 2060):
        total_time = 0.0
        # five runs to calculate the average time
        for k in range(5):
            # generation of the n-dimensional random vector
            v = np.random.random(n)
            start_time = time.perf_counter()
            # researched function
            if function == quick_sort:
                function(v, 0, len(v) - 1)
            else:
                function(v)
            stop_time = time.perf_counter()
            # computer execution time
            total_time = total_time + stop_time - start_time
        # the average time
        avg_time = total_time / 5
        # saving the results in file
        file.write('%d %s\n' % (n, avg_time))
    file.close()


# constant function
results("data/const_function.txt", const_function)
# the sum of the elements
results("data/sum_function.txt", sum)
# the product of the elements
results("data/prod_function.txt", prod)
# polynomial function - direct calculation
results("data/direct_polynom.txt", direct_polinom)
# polynomial function - horner's method
results("data/horner_polynom.txt", horner_polinom)
# bubble sort
results("data/bubble_sort.txt", bubble_sort)
# quick sort
results("data/quick_sort1.txt", quick_sort)
# timsort
results("data/tim_sort1.txt", sorted)






