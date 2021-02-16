class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p

def reverse(P: ListNode):
    dummy = ListNode(0, P)
    cur = dummy.next

    while cur and cur.next:
        next_p = cur.next
        cur.next = next_p.next
        next_p.next = dummy.next
        dummy.next = next_p

    return dummy.next


def is_linked_list_palindromic(G):
    first, second = G, G
    while second and second.next:
        first, second = first.next, second.next.next

    first, second = G, reverse(first)

    while first and second:
        if first.data != second.data:
            return False
        first, second = first.next, second.next
    return


if __name__ == '__main__':
    A = ListNode(7, None)
    B = ListNode(6, A)
    C = ListNode(5, B)
    D = ListNode(4, C)
    E = ListNode(3, D)
    F = ListNode(2, E)
    G = ListNode(1, F)

    is_linked_list_palindromic(G)

    while G and G.next:
        if G is None:
            break
        print(str(G.data) + "-->" + str(G.next.data))
        G = G.next
