# reverse nodes between mth node and nth node
class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def reverse_sublist(l: ListNode, m: int, n: int):
    prev, dummy = ListNode(), ListNode()
    prev.next. dummy.next = l, l
    while m > 0:
        p = p.next
        m -= 1

    cur = prev.next

    while n - m > 0:
        next = cur.next
        cur.next = next.next
        next.next = prev.next
        prev.next = next
        n -= 1
    return dummy.next
