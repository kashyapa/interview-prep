def binary_search(arr, key):
    # TODO: Write your code here
    left = 0
    right = len(arr)-1
    is_ascending = False
    if arr[0] > arr[-1]:
        is_ascending = True

    while left <= right:
        mid = left + (right - left)/2

        if key == arr[mid]:
            return True

        if is_ascending:
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if key > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


if __name__ == "__main__":
    main()
