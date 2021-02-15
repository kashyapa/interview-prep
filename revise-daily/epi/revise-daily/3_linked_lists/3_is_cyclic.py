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
    p = slow
    loop_count = 0
    while True:
        p = p.next
        loop_count += 1
        if p == slow:
            break

    start, end = l, l

    while loop_count != 0:
        end = end.next
        loop_count -= 1

    while start is not end:
        start = start.next
        end = end.next

    return start

