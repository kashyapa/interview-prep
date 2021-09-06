def maximum_sum_increasing_subsequence(nums):

    def rec(prev_idx, cur_idx):

        if cur_idx == len(nums):
            return 0
        sum1 = 0
        if prev_idx == -1 or nums[prev_idx] < nums[cur_idx]:
            sum1 = nums[cur_idx] + rec(cur_idx, cur_idx+1)

        sum2 = rec(prev_idx, cur_idx+1)
        return max(sum1, sum2)
    return rec(-1, 0)


def maximum_increasing_sum_subsequence(nums):

    dp = [0 for _ in range(len(nums)+1)]
    max_sum = 0
    for i in range(len(nums)+1):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
        max_sum = max(max_sum, dp[i])
    return max_sum
