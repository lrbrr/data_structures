from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        v = list(count.values())
        k = list(count.keys())
        return k[v.index(max(v))]

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

class Solution3:
    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

print(Solution().majorityElement([3,2,3])) # 3
print(Solution().majorityElement([2,2,1,1,1,2,2])) # 2

print(' - ' * 30)

print(Solution2().majorityElement([3,2,3])) # 3
print(Solution2().majorityElement([2,2,1,1,1,2,2])) # 2

print(' - ' * 30)

print(Solution3().majorityElement([3,2,3])) # 3
print(Solution3().majorityElement([2,2,1,1,1,2,2])) # 2
