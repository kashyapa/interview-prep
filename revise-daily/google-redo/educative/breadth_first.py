from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def level_order_traversal(root):
    queue = deque([root])
    res = []
    while queue:
        cur_level = []
        n = len(queue)
        for i in range(n):
            p = queue.popleft()
            cur_level.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        res.append(cur_level)
    return res


def reverse_level_order_traversal(root):
    res = []
    queue = deque([root])
    while queue:
        cur_level = []
        n = len(queue)
        for i in range(n):
            cur_level.append(queue.popleft())

        res.insert(0, cur_level)
    return res


def zigzag_level_order_traversal(root):
    queue = deque([root])
    res = []
    ltr = False
    while queue:
        n = len(queue)
        cur_level = []
        for _ in range(n):
            p = queue.popleft()
            if ltr:
                cur_level.append(p)
            else:
                cur_level.insert(0, p)
        ltr = not ltr
        res.append(cur_level)
    return res


def zigzag_traversal(root):
    stack1, stack2 = deque([root]), deque([])
    res = []
    ltr = True

    while stack1:
        for _ in range(len(stack1)):
            p = stack1.pop()
            print(p.val)
            if ltr:
                if p.left:
                    stack2.append(p.left)
                if p.right:
                    stack2.append(p.right)
            else:
                if p.right:
                    stack2.append(p.right)
                if p.left:
                    stack2.append(p.left)
        ltr = not ltr
        stack1, stack2 = deque(), stack1


def level_averages(root):

    queue = deque([root])
    res = []
    while queue:
        n = len(queue)
        r_sum = 0
        for _ in range(n):
            p = queue.popleft()
            r_sum += p.val
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        res.append(r_sum//n)
    return res


def minimum_depth(root):
    queue = deque([root])
    depth = 0
    while queue:

        n = len(queue)
        for _ in range(n):
            p = queue.popleft()
            if not p.left and not p.right:
                return depth
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        depth += 1
    return depth


def connect_level_order_siblings(root):

    queue = deque([root])
    while queue:
        prev = None
        n = len(queue)
        for _ in range(n):
            p = queue.popleft()
            if prev:
                prev.next = p
            p = prev
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
    return root


def connect_all_level_order_siblings(root):
    queue = deque([root])
    prev, cur = None, None

    while queue:
        cur = queue.popleft()

        if prev:
            prev.next = cur
        prev = cur
        if p.left:
            queue.append(p.left)
        if p.right:
            queue.append(p.right)
    return


def find_level_order_successor(root, target):
    queue = deque([root])
    while queue:

        n = len(queue)

        for _ in range(n):
            p = queue.popleft()

            if p.val == target:
                break

            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

    return queue[0] if queue else None


def right_view_of_binary_tree(root):

    queue = deque([root])
    res = []

    while queue:
        n = len(queue)

        for i in range(n):
            p = queue.popleft()

            if i == n-1:
                res.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
    return res
