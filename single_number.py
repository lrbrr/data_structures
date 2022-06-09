from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        position = 0
        for n in nums:
            if n in nums[:position] or n in nums[position+1:]:
                position += 1
            else:
                return n

print(Solution().singleNumber([2,2,1])) # 1
print(Solution().singleNumber([4,1,2,1,2])) # 4