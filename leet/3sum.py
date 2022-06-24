from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''Method to find the unique triplets which adds up to 0

        Args:
            nums: unsorted list of integers
        
        Returns:
            List of unique triplets from nums which adds up to 0
        '''
        if len(nums) < 3: return []
        nums.sort() # helps to find unique triplets if it is sorted

        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # use two sum II approach to deal with next two integers
            p1 = i
            p2 = len(nums) - 1
            while p1 < p2:
                total = nums[i] + nums[p1] + nums[p2]
                if total > 0:
                    p2 -= 1
                elif total < 0:
                    p1 += 1
                else:
                    result.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1

                    # To remove possible duplicate triplets from being added to the result
                    while nums[p1] == nums[p1-1]:
                        p1 += 1
        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, 0, 1], [-1, -1, 2]]
print(Solution().threeSum([])) # []
print(Solution().threeSum([0])) # []
print(Solution().threeSum([0, 0])) # []