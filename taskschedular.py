class QueueItem:
    def __init__(self, t, c):
        self.task = t
        self.count = c

    def __lt__(self, other):
        return self.count > other.count

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0
        import heapq
        import collections
        counter = collections.Counter(tasks)
        q = []
        for key in counter:
            heapq.heappush(q, QueueItem(key, counter[key]))
        res = 0
        while q:
            k = n + 1
            tempList = []
            while q and k:
                res += 1
                k -= 1
                item = heapq.heappop(q)
                item.count -= 1
                if item.count > 0:
                    tempList += [item]
            q += tempList
            if not q:
                break
            heapq.heapify(q)
            res += k
        return res


def leastIntervalWithPriorityQueue(tasks, n):
    if not tasks:
        return 0
    from queue import PriorityQueue
    from collections import Counter
    q = PriorityQueue()
    counter = Counter(tasks)
    for key in counter:
        q.put(QueueItem(key, counter[key]))
    res = 0
    while not q.empty():
        tempQueue = []
        k = n + 1
        while not q.empty() and k:
            item = q.get()
            item.count -= 1
            k -= 1
            res += 1
            if item.count > 0:
                tempQueue += [item]
        for it in tempQueue:
            q.put(it)
        if q.empty():
            break
        res += k
    return res

print(leastIntervalWithPriorityQueue(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
