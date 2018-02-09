
import itertools
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        self.lt20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        self.gte20 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.thousands = ['', 'Thousand', 'Million', 'Billion']
        def process(n):
            if n < 20:
                return [self.lt20[n]]
            elif n < 100:
                p1 = n % 10
                p2 = n // 10
                return [self.lt20[p1], self.gte20[p2]]
            else:
                p1 = n // 100
                return itertools.chain(process(n % 100), ['Hundred', self.lt20[p1]])
        res = []
        unit = 0
        while num > 0:
            todo = num % 1000
            num = num // 1000
            if todo > 0:
                res = itertools.chain(res, [self.thousands[unit]], process(todo))
                # res += [self.thousands[unit]]
                # res += process(todo)
            unit += 1
        result = [x for x in res if x != '']
        return " ".join(result[::-1])

print(Solution().numberToWords(1234567))