# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        import heapq
        class HeapItem:
            def __init__(self, it):
                self.interval = it
            def __lt__(self, other):
                return self.interval.end < other.interval.end
        intervals.sort(key=lambda it: it.start)
        q = []
        for it in intervals:
            if q and it.start >= heapq.nsmallest(1, q)[0].interval.end:
                heapq.heappop(q)
            heapq.heappush(q, HeapItem(it))
        return len(q)