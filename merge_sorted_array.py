from typing import List

class Solution:        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        elif n == 0:
            pass
        else:
            tracker1 = 0
            tracker2 = 0
            while tracker1 < m and tracker2 < n:
                if nums1[tracker1] < nums2[tracker2]:
                    tracker1 += 1
                else:
                    nums1.insert(tracker1, nums2[tracker2])
                    tracker1 += 1
                    tracker2 += 1
                    m += 1
                    nums1.pop(-1)
            
            if tracker2 < n:
                nums1[tracker1:] = nums2[tracker2:]

        print(nums1)

class Solution2:        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        print(nums1)

Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3) # [1,2,2,3,5,6]
Solution().merge([1], 1, [], 0) # [1]
Solution().merge([0], 0, [1], 1) # [1]
Solution().merge([1, 0], 1, [2], 1) # [1,2]
Solution().merge([2, 0], 1, [1], 1) # [1,2]

print(' - ' * 50)

Solution2().merge([1,2,3,0,0,0], 3, [2,5,6], 3) # [1,2,2,3,5,6]
Solution2().merge([1], 1, [], 0) # [1]
Solution2().merge([0], 0, [1], 1) # [1]
Solution2().merge([1, 0], 1, [2], 1) # [1,2]
Solution2().merge([2, 0], 1, [1], 1) # [1,2]