# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return None
        st = []
        num = None
        res = None
        sign = 1
        for c in s:
            if c.isdigit():
                num = int(c) if num is None else num * 10 + int(c)
            else:
                if num is not None:
                    val = num * sign
                    if st:
                        st[-1].add(NestedInteger(val))
                    else:
                        st += [NestedInteger(val)]
                    num = None
                    sign = 1
                if c == '[':
                    st += [NestedInteger()]
                elif c == ']':
                    top = st.pop()
                    if st:
                        st[-1].add(top)
                    else:
                        res = top
                elif c == '-':
                    sign = -1
        if num:
            return NestedInteger(num * sign)
        return res
