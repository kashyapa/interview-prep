#
# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number S

def count_subsets_equal_to_sum(nums, S):

    def rec(idx, remaining_sum):

        if remaining_sum == 0:
            return 1

        if idx == len(nums):
            return 0

        count = 0
        if nums[idx] <= remaining_sum:
            count = rec(idx+1, remaining_sum-nums[idx])
        count += rec(idx+1, remaining_sum)
    return rec(0, S)

def count_subsets_equal_to_sum(nums):
    s = sum(nums)
    dp = [0 for _ in range(s+1)]

    dp[0] = 1

    for i in range(s+1):
        dp[s] = 1 if nums[0] == s else 0

    n = len(nums)

    for i in range(1, n):
        for j in range(s+1):
            dp[j] += dp[j-nums[i]]
    return dp[s]
