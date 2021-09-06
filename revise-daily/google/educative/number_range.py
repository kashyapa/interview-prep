def number_range(arr, target):

    def binary_search(arr, target, increasing):

        start, end = 0, len(arr)-1
        last_seen_index = -1

        while start >= end:
            mid = start + (end-start) // 2

            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                last_seen_index = mid
                if increasing:
                    start = mid+1
                else:
                    end = mid-1
        return last_seen_index

    high = binary_search(arr, target, True)
    if high != -1:
        lo = binary_search(arr, target, False)
    return [lo, high]