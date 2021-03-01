from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    q = deque()
    q.append(root)
    result = []
    while q:
        n = len(q)
        level_sum = 0.0
        for _ in range(n):
            p = q.popleft()
            level_sum += p.val
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

        result.append(level_sum/n)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


if __name__ == '__main__':
    main()
