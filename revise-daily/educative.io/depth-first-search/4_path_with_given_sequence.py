# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):

    def find_path_rec(root, index):
        if root is None:
            return False

        if index == len(sequence) - 1 and root.val == sequence[index]:
            return root.left is None and root.right is None

        if root.val == sequence[index]:
            return find_path_rec(root.right, index+1) or find_path_rec(root.left, index+1)

        return False

    return find_path_rec(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


if __name__ == '__main__':
    main()
