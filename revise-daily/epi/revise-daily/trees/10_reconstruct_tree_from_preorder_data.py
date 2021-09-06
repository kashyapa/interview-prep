class BinaryTree:
    def __init__(self, val, left, right):
        self.left = left
        self.right = right
        self.val = val


def reconstruct_tree_from_preorder_with_markers(pre_order):

    def helper(pre_order_iter):

        data = next(pre_order_iter)
        if data is None:
            return None

        left_tree = helper(pre_order_iter)
        right_tree = helper(pre_order_iter)

        return BinaryTree(data, left_tree, right_tree)
    helper(iter(pre_order))

