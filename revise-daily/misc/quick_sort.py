def quick_sort(array, l, r):
    if l < r:
        pivot_idx = partition(array, l, r)
        quick_sort(array, l, pivot_idx)
        quick_sort(array, pivot_idx + 1, r)


def partition(array, l, r):
    pivot_idx = l + (r - l) // 2
    pivot = array[pivot_idx]
    array[r], array[pivot_idx] = array[pivot_idx], array[r]
    smaller = l
    for i in range(l, r):
        if array[i] < pivot:
            array[smaller], array[i] = array[i], array[smaller]
            smaller += 1
    array[smaller], array[r] = array[r], array[smaller]
    return smaller


def quickSort(array):
    # Write your code here.
    quick_sort(array, 0, len(array) - 1)
    return array
