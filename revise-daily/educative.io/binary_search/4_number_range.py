# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
# The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
#
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].


def find_range(arr, key):
    result = [- 1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)

    return result


def binary_search(arr, key, find_max_index):
    l, r = 0, len(arr) - 1
    key_index = -1

    while l <= r:
        m = l + (r - l) // 2

        if key < arr[m]:
            r = m - 1
        elif arr[m] < key:
            l = m + 1
        else:  # key == arr[m]
            # continue the loop by recording the last seen index which holds "key", until
            key_index = m
            if find_max_index:
                l = m + 1
            else:
                r = m - 1

    return key_index


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


if __name__ == "__main__":
    main()
