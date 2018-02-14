class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        self.visited = set()
        q = [(sx, sy)]
        while q:
            item = q.pop(0)
            print(item)
            if item == (tx, ty):
                return True
            self.visited.add(item)
            total = sum(item)
            if total <= tx:
                q.append((total, item[1]))
            if total <= ty:
                q.append((item[0], total))
        return False

print(Solution().reachingPoints(3,3,12,9))