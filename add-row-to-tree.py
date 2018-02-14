class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        else:
            self.nodes = []
            def findNodes(node, d, curd):
                if not node:
                    return
                if curd == d - 1:
                    self.nodes += [node]
                    return
                findNodes(node.left, d, curd + 1)
                findNodes(node.right, d, curd + 1)
            findNodes(root, d, 1)
            for node in self.nodes:
                left, right = node.left, node.right
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                node.left.left = left
                node.right.right = right
            return root
