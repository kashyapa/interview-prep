class ListNode:
    def __init__(self, val, next, jump):
        self.val = val
        self.next = next
        self.jump = jump


def copy_postings_list(postings: ListNode):
    dummy = ListNode(-1, postings, None)

    l1 = postings
    while l1:
        clone = ListNode(l1.val, l1.next, None)
        l1.next = clone

    l1 = postings
    while l1:
        l1.next.jump = l1.jump.next     # (l1.jump.next = clone(l1.jump)
        l1 = l1.next.next

    l1 = postings
    l2 = l1.next
    dummy2 = ListNode(-1, l2, None)
    while l1:
        l1.next = l2.next
        l1 = l1.next
        l2 = l1.next
    return dummy2.next

