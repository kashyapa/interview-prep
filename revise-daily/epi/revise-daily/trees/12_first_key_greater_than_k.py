def first_key_greater_than(tree, k):
    first_greater_than = None

    while tree:

        if tree.data > k:
            first_greater_than = tree.val
            tree = tree.left
        else:
            tree = tree.right
    return first_greater_than
        