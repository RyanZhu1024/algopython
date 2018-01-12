class TreeNode(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0

def gettopk(root, k, target):
    if root is None:
        return []
    res = []
    node = root
    st = []
    while node:
        st.append(node)
        node = node.left

    while st:
        top = st.pop()
        if len(res) == 0 or abs(top.val - target) < abs(res[-1] - target):
            res.append(top.val)
        if len(res) > k:
            res.pop(0)
        if top.right:
            node = top.right
            while node:
                st.append(node)
                node = node.left
    return res