import math


def smallest_subarray_with_given_sum(target, arr):
    l = 0
    sum = 0
    min_length = len(arr)

    for r in range(len(arr)):
        sum += arr[r]

        while sum >= target:
            min_length = min(min_length, r-l+1)
            sum -= arr[l]
            l += 1

    return min_length


if __name__ == '__main__':

    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

