# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.


def equal_subset_sum_partition(nums):
    s = sum(nums)

    def rec(idx, remaining_sum):
        if idx == len(nums):
            return remaining_sum == 0

        if remaining_sum == 0:
            return True

        if nums[idx] < remaining_sum:
            with_num = rec(idx+1, remaining_sum-nums[idx])
            if with_num:
                return True
        return rec(idx+1, remaining_sum)

    return rec(0, s)


def equal_subset_sum_dp(nums):
    s = sum(nums) // 2

    dp = [[False for _ in range(s+1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for i in range(s+1):
        dp[0][i] = True if nums[0] == i else False

    for i in range(len(nums)):
        for j in range(s+1):
            if dp[i-1][j]:
                dp[i][j] = True
            if nums[i] <= j:
                dp[i][j] = dp[i-1][j-nums[i]]

    return dp[len(nums)-1][s]
