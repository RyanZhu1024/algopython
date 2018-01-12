import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = []
        for node in lists:
            if node is not None:
                heapq.heappush(q, (node.val, node))
        dummy = ListNode(None)
        cur = dummy
        while q:
            node = heapq.heappop(q)
            cur.next = node[1]
            cur = cur.next
            if cur.next is not None:
                heapq.heappush(q, (cur.val, cur.next))
        return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)


node = Solution().mergeKLists([n1, n2, n3])
while node:
    print(node.val)
    node = node.next
