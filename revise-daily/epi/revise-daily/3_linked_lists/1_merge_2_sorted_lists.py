class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def merge_2_sorted_lists(l1: ListNode, l2: ListNode):
    
    head, tail = ListNode(), ListNode()

    while l1 and l2:
        if l1.data > l2.data:
            if head is None and tail is None:
                l1 = head
                tail = head
            else:
                tail.next = l1
                l1 = l1.next
        elif l2.data < l1.data:
            if head is None and tail is None:
                l2 = head
                head = tail
            else:
                tail.next = l2
                l2 = l2.next
        tail = tail.next
    p = l1 or l2
    tail.next = p
