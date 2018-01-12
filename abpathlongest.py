class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if input is None or len(input) == 0:
            return 0
        res = 0
        segs = input.split("\n")
        stack = []
        for seg in segs:
            tabNum = seg.count("\t")
            seg = seg.replace("\t", "")
            while len(stack) > 0 and stack[-1][1] > tabNum - 1:
                stack.pop()
            if "." in seg:
                abpath = seg if len(stack) == 0 else "/".join([s[0] for s in stack]) + "/" + seg
                res = max(res, len(abpath))
            else:
                directory = (seg, 0) if len(stack) == 0 else (seg, stack[-1][1] + 1)
                stack.append(directory)
        return res

Solution().lengthLongestPath("a\n\tb1\n\t\tf1.txt\n\taaaaa\n\t\tf2.txt")