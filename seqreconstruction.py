from collections import defaultdict
from collections import deque
class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        graph, indegree = defaultdict(list), defaultdict(int)
        for seq in seqs:
            for i, c in enumerate(seq):
                if i > 0:
                    graph[seq[i - 1]] += [c]
                    indegree[c] += 1
        if len(org) != len(indegree):
            return False
        q = deque()
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
        k = 0
        while q:
            if len(q) > 1:
                return False
            item = q.popleft()
            if org[k] != item:
                return False
            for nb in graph[item]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
            k += 1
        return k == len(org)

Solution().sequenceReconstruction([1,2,3],  [[1,2],[1,3],[2,3]])