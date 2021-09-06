def find_kth_smallest_element(arr, k):

    l, r = 0, len(arr)-1

    while l < r:
        pivot