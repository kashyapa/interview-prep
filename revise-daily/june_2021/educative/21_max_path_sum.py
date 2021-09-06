from heapq import *
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math

def max_path_sum(root):
    def rec(node):
        if node is None:
            return 0
        lsum = max(rec(node.left), 0)
        rsum = max(rec(node.right), 0)

        max_sum["max_sum"] = max(max_sum["max_sum"], lsum + rsum + node.val)
        return max(lsum + node.val, rsum + node.val)

    max_sum = {"max_sum": -math.inf}
    rec(root)
    return max_sum["max_sum"]
