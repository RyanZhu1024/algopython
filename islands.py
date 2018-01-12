class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        def dfs(grid, i, j):
            m, n = len(grid), len(grid[0])
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 1
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            return 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res += dfs(grid, i, j)
        return res

print(Solution().numIslands())