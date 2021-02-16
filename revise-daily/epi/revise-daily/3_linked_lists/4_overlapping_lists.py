class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def get_length(l):
    length = 0
    while l:
        l = l.next
        length += 1
    return length


def over_lapping_lists(l1, l2):
    l1_length = get_length(l1)
    l2_length = get_length(l2)

    if l1_length > l2_length:
        return over_lapping_lists(l2, l1)

    for _ in range(l2_length - l1_length):
        l2 = l2.next

    while l1 and l2 and l1 is not l2:
        l1 = l1.next
        l2 = l2.next

    return l2


