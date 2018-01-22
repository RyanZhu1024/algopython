class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return False
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[0][i] = False if p[i - 1] != '*' else dp[0][i - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # dp[i - 1][j - 1] ==> 匹配当前字s[i]
                    # dp[i][j - 1] ==> 匹配多个p[j - 1]，也就是匹配多个p
                    # dp[i - 1][j] ==> 匹配空字符串
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
        return dp[m][n]