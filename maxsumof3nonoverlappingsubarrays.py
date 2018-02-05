import sys


class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or 3 * k > len(nums):
            return []
        n = len(nums)
        sums = [0 for _ in range(n - k + 1)]
        sums[0] = sum(nums[: k])
        for i in range(1, len(sums)):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i + k - 1]
        dpfront = [[-sys.maxsize, 0] for _ in range(len(sums))]
        dpback = [[-sys.maxsize, 0] for _ in range(len(sums))]
        dpfront[0] = [sums[0], 0]
        dpback[len(dpback) - 1] = [sums[len(sums) - 1], len(sums) - 1]
        for i in range(1, len(dpfront)):
            dpfront[i] = max(dpfront[i - 1], [sums[i], i], key=lambda item: item[0])
        for i in range(len(dpback) - 2, -1, -1):
            dpback[i] = max(dpback[i + 1], [sums[i], i], key=lambda item: item[0])
        res, maxVal = [], -sys.maxsize
        for i in range(k, len(sums) - k):  # for non overlapping subarray, we start from k
            if sums[i] + dpfront[i - k][0] + dpback[i + k][0] > maxVal:
                res = [dpfront[i - k][1], i, dpback[i + k][1]]
                maxVal = sums[i] + dpfront[i - k][0] + dpback[i + k][0]
        return res
