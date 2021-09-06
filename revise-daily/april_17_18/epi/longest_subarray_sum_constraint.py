def longest_subarray_less_than_equal_k(arr, target_sum):
    map = {0: -1}
    sum = 0
    longest_length = 0

    for i in range(len(arr)):
        sum += arr[i]
        if sum not in map:
            map[sum] = i
        if sum-target_sum in map:
            longest_length = max(longest_length, i - map[sum-target_sum])

    return longest_length
