def can_partition(nums):
    total_sum = sum(nums)

    def rec(idx, remaining_sum):
        if remaining_sum == 0:
            return True

        if idx >= len(nums):
            return False

        if nums[idx] <= remaining_sum:
            return rec(idx+1, remaining_sum-nums[idx])
        return rec(idx+1, remaining_sum)
    return rec(0, total_sum//2)


def subset_sum_dp(nums):
    total_sum = sum(nums)

    dp = [[False for _ in range(total_sum//2 + 1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for i in range(1, total_sum//2+1):
        dp[0][i] = True if nums[0] == i else False

    for i in range(1, len(nums)):
        for j in range(1, total_sum//2+1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif nums[i] <= j:
                dp[i][j] = dp[i-1][j-nums[i]]
    return dp[-1][-1]
