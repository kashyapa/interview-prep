# class ListNode:
#     def __init__(self, val, next, jump):
#         self.val = val
#         self.next = next
#         self.jump = jump
#
#
# def copy_postings_list(l):
#     dummy_head = ListNode(0, l, None)
#     while l:
#         new_node = ListNode(l.val, l.next, None)
#         l.next = new_node
#         l = new_node.next
#
#     l = dummy_head.next
#     while l:
#         l.next.jump = l.jump.next
#         l = l.next.next
#
#     l = dummy_head.next
#     next = l.next
#
#     while l.next:
#         l.next, l = l.next.next, l.next


class ListNode:
    def __init__(self, val, next, other):
        self.val = val
        self.next = next
        self.other = other


def deep_copy(original: [ListNode]):
    dummy_head = ListNode(-1, original, None)

    l1 = original

    while l1 and l1.next:
        # create a copy of current node
        cloned_node = ListNode(l1.val, l1.next, None)
        l1.next = cloned_node

        # move onto next node in the original node
        l1 = l1.next.next

    l1 = dummy_head.next

    while l1 and l1.next:
        # setup other pointer for cloned node
        l1.next.other = l1.other.next  # l1.other.next = "cloned other" node

        # move to next node of original list
        l1 = l1.next.next

    cloned_head = None
    l1 = dummy_head.next
    while l1.next:
        cloned_node = l1.next
        if cloned_head is None:
            cloned_head = cloned_node

        if cloned_node is not None:
            l1.next = cloned_node.next
        if l1.next is not None:
            cloned_node.next = l1.next.next
        else:
            cloned_node.next = None

    return cloned_head

def deep_copy2(l: ListNode):

    clone_map = {}
    dummy_head = ListNode(-1, None, None)
    while l:
        clone_node = ListNode(l.val, None, None)
        clone_map[l] = clone_node
        l = l.next

    l = dummy_head.next

    while l:
        clone_node = clone_map[l]
        clone_node.next = clone_map[l.next]
        clone_node.other = clone_map[l.other]


if __name__ == "__main__":
    tail = ListNode(5, None, None)
    second_node = ListNode(4, tail, None)
    third_node = ListNode(3, second_node, None)
    fourth_node = ListNode(2, third_node, None)
    head = ListNode(1, fourth_node, None)
    l1 = head

    #setup other pointers
    head.other = third_node
    third_node.other = tail
    tail.other_node = second_node
    second_node.other = fourth_node
    fourth_node.other = head
    print("***** original list *****")

    while l1:
        if l1.next == None:
            print(str(l1.val) + "None" + str(l1.other.val) if l1.other is not None else "None")
            break

        print(str(l1.val) + ", " + str(l1.next.val)+ ", " + str(l1.other.val)if l1.other is not None else "None")
        l1 = l1.next
    cloned_list = deep_copy(head)
    l1 = cloned_list
    print("***** cloned list *****")
    while l1:
        if l1.next == None:
            print(str(l1.val) + "None" + str(l1.other.val) if l1.other is not None else "None")
            break
        print(str(l1.val) + ", " + str(l1.next.val) + ", " + str(l1.other.val)if l1.other is not None else "None")
        l1 = l1.next




