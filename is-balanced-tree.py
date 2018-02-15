# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node):
            if not node:
                return (0, True)
            left = check(node.left)
            right = check(node.right)
            height = max(left, right, key=lambda x: x[0])[0] + 1
            balance = left[1] and right[1] and abs(left[0] - right[0]) < 2
            return (height, balance)
        return check(root)[1]
            
