class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) < k:
            return 0
        dic = {0: -1}
        total = 0
        size = 0
        for i, v in enumerate(nums):
            total += v
            if total not in dic:
                dic[total] = i
            if total - k in dic:
                size = max(size, i - dic[total - k])
        return size