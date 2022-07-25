arr = [1, 5, 3, 0, 4, 15, 23, -3, -7]

def binary_search(arr, search_number):
    arr_len  = len(arr)
    start = 0
    end = arr_len - 1
    arr.sort()
    print(f'array: {arr}')
    for i in range(arr_len):
        middle = (start + end) // 2
        print(f'middle index : {middle}')
        
        if arr[middle] == search_number:
            return (f'Search number : {search_number} founded in  index: {middle} iterator: {i}')
        elif arr[middle] < search_number:
            start = middle + 1
        else:
            end = middle - 1
    return f'we could not find your number is {search_number}'

search_number = int(input('Enter a search number: '))
print(binary_search(arr, search_number))


