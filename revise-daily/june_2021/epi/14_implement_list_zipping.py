class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def list_zipping(l1, l2):
    tail = ListNode(-1)
    head = tail

    while l1 and l2:
        tail.next = l1
        tail = tail.next

        tail.next = l2
        tail = tail.next

        l1 = l1.next
        l2 = l2.next

    tail.next = l1 if l1 else l2
    return head

