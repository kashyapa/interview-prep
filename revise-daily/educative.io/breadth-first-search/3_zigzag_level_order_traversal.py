from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def zigzag_level_order(root):
    left_to_right = True
    q = deque()
    q.append(root)
    result = []

    while q:
        n = len(q)
        current_lvl = []
        for _ in range(n):
            p = q.popleft()
            if left_to_right:
                current_lvl.append(p.val)
            else:
                current_lvl.insert(0, p.val)

            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

        left_to_right = not left_to_right
        result.append(current_lvl)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(zigzag_level_order(root)))


if __name__ == '__main__':
    main()
