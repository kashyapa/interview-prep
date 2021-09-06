class ListNode:
    def __init__(self, data ):
        self.data = data
        self.next = None


def even_odd_merge(L:ListNode):

    even = L
    odd = even.next
    odd_head = odd
    while even.next and odd.next:
        even.next = odd.next
        even = even.next
        odd.next = even.next
        odd = odd.next
    even.next = odd_head

