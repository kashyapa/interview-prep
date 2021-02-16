class ListNode:
    def __init__(self, data, p):
        self.data = data
        self.next = p


def delete_node_from_linked_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next

