import math
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[N for _ in range(N)] for _ in range(N)]
        for mine in mines:
            grid[mine[0]][mine[1]] = 0
        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j in range(N):
                l = l + 1 if grid[i][j] else 0
                grid[i][j] = min(grid[i][j], l)
            for k in range(N - 1, -1, -1):
                r = r + 1 if grid[i][k] else 0
                grid[i][k] = min(grid[i][k], r)
            for j in range(N):
                u = u + 1 if grid[j][i] else 0
                grid[j][i] = min(grid[j][i], u)
            for k in range(N - 1, -1, -1):
                d = d + 1 if grid[k][i] else 0
                grid[k][i] = min(grid[k][i], d)
        res = 0
        for row in grid:
            res = max(res, max(row))
        return res

print(Solution().orderOfLargestPlusSign(5, [[4,2]]))
#print(Solution().orderOfLargestPlusSign(5, [[0,0],[0,1],[0,4],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[4,0],[4,1],[4,3],[4,4]]))