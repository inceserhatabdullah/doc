#!/usr/bin/env python3

def bubble_sort(arr):
    has_swapped = True
    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(arr) - num_of_iterations - 1):
            if arr[i] > arr[i+1]:
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
        num_of_iterations += 1
        
    return arr
