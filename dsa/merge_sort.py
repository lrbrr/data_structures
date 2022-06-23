from typing import List

def merge(arr1: List[int], arr2: List[int], arr: List[int]) -> List[int]:
    pointer1 = 0
    pointer2 = 0
    arr_pointer = 0
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] > arr2[pointer2]:
            arr[arr_pointer] = arr2[pointer2]
            pointer2 += 1
        else:
            arr[arr_pointer] = arr1[pointer1]
            pointer1 += 1
        arr_pointer += 1
    
    while pointer1 < len(arr1):
        arr[arr_pointer] = arr1[pointer1]
        pointer1 += 1
        arr_pointer += 1
    while pointer2 < len(arr2):
        arr[arr_pointer] = arr2[pointer2]
        pointer2 += 1
        arr_pointer += 1

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return

    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    
    merge(left, right, arr)

example1 = [2, 4, 3, 1]
merge_sort(example1) 
print(example1) # [1, 2, 3, 4]

example2 = [-1, 2, 4, 11, 8, -4, 10]
merge_sort(example2)
print(example2) # [-4, -1, 2, 4, 8, 11, 10]