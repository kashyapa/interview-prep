def has_path_sum(tree, target):
    if not tree:
        return target == 0

    target -= tree.val

    if not tree.left and not tree.right:
        return target == 0

    return has_path_sum(tree.left, target) or has_path_sum(tree.right, target)
