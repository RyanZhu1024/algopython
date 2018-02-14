class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n, m = len(A), len(B)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res