# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        #copy to next
        self.copyToNext(head)
        self.copyRandom(head)
        return self.removeLink(head)

    def copyToNext(self, node):
        while node:
            copy = RandomListNode(node.label)
            copy.next = node.next
            node.next = copy
            node = copy.next

    def copyRandom(self, node):
        while node:
            copy = node.next
            copy.random = node.random.next if node.random is not None else None
            node = copy.next

    def removeLink(self, node):
        dummy = RandomListNode(0)
        current = dummy
        while node:
            copy = node.next
            current.next = copy
            node.next = None
            node = copy.next
            current = current.next
        return dummy.next

x = RandomListNode(-1)
x.random = None
y = Solution().copyRandomList(x)
print(y.label)
print(y.random)
print(y.next)