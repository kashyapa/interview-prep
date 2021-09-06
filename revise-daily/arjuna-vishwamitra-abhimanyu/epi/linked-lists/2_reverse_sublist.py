# reverse nodes between mth node and nth node
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_sublist(l, m, n):
    for _ in range(m):
        l = l.next
    p = l
    cur = l.next
    count = n - m + 1
    for _ in range(count):
        next = cur.next
        cur.next = next.next
        next.next = l.next
        l.next = next
        