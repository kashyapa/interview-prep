import math

# Given an array of positive numbers and a positive number ‘k,’
# find the maximum sum of any contiguous subarray of size ‘k’.


def max_sub_array_of_size_k(k, arr):

    sum = 0
    max_sum = -math.inf

    for i in range(len(arr)):
        sum += arr[i]
        if i >= k-1:
            max_sum = max(max_sum, sum)
            sum -= arr[i+1-k]
    return max_sum


if __name__ == "__main__":
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
