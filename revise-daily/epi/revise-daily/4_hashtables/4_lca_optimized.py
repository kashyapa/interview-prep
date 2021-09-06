class BinaryTreeNode:
    def __init__(self, val, n0, n1, p):
        self.data = val
        self.right = None
        self.left = None
        self.parent = None


def optimized_lca(n0: BinaryTreeNode, n1: BinaryTreeNode):
    nodes_on_path = set()
    while n0 or n1:
        if n0 in nodes_on_path:
            return n0
        nodes_on_path.add(n0)
        n0 = n0.parent

        if n1 in nodes_on_path:
            return n1
        nodes_on_path.add(n1)
        n1 = n1.parent
    raise ValueError("n0 and n1 not in same tree")
import string