# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

def minimum_subset_sum_difference(nums):

    def rec(i, sum1, sum2):

        if i == len(nums):
            return abs(sum1 - sum2)

        diff1 = rec(i+1, sum1+nums[i], sum2)
        diff2 = rec(i+1, sum1, sum2+nums[i])

        return min(diff1, diff2)

    return rec(0, 0, 0)


def minimum_subset_sum_dp(nums):
    s = sum(nums) // 2

    dp = [[False for _ in range(s+1)] for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(s+1):
            if dp[i-1][j]:
                dp[i][j] = True
            if j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]

    n = len(nums)
    sum1 = 0
    for i in range(s, -1, -1):
        if dp[n-1][i]:
            sum1 = i
            break

    sum2 = s - sum1
    return abs(sum1-sum2)
