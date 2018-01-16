import string


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 0
        if wordList is None or len(wordList) == 0:
            return 0
        ladder = 1
        q = [beginWord, None]
        dic = set(wordList)
        dic.add(endWord)
        if beginWord in dic:
            dic.remove(beginWord)
        while q:
            current = q.pop(0)
            if current == endWord:
                return ladder
            if not current:
                if q:
                    q.append(None)
                    ladder += 1
                else:
                    break
            else:
                for i in range(len(current)):
                    for c in string.ascii_letters:
                        if current[i] != c:
                            candidate = current[:i] + c + current[i + 1:]
                            if candidate in dic:
                                q.append(candidate)
                                dic.remove(candidate)
        return 0


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
