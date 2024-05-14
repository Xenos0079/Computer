# 861. Score After Flipping Matrix
from sys import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Toggle rows to ensure the leftmost bit of each row is 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # Toggle columns to maximize the score
        for j in range(1, n):
            count_1 = sum(grid[i][j] for i in range(m))
            if count_1 < m - count_1:  # More 0's than 1's, toggle the column
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        # Calculate the score
        score = 0
        for row in grid:
            score += int(''.join(map(str, row)), 2)

        return score
        