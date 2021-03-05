# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
#
# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.

# The path must contain at least one node.

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaxSum:
    def __init__(self):
        self.max_sum = -math.inf


def find_maximum_path_sum(root):

    def find_max_sum_path(root):
        if root is None:
            return 0

        lsum = find_max_sum_path(root.left)
        rsum = find_max_sum_path(root.right)

        max_sum.max_sum = max(max_sum.max_sum, max(lsum + root.val, rsum + root.val))
        max_sum.max_sum = max(max_sum.max_sum, lsum + root.val + rsum)

        return lsum + rsum + root.val

    max_sum = MaxSum()

    find_max_sum_path(root)
    return max_sum.max_sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


if __name__ == '__main__':
    main()
