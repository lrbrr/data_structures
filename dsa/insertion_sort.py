from typing import List

def insertion_sort(arr: List[int], n: int) -> List[int]:
    for i in range(1, n):
        key = arr[i]

        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([2, 4, 3, 1], 4)) # [1, 2, 3, 4]
print(insertion_sort([-1, 2, 4, 11, 8, -4, 10], 7)) # [-4, -1, 2, 4, 8, 11, 10]