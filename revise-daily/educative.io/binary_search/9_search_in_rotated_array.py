# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number,
# find if a given ‘key’ is present in it.
#
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1.
# You can assume that the given array does not have any duplicates.


def search_rotated_array(arr, key):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = l + (r - l)//2
        if arr[m] == key:
            return m

        if arr[m] > arr[l]:
            if arr[m] > key >= arr[l]:
                r = m - 1
            else:
                l = m + 1
        else:
            if arr[m] < key <= arr[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


if __name__ == "__main__":
    main()
