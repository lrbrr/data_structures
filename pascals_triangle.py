from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                temp = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        temp.append(1)
                    else:
                        temp.append(result[i-1][j-1] + result[i-1][j])
                result.append(temp)
        return result

print(Solution().generate(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(Solution().generate(1)) # [[1]]