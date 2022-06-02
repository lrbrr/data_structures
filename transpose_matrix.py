from typing import List
import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        
        result = [[None] * row for _ in range(col)]
        
        for i in range(row):
            for j in range(col):
                result[j][i] = matrix[i][j]
                
        return result

class Solution2:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.array(matrix).transpose().tolist()

class Solution3:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))

class Solution4:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for col in range(len(matrix[0])):
            temp = []
            for row in range(len(matrix)):
                temp.append(matrix[row][col])
            result.append(temp)
        return result


print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().transpose([[1,2,3],[4,5,6]]))

print(' - ' * 50)

print(Solution2().transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution2().transpose([[1,2,3],[4,5,6]]))

print(' - ' * 50)

print(Solution3().transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution3().transpose([[1,2,3],[4,5,6]]))

print(' - ' * 50)

print(Solution4().transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution4().transpose([[1,2,3],[4,5,6]]))