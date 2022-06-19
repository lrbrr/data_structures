from cgitb import small

from typing import List

def selection_sort(arr: List[int], n: int) -> List[int]:
    for i in range(n):
        # find the smallest between i and n
        smallest = min(arr[i:n])

        # swap the smallest from its position to starting position
        temp = arr[i]
        idx_smallest = arr.index(smallest)
        arr[i] = smallest
        arr[idx_smallest] = temp

    return arr

print(selection_sort([2, 4, 3, 1], 4)) # [1, 2, 3, 4]
print(selection_sort([-1, 2, 4, 11, 8, -4, 10], 7)) # [-4, -1, 2, 4, 8, 11, 10]