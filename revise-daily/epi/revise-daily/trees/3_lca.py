from collections import namedtuple


def lowest_common_ancestor(tree, p, q):

    Status = namedtuple('Status', ('lca_node', 'target_nodes_covered'))
    def find_lca(tree):

        left_res = find_lca(tree.left)

        if left_res.target_nodes_covered == 2:
            return left_res.lca_node

        right_res = find_lca(tree.right)

        if right_res.target_nodes_covered == 2:
            return right_res.lca_node

        number_of_nodes_covered = left_res.target_nodes_covered + right_res.target_nodes_covered + (p, q).count(tree.val)
        if number_of_nodes_covered == 2:
            return Status(tree, number_of_nodes_covered)

        return Status(None, number_of_nodes_covered)
