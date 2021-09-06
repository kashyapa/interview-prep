def find_LIS(arr):
    def rec(prev_idx, cur_idx):
        if cur_idx == len(arr):
            return 0
        count = 0
        if prev_idx == -1 or arr[prev_idx] < arr[cur_idx]:
            count = 1+rec(cur_idx, cur_idx+1)
        count2 = rec(prev_idx, cur_idx+1)
        return max(count, count2)


def find_lis(nums):
    max_length = 0
    dp = [1 for _ in range(len(nums)+1)]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] > dp[j]+1:
                dp[i] = dp[j]+1

        max_length = max(max_length, dp[i])
    return max_length