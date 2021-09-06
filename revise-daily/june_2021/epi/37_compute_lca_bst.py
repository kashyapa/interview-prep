class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None

from collections import namedtuple

Result = namedtuple('Result', ('ancestor', 'number_of_targets_seen'))


def compute_lca_bst(node, p1, p2):

    def lca_helper(tree, p1, p2):

        if tree is None:
            return Result(None, 0)

        left_result = lca_helper(tree.left, p1, p2)

        if left_result.number_of_targets_seen == 2:
            return left_result.ancestor

        right_result = lca_helper(tree.right, p1, p2)
        if right_result.number_of_targets_seen == 2:
            return right_result

        num_target_nodes = left_result.number_of_targets_seen + right_result.number_of_targets_seen +\
                           (p1, p2).count(tree)

        return Result(tree if num_target_nodes == 2 else None, num_target_nodes)

    return lca_helper(node, p1, p2).ancestor

