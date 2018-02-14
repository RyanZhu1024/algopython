# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        self.index = 0
        self.sign = 1
        st = []
        def getNum(s):
            i = self.index
            while i < len(s) and s[i].isdigit():
                i += 1
            num = int(s[self.index: i]) * self.sign
            self.sign = 1
            self.index = i
            return num
        while self.index < len(s):
            if s[self.index].isdigit():
                num = getNum(s)
                node = TreeNode(num)
                if st:
                    if not st[-1].left:
                        st[-1].left = node
                    else:
                        st[-1].right = node
                st.append(node)
            elif s[self.index] == '-':
                self.sign = -1
                self.index += 1
            elif s[self.index] == ')':
                st.pop()
                self.index += 1
            elif s[self.index] == '(':
                self.index += 1
        return st[-1]

                
