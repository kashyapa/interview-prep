class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def remove_kth_last_element(l1: ListNode, k: int):
    dummy = ListNode(0, l1)
    first = dummy.next

    for _ in range(k):
        first = first.next

    second = dummy
    while first:
        first, second = first.next, second.next

    second.next = second.next.next
    return dummy.next


if __name__ == '__main__':
    A = ListNode(7, None)
    B = ListNode(6, A)
    C = ListNode(5, B)
    D = ListNode(4, C)
    E = ListNode(3, D)
    F = ListNode(2, E)
    G = ListNode(1, F)

    remove_kth_last_element(G, 3)

    while G and G.next:
        if G is None:
            break
        print(str(G.data) + "-->" + str(G.next.data))
        G = G.next
