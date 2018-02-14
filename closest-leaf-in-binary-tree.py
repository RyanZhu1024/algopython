# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        self.heights = {}
        self.st = []
        def getHeights(node):
            if node.left is None and node.right is None:
                self.heights[node] = (1, node)
                return self.heights[node]
            left = getHeights(node.left) if node.left else (sys.maxsize, None)
            right = getHeights(node.right) if node.right else (sys.maxsize, None)
            leaf = min(left, right, key=lambda x: x[0])
            pair = (leaf[0] + 1, leaf[1])
            self.heights[node] = pair
            return self.heights[node]
        def findKParents(node):
            if not node:
                return False
            self.st.append(node)
            if node.val == k:
                return True
            if findKParents(node.left):
                return True
            if findKParents(node.right):
                return True
            self.st.pop()
            return False
        getHeights(root)
        findKParents(root)
        res = sys.maxsize
        target = None
        p = 0
        while self.st:
            node = self.st.pop()
            h, leaf = self.heights[node]
            h += p
            p += 1
            if h < res:
                res = h
                target = leaf
        return target.val
