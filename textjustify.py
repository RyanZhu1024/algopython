class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
        if max([len(word) for word in words]) > maxWidth:
            return []
        i = 0
        res = []
        while i < len(words):
            j = i
            curLen = 0
            while j < len(words) and curLen + len(words[j]) <= maxWidth:
                curLen += (len(words[j]) + 1)
                j += 1
            curLen -= 1
            wordCnt = j - i
            temp = []
            if wordCnt == 1:
                temp.append(words[i])
                if maxWidth - len(words[i]) > 0:
                    temp.append(" " * (maxWidth - len(words[i])))
                res.append("".join(temp))
            elif j == len(words):
                temp.append(" ".join(words[i: j]))
                if curLen < maxWidth:
                    temp.append(" " * (maxWidth - curLen))
                res.append("".join(temp))
            else:
                spaces = maxWidth - curLen
                avg = spaces // (wordCnt - 1)
                remain = spaces % (wordCnt - 1)
                for k in range(i, j):
                    temp.append(words[k])
                    if k < j - 1:
                        temp.append(" " * (avg + 1))
                    if remain:
                        temp.append(" ")
                        remain -= 1
                res.append("".join(temp))
            i = j
        return res

print(Solution().fullJustify(["What","must","be","shall","be."], 12))