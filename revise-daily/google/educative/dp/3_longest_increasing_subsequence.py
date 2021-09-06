def longest_increasing_subsequence(nums):
    dp = [1 for _ in range(len(nums))]
    max_length = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j])
                max_length = max(max_length, dp[i])
    return max_length


def longest_increasing_subsequence_dp(nums):

    def rec(prev, cur):
        if cur >= len(nums):
            return 0
        c1 = 0
        if prev == -1 or nums[cur] > nums[prev]:
            c1 = 1 + rec(cur, cur+1)
        c2 = rec(prev, cur+1)
        return max(c1, c2)

    return rec(-1, 0)
