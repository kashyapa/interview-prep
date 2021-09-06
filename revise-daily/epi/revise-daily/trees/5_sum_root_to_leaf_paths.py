def sum_root_to_leaf_paths(tree):
    if not tree:
        return 0

    def sum_root_to_leaf(tree, partial_sum):
        if not tree:
            return 0

        if tree.left is None and tree.right is None:
            return partial_sum

        partial_sum += partial_sum * 2 + tree.val

        return sum_root_to_leaf(tree.left, partial_sum) + sum_root_to_leaf(tree.right, partial_sum)
    return sum_root_to_leaf(tree, 0)