#!/usr/bin/env python3

def binary_search(arr, search_number):
    arr.sort()
    start_index = 0
    final_index = len(arr) - 1
    
    while arr[0] <= len(arr) - 1:
        middle_index = (start_index + final_index) // 2
       
        if arr[middle_index] == search_number:
            print(f'We found the number you searched!\nlist = {arr}\nindex = {middle_index}\nsearch_number = {search_number}')
            return middle_index
        elif arr[middle_index] < search_number:
            start_index = middle_index + 1
        else:
            final_index = middle_index - 1
    return False