# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.count = 0
    def isUnivalue(self, node):
        if not node:
            return False
        l = node.val == node.left.val and self.isUnivalue(node.left) if node.left else True
        r = node.val == node.right.val and self.isUnivalue(node.right) if node.right else True
        return l and r


    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if self.isUnivalue(root):
            self.count += 1
        self.countUnivalSubtrees(root.left)
        self.countUnivalSubtrees(root.right)
        return self.count
