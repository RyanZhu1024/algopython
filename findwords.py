class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0] or not words:
            return []

        class Trie:
            def __init__(self):
                self.children = [None for _ in range(26)]
                self.word = None

        root = Trie()
        self.res = []

        def buildTrie(word):
            current = root
            for c in word:
                index = ord(c) - 97
                if not current.children[index]:
                    current.children[index] = Trie()
                current = current.children[index]
            current.word = word

        for word in words:
            buildTrie(word)

        def dfs(i, j, trie):
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return
            c = board[i][j]
            if c == '#' or trie.children[ord(c) - 97] is None:
                return
            nextTrie = trie.children[ord(c) - 97]
            if nextTrie.word:
                self.res += [nextTrie.word]
                nextTrie.word = None
            board[i][j] = '#'
            dfs(i + 1, j, nextTrie)
            dfs(i - 1, j, nextTrie)
            dfs(i, j - 1, nextTrie)
            dfs(i, j + 1, nextTrie)
            board[i][j] = c

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return self.res


print(Solution().findWords([
    ['h', 'a', 'a', 'n'],
    ['e', 't', 'a', 'b'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain", "ath"]))
