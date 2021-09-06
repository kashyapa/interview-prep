def max_consecutive_ones_K_replacements(nums, K):
    ones = 0
    left = 0
    max_ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            ones += 1
        while i - left + 1 - ones >= K:
            if nums[left] == 1:
                ones -= 1
            left += 1
        max_ones = max(max_ones, i-left+1)
    return max_ones
