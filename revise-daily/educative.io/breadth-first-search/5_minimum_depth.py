from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0

    queue = deque()
    minimum_depth = 0
    queue.append(root)

    while queue:

        lvl_size = len(queue)
        minimum_depth += 1
        for _ in range(lvl_size):
            p = queue.popleft()
            if not p.left and not p.right:
                return minimum_depth
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

    return minimum_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
