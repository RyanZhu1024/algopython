class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b:
            return ''
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 and j >= 0:
            val = int(a[i]) + int(b[j]) + carry
            res += [val % 2]
            carry = val // 2
            i -= 1
            j -= 1
        while i >= 0:
            val = int(a[i]) + carry
            res += [val % 2]
            carry = val // 2
            i -= 1
        while j >= 0:
            val = int(b[j]) + carry
            res += [val % 2]
            carry = val // 2
            j -= 1
        if carry == 1:
            res += [1]
        return "".join(map(str, res[::-1]))

print(Solution().addBinary("11", "1"))