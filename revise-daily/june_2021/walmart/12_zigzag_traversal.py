from collections import deque


def zigzag_traversal(tree):

    stack1, stack2 = deque(), deque()

    stack1.append(tree)
    ltor = True

    while stack1:
        l = len(stack1)
        for _ in range(l):
            p = stack1.pop()
            print(p.val)
            if ltor:
                if p.left:
                    stack2.append(p.left)
                if p.right:
                    stack2.append(p.right)
            else:
                if p.right:
                    stack2.append(p.right)
                if p.left:
                    stack2.append(p.left)
        stack1, stack2 = stack2, stack1
        ltor = not ltor
    return
