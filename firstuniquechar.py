from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return -1
        orderdic = LastUpdatedOrderedDict()
        for i, c in enumerate(s):
            if c in orderdic:
                pre = orderdic[c]
                orderdic[c] = (i, pre[1] + 1)
            else:
                orderdic[c] = (i, 1)
        first = list(orderdic.items())[0]
        return first[1][0] if first[1][1] == 1 else -1

print(Solution().firstUniqChar("leetcode"))