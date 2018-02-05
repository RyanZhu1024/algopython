class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return ['']
        q = [s]
        success = False
        res = []
        def valid(ss):
            cnt = 0
            for c in ss:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    if cnt == 0:
                        return False
                    else:
                        cnt -= 1
            return cnt == 0
        while q and not success:
            nextLevel = set()
            while q:
                temp = q.pop(0)
                if valid(temp):
                    res += [temp]
                    success = True
                if not success:
                    for i in range(len(temp)):
                        if temp[i] in ('(', ')'):
                            nextLevel.add(temp[0: i] + temp[i + 1:])
            q = list(nextLevel)
        return res