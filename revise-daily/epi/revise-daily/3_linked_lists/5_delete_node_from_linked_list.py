class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def delete_node_from_linked_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next


if __name__ == '__main__':
    A = ListNode(7, None)
    B = ListNode(6, A)
    C = ListNode(5, B)
    D = ListNode(4, C)
    E = ListNode(3, D)
    F = ListNode(2, E)
    G = ListNode(1, F)

    delete_node_from_linked_list(D)

    while G and G.next:
        if G is None:
            break
        print(str(G.data) + "-->" + str(G.next.data))
        G = G.next
