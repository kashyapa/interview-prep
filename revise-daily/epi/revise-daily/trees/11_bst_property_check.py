def bst_check(tree):

    def helper(tree, max_val, min_val):
        if tree is None:
            return True

        return tree.val > min_val and tree.val < max_val and helper(tree.left, tree.val, min_val) and helper(tree.right, max_val, tree.val)

