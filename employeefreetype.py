# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        def merge(intervals):
            i = 0
            res = []
            while i < len(intervals):
                current = intervals[i]
                j = i + 1
                while j < len(intervals) and intervals[j].start <= current.end:
                    current.end = max(current.end, intervals[j].end)
                    j += 1
                res.append(current)
                i = j
            return res
        intervals = []
        for sch in schedule:
            intervals += sch
        intervals.sort(key=lambda interval: interval.start)
        merged = merge(intervals)
        res = []
        begin, end = merged[0].end, None
        for i in range(1, len(merged)):
            end = merged[i].start
            res.append([begin, end])
            begin = merged[i].end
        return res


class QueueItem(object):
    """docstring for QueueItem."""
    def __init__(self, empNo, interval, index):
        super(QueueItem, self).__init__()
        self.employeeNumber = empNo
        self.interval = interval
        self.index = index
    def __lt__(self, other):
        return self.interval.start < other.interval.start

def employeeFreeTime(schedule):
    """
    :type schedule: List[List[Interval]]
    :rtype: List[Interval]
    """
    from queue import PriorityQueue
    q = PriorityQueue()
    for i, sch in enumerate(schedule):
        if len(sch) > 0:
            q.put(QueueItem(i, sch[0], 0))
    res = []
    curInterval = None
    while not q.empty() > 0:
        item = q.get()
        if curInterval is None:
            curInterval = item.interval
        elif item.interval.start <= curInterval.end:
            curInterval.end = max(curInterval.end, item.interval.end)
        else:
            res.append([curInterval.end, item.interval.start])
            curInterval = item.interval
        if item.index + 1 < len(schedule[item.employeeNumber]):
            item.index += 1
            item.interval = schedule[item.employeeNumber][item.index]
            q.put(item)
    return res
