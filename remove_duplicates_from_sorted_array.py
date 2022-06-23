from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                nums[p1+1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1+1

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)

print(Solution().removeDuplicates([1,1,2])) # 2
print(Solution().removeDuplicates([1,1,2,3,3])) # 3
print(Solution().removeDuplicates([1,1,2,3,3,4,4,5,5])) # 5

print(' - ' * 30)

print(Solution2().removeDuplicates([1,1,2])) # 2
print(Solution2().removeDuplicates([1,1,2,3,3])) # 3
print(Solution2().removeDuplicates([1,1,2,3,3,4,4,5,5])) # 5