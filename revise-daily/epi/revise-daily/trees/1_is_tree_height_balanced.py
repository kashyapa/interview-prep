import math
from collections import namedtuple


def is_tree_height_balanced(root):
    Status = namedtuple('Status', ('balanced', 'height'))

    def check_balanced(tree):

        if not tree:
            return Status(True, 0)

        left_result = check_balanced(tree.left)

        if not left_result.balanced:
            return Status(False, left_result.height)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return Status(False, right_result.height)

        status = abs(left_result.height - right_result.height) <= 1

        return Status(status, max(left_result.height, right_result.height) + 1)

    return check_balanced(root).status

