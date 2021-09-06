def longest_subarray_with_sum(nums, k):
    map = dict()
    count = 0
    running_sum = 0
    map.put(0, 1)
    for i in range(len(nums)):
        running_sum += nums[i]
        count += map.get(running_sum - k, 0) + 1
        map[running_sum] = map.get(running_sum, 0) + 1

    return count