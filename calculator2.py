class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        number = 0
        sign = 1
        if not s:
            return res
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                number = number * 10 + int(c)
                i += 1
            elif c == '+':
                res += number * sign
                sign = 1
                number = 0
                i += 1
            elif c == '-':
                res += number * sign
                sign = -1
                number = 0
                i += 1
            elif c == '*':
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                number = number * int(s[i + 1: j])
                i = j
            elif c == '/':
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                number = number // int(s[i + 1: j])
                i = j
            else:
                i += 1
        res += number * sign
        return res

print(Solution().calculate(" 3 / 2 "))