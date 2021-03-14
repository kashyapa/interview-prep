from heapq import *
"""
Time complexity #
Since we’ll be going through all the elements of all arrays and will be removing/adding one element to the heap in 
each step, the time complexity of the above algorithm will be O(N*logK),O(N∗logK), where ‘N’ is the total number of 
elements in all the ‘K’ input arrays.

Space complexity #
The space complexity will be O(K)O(K) because, at any time, our min-heap will be storing one number from all the 
‘K’ input arrays.

"""
# Sort from M sorted lists


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    min_heap = []

    for first_node in lists:
        if first_node is not None:
            heappush(min_heap, first_node)
    head, tail = None, None

    while min_heap:
        p = heappop(min_heap)
        if head is None:
            head = tail = p
        else:
            tail.next = p
            tail = tail.next

        if p.next is not None:
            heappush(min_heap, p.next)

    return head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next


if __name__ == "__main__":
    main()
