def minimum_subset_sum_difference(nums):

    def rec(idx, sum1, sum2):
        if idx == len(nums):
            return abs(sum1-sum2)

        diff1 = rec(idx+1, sum1+nums[idx], sum2)
        diff2 = rec(idx+1, sum1, sum2+nums[idx])

        return min(diff1, diff2)
    return rec(0, 0, 0)


def minimum_subset_sum_difference(nums):
    dp = [[False for _ in range(sum(nums)+1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for i in range(sum(nums)+1):
        dp[0][i] = True if i == nums[0] else False
        
    for i in range(1, len(nums)):
        for j in range(1, sum(nums)+1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
            
    sum1 = 0
    for i in range(sum(nums)//2, -1, -1):
        if dp[len(nums)-1][i]:
            sum1 = i
            break
    sum2 = sum(nums) - sum1
    return abs(sum2-sum1)

        