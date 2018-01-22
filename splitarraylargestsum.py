class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(target, nums, m):
            current, count = 0, 0
            for n in nums:
                current += n
                if current > target:
                    count += 1
                    if count >= m:
                        return False
                    current = n
            return True
        def bs(sumLow, sumHigh, m, nums):
            l, r = sumLow, sumHigh
            while l < r:
                mid = l + (r - l) // 2
                if valid(mid, nums, m):
                    r = mid
                else:
                    l = mid + 1
            return l
        sumHigh, singleMax = sum(nums), max(nums)
        return bs(singleMax, sumHigh, m, nums)