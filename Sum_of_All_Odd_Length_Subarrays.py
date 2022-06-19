from typing import List

def sumOddLengthSubarrays(arr: List[int]) -> int:
    sum_all = 0

    for length_being_calculated in range(1, len(arr)+1, 2):
        for idx in range(len(arr)):
            if idx+length_being_calculated <= len(arr):
                sum_all += sum(arr[idx: idx+length_being_calculated])

    return sum_all

print(sumOddLengthSubarrays([1, 4, 2, 5, 3, 4, 1])) # 136
print(sumOddLengthSubarrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 605