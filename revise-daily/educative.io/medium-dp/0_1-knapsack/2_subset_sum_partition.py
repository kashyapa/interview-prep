# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements
# in both the subsets is equal.

def can_partition(num):
    s = sum(num)

    return can_partition_recursive(num, s / 2, 0)


def can_partition_recursive(num, s, index):
    if index >= len(num):
        return False

    if s == 0:
        return True

    if num[index] <= s:
        if can_partition_recursive(num, s - num[index], index + 1):
            return True
    return can_partition_recursive(num, s, index + 1)


def can_partition_memo(dp, num, s, index):
    if index >= len(num):
        return False

    if s == 0:
        return True

    if dp[index][s] != -1:
        return dp[index][s]

    for i in range(len(num)):
        if num[i] <= s:
            if can_partition_recursive(num, s - num[i], i + 1):
                dp[index][s] = True

    dp[index][s] = can_partition_recursive(num, s, i + 1)

    return dp[index][s]


def can_partition_dp(num):
    s = sum(num)
    dp = [[False for _ in range(s // 2 + 1)] for _ in range(len(num))]

    # populate the sum=0 column, as we can always have '0' sum without including
    # any element
    for i in range(0, len(num)):
        dp[i][0] = True

    for j in range(s // 2 + 1):
        dp[0][j] = num[0] == j

    for i in range(len(num)):
        for j in range(1, s // 2 + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]

            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]
    return dp[len(num) - 1][s // 2]


def main():
    # print("Can partition: " + str(can_partition_dp([1, 2, 3, 4])))
    # print("Can partition: " + str(can_partition_dp([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_dp([2, 3, 4, 6])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


if __name__ == "__main__":
    main()
