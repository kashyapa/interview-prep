class ListNode:
    def __init__(self, val, next, other):
        self.val = val
        self.next = next
        self.other = other


def copy_postings_list(l1):
    dummy_head = ListNode(-1, l1, None)
    clone_map = {}

    while l1:
        clone_node = ListNode(l1.val, None, None)
        clone_map[l1] = clone_node

        l1 = l1.next
    
    l1 = dummy_head.next
    
    while l1:
        clone_node = clone_map[l1]
        clone_node.next = clone_map[l1.next] if l1.next else None
        clone_node.other = clone_map[l1.other] if l1.other else None
        