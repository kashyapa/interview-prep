from collections import deque


def connect_siblings(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        n = len(queue)
        prev = None
        for _ in range(n):
            p = queue.popleft()
            if prev is None:
                res.append(p)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
            if prev is not None:
                prev.right = p
            prev = p
    return res
