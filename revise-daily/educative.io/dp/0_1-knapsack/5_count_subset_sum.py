# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.


def count_subsets(nums, s):
    # return count_subsets_equal_to_s_rec(nums, s, 0)
    return count_subset_equal_to_sum_dp(nums, s)


def count_subsets_equal_to_s_rec(nums, sum, index):
    if sum == 0:
        return 1

    if len(nums) == 0 or index >= len(nums):
        return 0

    count_with_num, count_without_num = 0, 0

    if sum >= nums[index]:
        count_with_num = count_subsets_equal_to_s_rec(nums, sum - nums[index], index + 1)
    count_without_num = count_subsets_equal_to_s_rec(nums, sum, index + 1)

    return count_with_num + count_without_num


def count_subset_equal_to_sum_dp(nums, sum):
    dp = [[-1 for _ in range(sum + 1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1

    for i in range(1, sum + 1):
        dp[0][i] = 1 if nums[0] == i else 0

    for i in range(1, len(nums)):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j]
            if nums[i] <= j:
                dp[i][j] += dp[i - 1][j - nums[i]]

    return dp[len(nums) - 1][sum]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


if __name__ == "__main__":
    main()
