from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        whole_sum = sum(nums)
        left_sum = 0
        for idx, ele in enumerate(nums):
            if left_sum == (whole_sum - left_sum - ele):
                return idx
            left_sum += ele
        return -1

print(Solution().pivotIndex([1,7,3,6,5,6])) # 3
print(Solution().pivotIndex([1,2,3])) # -1
print(Solution().pivotIndex([-1,-1,-1,0,1,1])) # 0