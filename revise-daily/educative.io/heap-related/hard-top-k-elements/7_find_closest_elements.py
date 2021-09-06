def find_closest_elements(arr, K, X):
    result = []
    index = binary_search(arr, X)

    i = index
    j = index + 1

    for _ in range(K):
        if i >= 0 and j < len(arr):
            diff1 = abs(arr[i] - X)
            diff2 = abs(arr[j] - X)
            if diff1 <= diff2:
                result.append(arr[i])
                i -= 1
            else:
                result.append(arr[j])
                j += 1
        elif i >= 0:
            result.append(arr[i])
            i -= 1
        elif j <= len(arr):
            result.append(arr[j])
            j += 1

    return result


def binary_search(arr, X):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = left + (right-left)/2

        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    print("'K' closest numbers to 'X' are: " + str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " + str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " + str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


if __name__ == "__main__":
    main()
