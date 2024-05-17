# 1219. Path with Maximum Gold

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0

        def dfs(i, j, cur_gold):
            nonlocal max_gold
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            cur_gold += grid[i][j]
            temp = grid[i][j]
            grid[i][j] = 0  # Mark as visited
            max_gold = max(max_gold, cur_gold)
            dfs(i + 1, j, cur_gold)
            dfs(i - 1, j, cur_gold)
            dfs(i, j + 1, cur_gold)
            dfs(i, j - 1, cur_gold)
            grid[i][j] = temp  # Backtrack

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)

        return max_gold