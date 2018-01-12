class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def getPermutations(w):
            visit = [False for _ in range(len(w))]
            res = []
            dfs(w, "", visit, res)
            return res

        def dfs(w, cur, visit, res):
            if len(cur) == len(w):
                res += [cur]
            for i in range(len(w)):
                if i > 0 and w[i - 1] == w[i] and not visit[i - 1]:
                    continue
                if visit[i]:
                    continue
                visit[i] = True
                dfs(w, cur + w[i], visit, res)
                visit[i] = False

        from collections import Counter
        import itertools as it
        counter = Counter(s)
        odds = []
        halfs = []
        for k, v in counter.items():
            if v % 2 == 1:
                odds += [k]
            halfs += [k * (v // 2)]
        if len(odds) > 1:
            return []
        halfs.sort()
        allperms = getPermutations("".join(halfs))
        ch = ''
        if len(odds) == 1:
            ch = odds[0]
        return list(map(lambda perm: "".join(perm) + ch + "".join(perm[::-1]), allperms))