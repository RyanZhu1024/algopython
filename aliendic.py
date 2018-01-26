import collections


class Node:
    def __init__(self, c):
        self.c = c
        self.degree = 0
        self.children = set()

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        table = {}
        for word in words:
            nodes = map(lambda c: Node(c), word)
            for node in nodes:
                if node.c not in table:
                    table[node.c] = node
        for i in range(0, len(words) - 1):
            preWord, nextWord = words[i], words[i + 1]
            length = min(map(len, [preWord, nextWord]))
            for j in range(length):
                preC, nextC = preWord[j], nextWord[j]
                if preC != nextC:
                    if table[nextC] not in table[preC].children:
                        table[preC].children.add(table[nextC])
                        table[nextC].degree += 1
                    break
        res = []
        q = collections.deque()
        for key in table:
            if table[key].degree == 0:
                q.append(table[key])
        if not q:
            return ""
        while q:
            head = q.popleft()
            res += [head.c]
            for child in head.children:
                child.degree -= 1
                if child.degree == 0:
                    q.append(child)
        return "".join(res) if len(res) == len(table) else ""

print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))