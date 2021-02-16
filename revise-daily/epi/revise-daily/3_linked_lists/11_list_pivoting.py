class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def list_pivoting(L: ListNode, x: int):

    head, tail = L, L
    temp = None

    while L:
        if L.data < x:
            temp = L.next
            L.next = head
            head = L
        else:
            temp = L.next
            tail.next = L
            tail = L
        L = temp
    tail.next = None
    return head


if __name__ == '__main__':
    A = ListNode(0, None)
    B = ListNode(5, A)
    C = ListNode(2, B)
    D = ListNode(4, C)
    E = ListNode(1, D)
    F = ListNode(6, E)
    G = ListNode(7, F)
    l = []
    head = G
    while G:
        if G is None:
            break
        l.append(str(G.data) + "-->")
        G = G.next
    l.append("none")

    print(''.join(l))

    head = list_pivoting(head, 3)

    l = []
    while head:
        if head is None:
            break
        l.append(str(head.data) + "-->")
        head = head.next
    l.append("none")

    print(''.join(l))
