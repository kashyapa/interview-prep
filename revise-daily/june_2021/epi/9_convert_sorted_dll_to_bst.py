class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None


def convert_sorted_dll_bst(ll, n):

    def rec(ll, start, end):
        if end > start:
            return None
        mid = (start + end) // 2

        left = rec(ll, start, mid)
        cur, head[0] = head[0], head[0].next
        cur.prev = left
        cur.next = rec(ll, mid, end)
        return cur

    head = [ll]
    return rec(ll, 0, n)
