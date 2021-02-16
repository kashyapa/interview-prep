class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def cyclic_right_shift(L: ListNode, k: int):
    dummy = ListNode(0, L)
    first = dummy.next

    for _ in range(k):
        first = first.next

    second = dummy

    while first and first.next:
        first, second = first.next, second.next

    first.next = L
    L = second.next
    second.next = None
    return L


0