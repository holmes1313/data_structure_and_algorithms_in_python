# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:03:08 2019

@author: z.chen7
"""

# Binary Search Practice
"""
You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        if low == high:
            return low if input_array[low] == value else -1
        mid = (low + high) // 2
        if input_array[mid] == value:
            return mid
        elif value < input_array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
binary_search(test_list, test_val1)
binary_search(test_list, test_val2)





# Recursion
"""
basic example in pseudo code

function recursive(input):
    # 2.base case
    if input <= 0:
        return input
    
    else:
        # 1.calls itself
        output = recursive(input - 1)  # 3. alter the input parameter at some point
        return output

Our Steps
recursive(2)
    recursive(1)
        recursive(0)
            return 0
        output = 0
        return 0
    output = 0
    return 0

"""

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def getFib(position):
    memory = {}
    
    if memory.get(position):
        return memory.get(position)
    
    if (position == 0) or (position == 1):
        memory[position] = position
        return position

    output = getFib(position - 1) + getFib(position - 2)
    memory[position] = output
        
    return output
        
getFib(9)    
getFib(11)
getFib(0)






# Sorting
"""
An in place sorting algorithm just reranges the elements in the data structure
they're already in without needing to copy everything to a new data structure.
These algorithms have low space complexity, because you don't need to recreate
the data structure."""


# Bubble sort
"""
Bubble sort, sometimes referred to as sinking sort, 
is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements and swaps them if they are in the wrong order. """
# Efficiency of Bubble Sort
# O(n^2)
# Bubble sorting is a great example of an in-place sorting algorithm
# space = O(1)

def bubbleSort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                
    return my_list

my_list = ['b', 'd', 'f', 'a', 'c', 'e']
bubbleSort(my_list)



# Merge sort
"""
Merge sort is a divide and conquer algorithm to 
1.Divide the unsorted list into n sublists, each containing one element 
2.Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining."""
# Efficiency of Bubble Sort
# O(n*log(n))
# space = O(n)


# Quick sort
"""
Quicksort is a divide and conquer algorithm.
Quicksort first divides a large array into two smaller sub-arrays: 
    the low elements and the high elements. 
Quicksort can then recursively sort the sub-arrays. The steps are:

1.Pick an element, called a pivot, from the array.
2.Partitioning: reorder the array so that all elements with values less than 
the pivot come before the pivot, while all elements with values greater 
than the pivot come after it (equal values can go either way). 
After this partitioning, the pivot is in its final position. 
This is called the partition operation.
3.Recursively apply the above steps to the sub-array of 
elements with smaller values and separately to the sub-array 
of elements with greater values."""
# O(n^2)
# space = O(1)

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    return array
    
    
    

