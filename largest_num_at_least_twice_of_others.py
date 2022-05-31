from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]*2 <= max(nums) or i == nums.index(max(nums)):
                continue
            else:
                return -1
        return nums.index(max(nums))
        
print(Solution().dominantIndex([3,6,1,0])) # 1
print(Solution().dominantIndex([1,2,3,4])) # -1
print(Solution().dominantIndex([1])) # 0
print(Solution().dominantIndex([0,0,0,1])) # 3