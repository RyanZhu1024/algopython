# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def pathSum(self, root, k):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.counter = collections.Counter()
        self.counter[0] = 1
        self.res = 0
        def dfs(node, total):
            if not node:
                return
            total += node.val
            self.res += self.counter[total - k]
            self.counter[total] += 1
            dfs(node.left, total)
            dfs(node.right, total)
            self.counter[total] -= 1
        dfs(root, 0)
        return self.res
