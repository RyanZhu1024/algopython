class Union(object):
    def __init__(self):
        self.parents = {}
        self.weights = {}
        self.count = 0

    def add(self, node):
        self.parents[node] = node
        self.weights[node] += 1
        self.count += 1

    def root(self, node):
        while self.parents[node] != node:
            # path compression
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]

    def unite(self, p, q):
        rootp, rootq = self.root(p), self.root(q)
        if rootp == rootq:
            return
        if self.weights[rootp] > self.weights[rootq]:
            rootp, rootq = rootq, rootp
        self.parents[rootp] = rootq
        self.weights[rootq] += self.weights[rootp]
        self.count -= 1