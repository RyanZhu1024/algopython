class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        counter = collections.Counter(s)
        res = 0
        odd = 0
        for key in counter:
            if counter[key] % 2 == 0:
                res += counter[key]
            else:
                res += (counter[key] - 1)
                odd = max(odd, counter[key])
        return res + 1 if odd > 0 else res