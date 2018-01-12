# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
import collections
from fractions import gcd
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n < 2:
            return n
        maxPoint = 0
        slopes = collections.Counter()
        for i in range(n):
            curMax, overlapPoints, verticalPoints = 0, 0, 0
            for j in range(i + 1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    overlapPoints += 1
                elif points[i].x == points[j].x:
                    verticalPoints += 1
                else:
                    xdif, ydif = points[j].x - points[i].x, points[j].y - points[i].y
                    g = gcd(xdif, ydif)
                    print(g)
                    xdif = int(xdif / g)
                    ydif = int(ydif / g)
                    slopes[(xdif, ydif)] += 1
                    curMax = max(curMax, slopes[(xdif, ydif)])
                curMax = max(curMax, verticalPoints)
            maxPoint = max(maxPoint, curMax + overlapPoints + 1)
            slopes = collections.Counter()
        return maxPoint

print(Solution().maxPoints([Point(0,0),Point(-1,-1),Point(2,2)]))