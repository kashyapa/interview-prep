# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each
# path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from
# parent to child (top to bottom).


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    def find_paths_to_sum(root, path):

        if root is None:
            return

        path.append(root.val)
        sum_val = 0
        for i in range(len(path)-1, -1, -1):
            sum_val += path[i]
            if sum_val == S:
                result.append(path.copy())
                return True

        find_paths_to_sum(root.left, path)
        find_paths_to_sum(root.right, path)
        path.pop()

        return

    result = []
    find_paths_to_sum(root, [])
    return len(result)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
