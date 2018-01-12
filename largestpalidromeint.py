class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        maxVal = 10 ** (n * 2) - 1
        minVal = 10 ** ((n - 1) ** 2)
        begin = 10 ** (n - 1)
        end = 10 ** (n) - 1
        for i in range(maxVal, minVal - 1, -1):
            for j in range(end, begin - 1, -1):
                if end >= int(i / j) >= begin and i % j == 0 and str(i) == str(i)[::-1]:
                    print(j)
                    return i % 1337
        return -1

print(Solution().largestPalindrome(2))


class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: (y+x, x+y))
        return ''.join(num).lstrip('0') or '0'