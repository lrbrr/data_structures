from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []        
        for num in nums:
            heappush(heap, -num)
        
        for i in range(k):
            result = heappop(heap)
        
        return -result

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

print(Solution().findKthLargest([1, 4, 2, 3, 5, 8, -1], 2)) # 5

print(' - ' * 30)

print(Solution2().findKthLargest([1, 4, 2, 3, 5, 8, -1], 2)) # 5