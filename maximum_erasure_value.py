from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = []
        temp = [nums[0]]
        for ele in range(1, len(nums)):
            if nums[ele] not in temp:
                temp.append(nums[ele])
            else:
                result.append(sum(temp))
                last_index = [idx for idx, _ in enumerate(nums[:ele]) if nums[idx] == nums[ele]]
                temp = [n for n in nums[last_index[-1]+1:ele+1]]
        result.append(sum(temp))
        return max(result)

class Solution2:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        current_sum, max_sum, pos = 0, 0, 0
        for num in nums:
            while num in seen:
                current_sum -= nums[pos]
                seen.remove(nums[pos])
                pos += 1
            current_sum += num
            seen.add(num)
            max_sum = max(current_sum, max_sum)
        return max_sum

print(Solution().maximumUniqueSubarray([4,2,4,5,6])) # 17
print(Solution().maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])) # 8
print(Solution().maximumUniqueSubarray([1,2,3,4,5,6,7,8,9,10])) # 55

print(' - ' * 50)

print(Solution2().maximumUniqueSubarray([4,2,4,5,6])) # 17
print(Solution2().maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])) # 8
print(Solution2().maximumUniqueSubarray([1,2,3,4,5,6,7,8,9,10])) # 55