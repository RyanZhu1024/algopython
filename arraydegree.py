import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        maxLen = max([counter[key] for key in counter])
        mostComm = []
        for key in counter:
            if counter[key] == maxLen:
                mostComm.append(key)
        minLen = len(nums)
        for item in mostComm:
            start = nums.index(item)
            end = len(nums) - 1 - nums[::-1].index(item)
            minLen = min(minLen, end - start + 1)
        return minLen

print(Solution().findShortestSubArray([1,2,2,3,1]))