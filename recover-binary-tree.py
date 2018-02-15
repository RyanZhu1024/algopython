# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.preNode = None
        self.first = None
        self.second = None
        def traverse(curNode):
            if curNode:
                traverse(curNode.left)
                if self.preNode and self.preNode.val > curNode.val:
                    self.first = self.preNode
                if self.first and self.preNode.val > curNode.val:
                    self.second = curNode
                self.preNode = curNode
                traverse(curNode.right)
        traverse(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
