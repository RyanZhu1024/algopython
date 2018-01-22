class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0
        self.dic = {}

    def insert(self, node):
        self.moveToHead(node)
        self.size += 1

    def evict(self):
        last = self.tail.pre
        self.breakLink(last)
        self.size -= 1
        del self.dic[last.key]

    def breakLink(self, node):
        pre = node.pre
        nxt = node.next
        if not pre:
            print(node.key, node.val, pre, nxt)
        pre.next = nxt
        nxt.pre = pre
        node.next = None
        node.pre = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.breakLink(node)
        self.moveToHead(node)
        return node.val

    def moveToHead(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        node.next.pre = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.breakLink(node)
            self.moveToHead(node)
        else:
            node = Node(value, key)
            if self.size == self.capacity:
                self.evict()
            self.dic[key] = node
            self.insert(node)
