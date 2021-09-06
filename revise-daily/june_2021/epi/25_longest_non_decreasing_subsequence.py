def longest_non_decreasing_subsequence(nums):
    dp = [1] * len(nums)
    max_length = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
                max_length = max(max_length, dp[i])
    return max_length

