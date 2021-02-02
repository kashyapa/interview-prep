# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
#
# You can assume that the array does not have any duplicates.

# Input: [10, 15, 1, 3, 8]
# Output: 2
# Explanation: The array has been rotated 2 times.


def count_rotations(arr):

    return 0  # the array has not been rotated


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


if __name__ == "__main__":
    main()
