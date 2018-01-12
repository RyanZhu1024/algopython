import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        q = []
        for key in counter:
            cnt = counter[key]
            if len(q) < k:
                heapq.heappush(q, (cnt, key))
            else:
                smallest = heapq.nsmallest(1, q)[0]
                if cnt > smallest[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, (cnt, key))
        return [x[1] for x in q]

print(Solution().topKFrequent([1,1,1,2,2,3], 2))