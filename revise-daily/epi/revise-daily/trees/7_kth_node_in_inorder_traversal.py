def kth_node_inorder_traversal(tree, k):

    while tree:
        left_tree_count = tree.left.count

        if left_tree_count == k-1:
            return tree

        if left_tree_count < k-1:
            k -= left_tree_count+1
            tree = tree.right
        else:
            tree = tree.left
    return None