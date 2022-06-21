from heapq import heappop, heappush
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0: continue

            # push the difference into the heap
            heappush(heap, diff)

            # check if we have ladders to climb:
            if len(heap) > ladders:
                min_height = heappop(heap)
                bricks -= min_height
            
            # check if we have bricks left
            if bricks < 0: return i
        return len(heights) - 1


print(Solution().furthestBuilding([4,2,7,6,9,8,14], 5, 1)) # 4
print(Solution().furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2)) #7
print(Solution().furthestBuilding([14,3,19,3], 17, 0)) #3