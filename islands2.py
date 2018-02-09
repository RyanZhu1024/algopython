class Solution(object):
    def numIslands2(self, m, n, positions):
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.parents:
                    islands.unite(p, q)
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.parents = {}
        self.rank = {}
        self.count = 0

    def add(self, p):
        self.parents[p] = p
        self.rank[p] = 1
        self.count += 1

    def root(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.rank[i] > self.rank[j]:
            i, j = j, i
        self.parents[i] = j
        self.rank[j] += self.rank[i]
        self.count -= 1


print(Solution().numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]))