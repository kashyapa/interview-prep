import math


def search_element_in_infinite_array(array, key):
    start, end = 0, 1
    while array[end] < key and array[end] != math.inf:
        range = end-start
        start = end
        end += 2 * range

    while start < end:
        mid = (start + end) // 2
        if array[mid] == math.inf:
            return mid

        if array[mid] > key:
            end = mid - 1
        else:
            start = mid+1
    return start
