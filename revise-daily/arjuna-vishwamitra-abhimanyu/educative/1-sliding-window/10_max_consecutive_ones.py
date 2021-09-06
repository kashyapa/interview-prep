def max_consecutive_ones(nums):

    # find longest consecutive ones after replacing max 1 zero
    last_seen_zero = -1
    left = 0
    max_ones = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            if last_seen_zero >= left:
                left = last_seen_zero + 1
            last_seen_zero = i
        max_ones = max(max_ones, i - left + 1)
    return max_ones