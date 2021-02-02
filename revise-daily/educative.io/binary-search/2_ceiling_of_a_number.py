# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
# The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
#
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.


def search_ceiling_of_a_number(arr, key):
    # TODO: Write your code here
    l, r = 0, len(arr) - 1

    while l <= r:
        m = l + (r-l)//2
        if arr[m] == key:
            return m
        if key < arr[m]:
            r = m - 1
        else:
            l = m + 1

    return l


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


if __name__ == "__main__":
    main()
