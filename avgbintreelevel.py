import collections
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        q.append(None)
        bfs = []
        res = []
        while q:
            node = q.popleft()
            if node is None:
                res += [(sum(bfs) / len(bfs))]
                bfs = []
                if len(q) > 0:
                    q.append(None)
            else:
                bfs += [node.val]
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return res
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
Solution().averageOfLevels(root=TreeNode(1))