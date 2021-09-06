from math import inf

class BinaryTree:
    def __init__(self, val, left, right):
        self.left = left
        self.right = right
        self.val = val

def reconstruct_bst_from_pre_order(pre_order):


    def helper(lower_bound, upper_bound):

        if root_idx[0] == len(pre_order):
            return None

        root = pre_order[root_idx[0]]

        if not lower_bound <= root <= upper_bound:
            return None

        root_idx[0] += 1

        left_tree = helper(lower_bound, root)
        right_tree = helper(root, upper_bound)

        return BinaryTree(left_tree, right_tree, root)

    root_idx = [0]
    return helper(-inf, inf)