class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def is_cyclic(l1: ListNode):
    slow, fast = l1, l1

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return find_loop_node(l, slow)

    return None


def find_loop_node(l, slow):
    fast, slow = l, l
    while True:

