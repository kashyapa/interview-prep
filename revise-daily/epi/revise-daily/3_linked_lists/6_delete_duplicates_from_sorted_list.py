class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def delete_duplicates(l1: ListNode):
    dummy = ListNode()
    dummy.next = l1

    while l1:
        next_distinct = l1.next
        while next_distinct and l1.data == next_distinct.data:
            next_distinct = next_distinct.next
        l1.next = next_distinct
        l1 = l1.next

    return dummy.next
