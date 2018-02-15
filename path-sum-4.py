class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curDepth = 2
        total = 0
        curDepthList = [TreeNode(nums[0] % 10)]
        i = 1
        while i < len(nums):
            nextList = [None for _ in range(2 ** (curDepth - 1))]
            j = i
            while j < len(nums):
                if nums[j] // 100 > curDepth:
                    break
                j += 1
            subList = nums[i: j]
            curDepth += 1
            i = j
            for n in subList:
                pos = (n // 10) % 10
                val = n % 10
                node = TreeNode(val)
                nextList[pos - 1] = node
                if pos % 2 == 0:
                    parentPos = (pos - 2) // 2
                    curDepthList[parentPos].right = node
                    node.val += curDepthList[parentPos].val
                else:
                    parentPos = (pos - 1) // 2
                    curDepthList[parentPos].left = node
                    node.val += curDepthList[parentPos].val
            for cur in curDepthList:
                if cur and cur.left is None and cur.right is None:
                    total += cur.val
            curDepthList = nextList
        for cur in curDepthList:
            if cur:
                total += cur.val
        return total
