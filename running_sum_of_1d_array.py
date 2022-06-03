from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]

class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        
        result.append(nums[0])
        for i in range(1, len(nums)):
            result.append(nums[i] + result[i-1])
        
        return result
    
print(Solution().runningSum([1,2,3,4])) # [1,3,6,10]
print(Solution().runningSum([1,1,1,1,1])) # [1,2,3,4,5]
print(Solution().runningSum([3,1,2,10,1])) # [3,4,6,16,17]

print(' - ' * 50)

print(Solution2().runningSum([1,2,3,4])) # [1,3,6,10]
print(Solution2().runningSum([1,1,1,1,1])) # [1,2,3,4,5]
print(Solution2().runningSum([3,1,2,10,1])) # [3,4,6,16,17]