from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers[i+1:]:
                return [i+1, numbers[i+1:].index(target - numbers[i])+i+2]

class Solution2:
    def sum_matrix(self, nums: List[int]) -> List[List[int]]:
        empty_matrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for row in range(len(nums)):
            for col in range(len(nums)):
                empty_matrix[row][col] = nums[row] + nums[col]
        return empty_matrix
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        matrix = self.sum_matrix(numbers)
        for i in range(len(matrix)):
            if target in matrix[i]:
                return [i+1, matrix[i][i+1:].index(target)+i+2]

class Solution3:       
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            total = numbers[p1] + numbers[p2]
            if total > target:
                p2 -= 1
            elif total < target:
                p1 += 1
            else:
                return [p1+1, p2+1]
        return []

print(Solution().twoSum([2,7,11,15], 9)) # [1,2]
print(Solution().twoSum([2,7,11,15], 26)) # [3,4]
print(Solution().twoSum([2,7,11,15], 18)) # [2,4]
print(Solution().twoSum([0, 0, 3, 4], 0)) # [1,2]

print(' - ' * 50)

print(Solution2().twoSum([2,7,11,15], 9)) # [1,2]
print(Solution2().twoSum([2,7,11,15], 26)) # [3,4]
print(Solution2().twoSum([2,7,11,15], 18)) # [2,4]
print(Solution2().twoSum([0, 0, 3, 4], 0)) # [1,2]

print(' - ' * 50)

print(Solution3().twoSum([2,7,11,15], 9)) # [1,2]
print(Solution3().twoSum([2,7,11,15], 26)) # [3,4]
print(Solution3().twoSum([2,7,11,15], 18)) # [2,4]
print(Solution3().twoSum([0, 0, 3, 4], 0)) # [1,2]