from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cross_off_list = [i for i in range(left, right+1)]
        for rnge in ranges:
            for i in range(rnge[0], rnge[1]+1):
                if i in cross_off_list:
                    cross_off_list.remove(i)
        return True if len(cross_off_list) == 0 else False

print(Solution().isCovered([[1,2],[3,4],[5,6]], 2, 5)) # True
print(Solution().isCovered([[1,10],[10,20]], 21, 21)) # False
print(Solution().isCovered([[37,49],[5,17],[8,32]], 29, 49)) # False