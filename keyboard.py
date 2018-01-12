class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        row2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        row3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        res = []
        for word in words:
            if self.testrow(word, row1) or self.testrow(word, row2) or self.testrow(word, row3):
                res += [word]
        return res

    def testrow(self, word, row):
        for c in word:
            if c.lower() not in row:
                return False
        return True

print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))