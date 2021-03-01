from collections import deque


class TreeNode:
    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def level_order_successor(root, key):

    queue = deque()
    queue.append(root)

    while queue:
        length = len(queue)

        for _ in range(length):
            p = queue.popleft()
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

            if p.val == key:
                return queue[0].val
    return None


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(str(level_order_successor(root, 2)))
