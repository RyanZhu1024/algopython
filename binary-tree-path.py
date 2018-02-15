# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        def dfs(node, curPath):
            if not node:
                return
            if node.left is None and node.right is None:
                curPath = curPath + '->' + str(node.val) if curPath else str(node.val)
                self.res += [curPath]
            else:
                nextPath = str(node.val) if not curPath else curPath + '->' + str(node.val)
                dfs(node.left, nextPath)
                dfs(node.right, nextPath)
        if root:
            dfs(root, "")
        return self.res
