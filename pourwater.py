class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        def findLeftCandidate():
            candidate = -1
            i = K - 1
            while i >= 0 and heights[i] <= heights[i + 1]:
                if heights[i] < heights[i + 1]:
                    candidate = i
                i -= 1
            return candidate
        def findRightCandidate():
            candidate = -1
            i = K + 1
            while i < len(heights) and heights[i] <= heights[i - 1]:
                if heights[i] < heights[i - 1]:
                    candidate = i
                i += 1
            return candidate
        drops = V
        while drops > 0:
            leftCandidate = findLeftCandidate()
            rightCandidate = findRightCandidate()
            if leftCandidate == -1 and rightCandidate == -1:
                heights[K] += 1
            elif leftCandidate == -1:
                heights[rightCandidate] += 1
            else:
                heights[leftCandidate] += 1
            drops -= 1
        return heights
