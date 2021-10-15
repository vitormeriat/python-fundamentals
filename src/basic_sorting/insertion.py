"""
# Insertion

Simple implementation of the insertion sort algorithm in Python

:param array: some mutable ordered array with heterogeneous comparable items inside 
:return: the same array ordered by ascending


Examples:
>>> insertion_sort([0, 5, 3, 2, 2])
[0, 2, 2, 3, 5]

>>> insertion_sort([])
[]

>>> insertion_sort([-2, -5, -45])
[-45, -5, -2]

>>>>>>>>>>>>>>>>>>>> output

Insertion Sort
============================================

Enter numbers separated by a comma:
1,6,3,8
[1, 3, 6, 8]
"""

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertion_sort(array):   
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -= 1
    return array
