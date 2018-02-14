# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.counter = collections.Counter()
        def calTotal(node):
            if not node:
                return 0
            left = calTotal(node.left)
            right = calTotal(node.right)
            total = left + right + node.val
            self.counter[total] += 1
            return total
        calTotal(root)
        freq = self.counter.most_common(1)[0][1]
        res = []
        for key in self.counter:
            if self.counter[key] == freq:
                res += [key]
        return res
