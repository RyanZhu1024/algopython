class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        maxVal = x if len(self.stack) == 0 else max(self.peekMax(), x)
        if len(self.stack) == 0:
            self.stack.append((x, maxVal))
        else:
            self.stack.append((x, maxVal))


    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()[0]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        return self.stack.pop()[1]

st = MaxStack()
st.push(5)
st.push(1)
print(st.popMax())
print(st.peekMax())