from typing import List

class Solution:
    # linear scan
    def peakFinder(self, arr: List[int]) -> List[int]:

        # first element is peak if second is smaller than first
        if arr[0] > arr[1]: return arr[0]

        # if neither first nor last are peaks, find peak
        for i in range(1, len(arr) - 1):
            if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                return arr[i]
        
        # last element is peak if second to last is smaller than last
        if arr[-2] < arr[-1]: return arr[-1]

class Solution2:
    # Binary search - Recursive
    def search(self, arr: List[int], start: int, end: int) -> int:
        if start == end: return arr[start]
        mid = (start + end) // 2
        if arr[mid] > arr[mid+1]:
            return self.search(arr, start, mid)
        return self.search(arr, mid+1, end)

    def peakFinder(self, arr: List[int]) -> List[int]:
        return self.search(arr, 0, len(arr) -1)

class Solution3:
    # Binary search - Iterative
    def peakFinder(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = (start+end) // 2
            if arr[mid] > arr[mid+1]:
                end = mid
            else:
                start = mid+1
        return arr[start]

print(Solution().peakFinder([1, 2, 1, 3, 4, 5])) # 2 | 5
print(Solution().peakFinder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 10

print(' - '* 20)

print(Solution2().peakFinder([1, 2, 1, 3, 4, 5])) # 2 | 5
print(Solution2().peakFinder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 10

print(' - '* 20)

print(Solution3().peakFinder([1, 2, 1, 3, 4, 5])) # 2 | 5
print(Solution3().peakFinder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 10