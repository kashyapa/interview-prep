def reconstruct_tree_from_traversal_data(pre_order, in_order):

    def rec(pre_order_start, pre_order_end, in_order_start, inorder_end):

        root = pre_order[pre_order_start]

        number_of_nodes_in_left_subtree = in_order.index(root.val) + 1

        root.left = rec(pre_order_start+1, pre_order_start+1 + number_of_nodes_in_left_subtree, )