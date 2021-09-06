# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of
# each path equals ‘S’.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):

    allPaths = []

    def find_paths_rec(root, sum, path: list):
        if root is None:
            return
        path += [root.val]
        if sum == root.val and root.left is None and root.right is None:
            allPaths.append(path.copy())
            return
        else:
            find_paths_rec(root.left, sum - root.val, path)
            find_paths_rec(root.right, sum - root.val, path)
            path.pop()
        return

    find_paths_rec(root, sum, [])

    return allPaths


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


if __name__ == '__main__':
    main()
