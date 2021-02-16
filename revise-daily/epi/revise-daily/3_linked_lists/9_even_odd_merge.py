class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def even_odd_merge(L: ListNode):
    if L is None:
        return L

    even = L
    odd = even.next

    odd_head = odd
    while even.next and odd.next:
        even.next = odd.next
        even = even.next

        odd.next = even.next
        odd = odd.next
    even.next = odd_head


if __name__ == '__main__':
    A = ListNode(7, None)
    B = ListNode(6, A)
    C = ListNode(5, B)
    D = ListNode(4, C)
    E = ListNode(3, D)
    F = ListNode(2, E)
    G = ListNode(1, F)

    even_odd_merge(G)

    while G and G.next:
        if G is None:
            break
        print(str(G.data) + "-->" + str(G.next.data))
        G = G.next
