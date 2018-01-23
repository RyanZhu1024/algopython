class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == None or p == None:
            return False
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)]for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2] if i > 1 else True #fill first row，i - 2 为了匹配空字符串
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #处理 . 和 字符相等的情况
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 处理 * 情况
                elif p[j - 1] == '*' and j > 1:
                    '''
                    dp[i][j - 2] 匹配空字符串
                    dp[i - 1][j] 匹配前 i - 1 个字符串和 前 j 个pattern，因为在*的情况下，前 i - 1 必须先匹配，才能保证之后的*匹配，
                    因为*代表 preceding letters
                    s[i - 1] == p[j - 2] or p[j - 2] == '.' 代表的就是 preceding letter
                    '''
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return dp[m][n]