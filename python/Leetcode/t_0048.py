import time
from typing import List

class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new = [['x' for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                new[i][j] = matrix[n - j - 1][i]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new[i][j]

    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]

# 创建一个测试矩阵
test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 测试算法1的执行时间
start_time = time.time()
Solution().rotate1(test_matrix)
end_time = time.time()
print("Algorithm 1 execution time:", end_time - start_time)

# 测试算法2的执行时间
start_time = time.time()
Solution().rotate2(test_matrix)
end_time = time.time()
print("Algorithm 2 execution time:", end_time - start_time)