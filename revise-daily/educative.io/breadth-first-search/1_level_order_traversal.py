from collections import deque


class TreeNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def traverse(root):

    q = deque([root])
    result = []

    while q:
        n = len(q)
        current_level = []
        for _ in range(n):
            p = q.popleft()
            current_level.append(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        result.append(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


if __name__ == '__main__':
    main()
