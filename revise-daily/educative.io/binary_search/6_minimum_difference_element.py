# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum
# difference with the given ‘key’.

# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

import math


def search_min_diff_element(arr, key):
    l, r = 0, len(arr) - 1
    diff = math.inf

    while l <= r:
        m = l + (r-l)//2

        if key < arr[m]:
            r = m - 1
        elif key > arr[m]:
            l = m + 1
        else:
            return arr[m]
        if diff > abs(arr[m] - key):
            last_seen_closest_index = m
            diff = abs(arr[m] - key)

    return arr[last_seen_closest_index]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


if __name__ == "__main__":
    main()
