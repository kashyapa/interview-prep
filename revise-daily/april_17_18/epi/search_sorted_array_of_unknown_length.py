def search_sorted_array_unknown_length(arr, target):
    start, end = 0, 1

    while arr[end] != -1 and arr[end] < target:
        t = end
        end = end + (end-start) * 2
        start = t

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] == -1 or arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


if __name__ == "__main__":
    print(search_sorted_array_unknown_length([2, 3, 5, 5, 6, 8, 9, -1, -1  -1], 4))