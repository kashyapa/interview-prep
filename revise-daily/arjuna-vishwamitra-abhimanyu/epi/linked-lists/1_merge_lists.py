class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_sorted_lists(l1, l2):
    dummy = ListNode(-1)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
            tail = tail.next
    tail.next = l1 or l2
    return dummy.next


if __name__ == "__main__":
    l1 = ListNode(4)
    head = l1
    l1.next = ListNode(7)
    l1 = l1.next
    l1.next = ListNode(9)


    l2 = ListNode(2)
    head2 = l2
    l2.next = ListNode(10)
    l2 = l2.next
    l2.next = ListNode(54)

    res = merge_sorted_lists(head, head2)
    while res:
        print(res.val)
        res = res.next