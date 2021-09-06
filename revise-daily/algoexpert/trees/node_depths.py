from collections import deque


def nodeDepths(root):
    # Write your code here.
    queue = deque()
    queue.append([(root, 0)])
    sum_of_depths = 0
    while queue:
        p, depth = queue.popleft()

        sum_of_depths += depth

        if p.left:
            queue.append((p.left, depth + 1))
        if p.righ:
            queue.append((p.right, depth + 1))
    return sum_of_depths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


