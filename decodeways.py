class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            if int(s[i]) > 0:
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i] += (dp[i - 2] if i > 1 else 1)
        return dp[len(s) - 1]