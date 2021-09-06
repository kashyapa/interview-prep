from imports import *


def count_subset_sum(nums):

    def rec(idx, remaining_sum):
        if remaining_sum == 0:
            return 1
        if idx == len(nums):
            return 0
        count = 0
        if nums[idx] <= remaining_sum:
            count = rec(idx+1, remaining_sum-nums[idx])

        return count + rec(idx+1, remaining_sum)
    return rec(0, sum(nums))


def count_subset_sum_dp(nums):

    dp = [[-1 for _ in range(sum(nums)+1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1

    for i in range(sum(nums)+1):
        dp[0][i] = 1 if nums[0] == i else 0

    for i in range(1, len(nums)):
        for j in range(1, sum(nums)+1):
            dp[i][j] = dp[i-1][j]
            if nums[i] <= j:
                dp[i][j] += dp[i-1][j-nums[i]]
    return dp[-1][-1]
