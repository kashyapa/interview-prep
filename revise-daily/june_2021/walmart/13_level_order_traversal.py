from collections import deque


def level_order_traversal(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        n = len(queue)
        cur_lvl = []
        for _ in range(n):
            p = queue.popleft()
            cur_lvl.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        res.append(cur_lvl)
    return res

