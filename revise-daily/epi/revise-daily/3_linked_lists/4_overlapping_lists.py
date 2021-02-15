class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def over_lapping_lists(l1, l2):
    while l1.next is not None:
        l1 = l1.next
    l1.next =
    while l2 != l1:
        if l2.next is None:
            return False
        l2 = l2.next

    return l2 == l1


