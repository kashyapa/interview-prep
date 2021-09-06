class ListNode:
    def __init__(self, val):
        self.val = val
        self.other = None
        self.next = None

def copy_linked_list(lnode):
    clone = {}
    head = lnode
    while lnode and lnode.next:
        clone_node = ListNode(lnode.val)
        clone[lnode.val] = clone_node
        lnode = lnode.next

    lnode = head
    while lnode:
        cl = clone[lnode]
        cl.next = clone[lnode.next] if lnode.next !=  None else None
        cl.other = clone[lnode.other] if lnode.other != None else None
        lnode = lnode.next

    return clone[head]


