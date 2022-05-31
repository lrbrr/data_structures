from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original

class Solution2:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        else:
            return self.findFinalValue(nums, original*2)

print(Solution().findFinalValue([5, 3, 6, 1, 12], 3)) # 24
print(Solution().findFinalValue([2, 7, 9], 4)) # 4

print(Solution2().findFinalValue([5, 3, 6, 1, 12], 3)) # 24
print(Solution2().findFinalValue([2, 7, 9], 4)) # 4