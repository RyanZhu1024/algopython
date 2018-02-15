# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.totalMax = -sys.maxsize
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxVal = max(node.val, left + node.val, right + node.val)
            self.totalMax = max(self.totalMax, maxVal, node.val + left + right)
            return maxVal
        dfs(root)
        return self.totalMax
