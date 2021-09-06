class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def list_pivoting(L, x):
    
    head, tail = None, None
    temp = None
    
    while L:
        if L.val < x:
            temp = L.next
            L.next = head
            head = L
        else:
            temp = L.next
            tail.next = L
            tail = L
        L = temp
    tail.next = None
    
            