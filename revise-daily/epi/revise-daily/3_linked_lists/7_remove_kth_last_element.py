class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def remove_kth_last_element(l1: ListNode, k: int):
    dummy = ListNode(0, l1)
    first = dummy.next

    for _ in range(k):
        first = first.next

    second = dummy
    while first:
        first, second = first.next, second.next

    second.next = second.next.next
    return dummy.next
