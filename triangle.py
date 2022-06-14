from typing import List

class Solution:
    # top down
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return min(triangle[0])
        
        for level in range(1, len(triangle)):
            for lvl_idx in range(len(triangle[level])):
                prev_idx = lvl_idx-1 if lvl_idx-1 > 0 else 0
                same_idx = lvl_idx if len(triangle[level-1]) > lvl_idx else len(triangle[level-1])-1
                triangle[level][lvl_idx] = min (triangle[level][lvl_idx] + triangle[level-1][same_idx], triangle[level][lvl_idx] + triangle[level-1][prev_idx])
        return min(triangle[-1])

class Solution2:
    # Bottom up
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return

        row = triangle[-1]
        for level in range(len(triangle)-2, -1,-1):
            for lvl_idx in range(len(triangle[level])):
                row[lvl_idx] = min(row[lvl_idx], row[lvl_idx+1]) + triangle[level][lvl_idx]

        return row[0]

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(Solution().minimumTotal([[-1],[2,3],[1,-1,-3]])) # -1

print(' - ' * 30)

print(Solution2().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(Solution2().minimumTotal([[-1],[2,3],[1,-1,-3]])) # -1