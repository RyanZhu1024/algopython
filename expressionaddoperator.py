import itertools
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        slots = len(num) - 1
        combinations = itertools.product(['+', '-', '*', ''], repeat = slots)
        res = []
        for comb in combinations:
            exp = "".join(map(lambda pair: "".join(pair), itertools.zip_longest(num, comb, fillvalue='')))
            try:
                if eval(exp) == target:
                    res += [exp]
            except:
                pass
        return res

print(Solution().addOperators('00', 0))