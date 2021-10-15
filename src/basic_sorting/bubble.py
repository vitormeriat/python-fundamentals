
"""
Simple implementation of bubble sort algorithm in Python

* param array: some mutable ordered array with heterogeneous comparable items inside
* return: the same array ordered by ascending

### Examples:

bubble_sort([0, 5, 3, 2, 2])
[0, 2, 2, 3, 5]

bubble_sort([])
[]

bubble_sort([-2, -5, -45])
[-45, -5, -2]

>>>>>>>>>>>>>>>>>>>> output

Bubble Sort
========================================

Enter numbers separated by a comma:

12,6,2,89,45,74,23,1
[1, 2, 6, 12, 23, 45, 74, 89]
"""

def bubble_sort(array):
    length = len(array)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

