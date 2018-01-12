class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, i, j):
            m, n = len(grid), len(grid[0])
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1
            res += dfs(grid, i + 1, j)
            res += dfs(grid, i - 1, j)
            res += dfs(grid, i, j + 1)
            res += dfs(grid, i, j - 1)
            return res
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(grid, i, j))
        return result

print(Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))