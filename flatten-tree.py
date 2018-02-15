# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flat(node):
            if not node:
                return node
            if node.left is None and node.right is None:
                return (node, node)
            left = flat(node.left)
            right = flat(node.right)
            head = node
            tail = right[1] if right else left[1]
            node.left = None
            if left and right:
                node.right = left[0]
                left[1].right = right[0]
                tail = right[1]
            elif left:
                node.right = left[0]
                tail = left[1]
            elif right:
                tail = right[1]
            return (head, tail)
        flat(root)
