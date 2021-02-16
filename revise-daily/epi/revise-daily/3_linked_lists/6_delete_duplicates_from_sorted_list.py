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

if __name__ == '__main__':
    A = ListNode(7, None)
    B = ListNode(6, A)
    C = ListNode(5, B)
    D = ListNode(4, C)
    E = ListNode(3, D)
    F = ListNode(2, E)
    G = ListNode(1, F)

    delete_duplicates(G)

    while G and G.next:
        if G is None:
            break
        print(str(G.data) + "-->" + str(G.next.data))
        G = G.next