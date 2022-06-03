from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)

print(Solution().missingNumber([0])) # 1
print(Solution().missingNumber([1])) # 0
print(Solution().missingNumber([0, 1])) # 2
print(Solution().missingNumber([0, 1, 2])) # 3

print(' - ' * 50)

print(Solution2().missingNumber([0])) # 1
print(Solution2().missingNumber([1])) # 0
print(Solution2().missingNumber([0, 1])) # 2
print(Solution2().missingNumber([0, 1, 2])) # 3