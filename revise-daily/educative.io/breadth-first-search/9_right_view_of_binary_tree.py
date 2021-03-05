class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


from collections import deque


def tree_right_view(root):
    queue = deque()

    queue.append(root)
    result = []
    while queue:
        n = len(queue)
        for i in range(0, n):
            p = queue.popleft()
            if i == n-1:
                result.append(p)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


if __name__ == '__main__':
    main()
