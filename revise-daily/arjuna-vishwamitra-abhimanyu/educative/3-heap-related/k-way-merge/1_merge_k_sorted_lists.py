class ListNode:

    def __init__(self, val):
        self.next = None
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

from imports import *


def merge_k_sorted_lists(lists):

    min_heap = []
    for first in lists:
        if first is not None:
            heappush(min_heap, first)

    head = tail = None

    while min_heap:
        p = heappop(min_heap)

        if head is None:
            head = tail = p
        else:
            tail.next = p
            tail = tail.next

        if p.next:
            heappush(min_heap, p.next)
    return head
