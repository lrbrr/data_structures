from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]])) # [[1, 6], [8, 10], [15, 18]]
print(Solution().merge([[1,4],[4,5]])) # [[1, 5]]
print(Solution().merge([[1,4],[2,3]])) # [[1, 4]]
print(Solution().merge([[1,4],[2,6],[3,5]])) # [[1, 6]]
print(Solution().merge([[1,4],[2,6],[3,5],[7,9]])) # [[1, 6], [7, 9]]