from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        eps = 0.01
        result = [abs(num-eps) for num in nums]
        idx_min = result.index(min(result))
        return abs(nums[idx_min]) if nums[idx_min] < 0 and abs(nums[idx_min]) in nums else nums[idx_min]

print(Solution().findClosestNumber([-1,2,1,4])) # 1
print(Solution().findClosestNumber([-4,-2,1,4,8])) # 1
print(Solution().findClosestNumber([-4,-2,4,8,10])) # -2