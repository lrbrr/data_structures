from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row2 - row1 + 1):
            for j in range(col2 - col1 + 1):
                result += self.matrix[row1 + i][col1 + j]
        return result

class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.sum_matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]
        
        for i in range(self.row):
            for j in range(self.col):
                if i == 0 and j == 0:
                    self.sum_matrix[i][j] = self.matrix[i][j]
                    continue
                if i > 0 and j > 0:
                    self.sum_matrix[i][j] = self.matrix[i][j] + self.sum_matrix[i][j-1] + self.sum_matrix[i-1][j] - self.sum_matrix[i-1][j-1]
                    continue
                if i > 0:
                    self.sum_matrix[i][j] = self.matrix[i][j] + self.sum_matrix[i-1][j]
                if j > 0:
                    self.sum_matrix[i][j] = self.matrix[i][j] + self.sum_matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 - 1 > -1:
            up_sum_matrix = self.sum_matrix[row1 - 1][col2]
        else: 
            up_sum_matrix = 0
            
        if col1 - 1 > -1:
            down_sum_matrix = self.sum_matrix[row2][col1 - 1]
        else:
            down_sum_matrix = 0
            
        if col1 - 1 > -1 and row1 - 1 > -1:
            top_corner_sum_matrix = self.sum_matrix[row1 - 1][col1 - 1]
        else:
            top_corner_sum_matrix = 0

        return self.sum_matrix[row2][col2] - up_sum_matrix - down_sum_matrix + top_corner_sum_matrix

class NumMatrix3:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum_matrix = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        
        if matrix == None:
            return
        
        for row in range(1, len(matrix)+1):
            for col in range(1, len(matrix[0])+1):
                self.sum_matrix[row][col] = matrix[row-1][col-1] + self.sum_matrix[row][col-1] + self.sum_matrix[row-1][col] - self.sum_matrix[row-1][col-1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2+1][col2+1] - self.sum_matrix[row2+1][col1] - self.sum_matrix[row1][col2+1] + self.sum_matrix[row1][col1]
        


example1 = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(example1.sumRegion(2,1,4,3)) # 8
print(example1.sumRegion(1,1,2,2)) # 11
print(example1.sumRegion(1,2,2,4)) # 12

print(' - ' * 50)

example1 = NumMatrix2([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(example1.sumRegion(2,1,4,3)) # 8
print(example1.sumRegion(1,1,2,2)) # 11
print(example1.sumRegion(1,2,2,4)) # 12

print(' - ' * 50)

example1 = NumMatrix3([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(example1.sumRegion(2,1,4,3)) # 8
print(example1.sumRegion(1,1,2,2)) # 11
print(example1.sumRegion(1,2,2,4)) # 12