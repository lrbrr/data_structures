from typing import List

def insertion_sort(arr: List[int], n: int) -> List[int]:
    sorted = [arr[0]]
    for n_unsorted in range(1, n):
        picked = arr[n_unsorted]
        to_place = n_unsorted
        while arr[to_place-1] > picked and to_place > 0:            
            to_place -= 1
        sorted.insert(to_place, picked)
    return sorted

print(insertion_sort([2, 4, 3, 1], 4)) # [1, 2, 3, 4]
print(insertion_sort([-1, 2, 4, 11, 8, -4, 10], 7)) # [-4, -1, 2, 4, 8, 11, 10]