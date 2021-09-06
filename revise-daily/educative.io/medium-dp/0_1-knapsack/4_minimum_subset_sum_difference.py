# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset
# sums.

# Input: {1, 2, 3, 9}
# Output: 3
# Explanation: We can partition the given set into two subsets where minimum absolute difference
# between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.


def can_partition(num):
#    return can_partition_rec(num, 0, 0, 0)
    return can_partition_dp(num)


def can_partition_rec(num, index, sum1, sum2):
    if index == len(num):
        return abs(sum1 - sum2)

    diff1 = can_partition_rec(num, index + 1, num[index] + sum1, sum2)
    diff2 = can_partition_rec(num, index + 1, sum1, sum2 + num[index])

    return min(diff1, diff2)


def can_partition_dp(num):
    s = sum(num)
    n = len(num)
    dp = [[False for x in range(int(s / 2) + 1)] for y in range(n)]

    # populate the s=0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to that number
    for j in range(1, int(s / 2) + 1):
        dp[0][j] = num[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, int(s / 2) + 1):
            # if we can get the sum 's' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - num[i]]

    sum1 = 0
    # find the largest index in the last row which is true
    for i in range(int(s / 2), -1, -1):
        if dp[n - 1][i]:
            sum1 = i
            break

    sum2 = s - sum1
    return abs(sum2 - sum1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


if __name__ == "__main__":
    main()


# def main():
#     print("Can partition: " + str(can_partition([1, 2, 3, 9])))
#     print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
#     print("Can partition: " + str(can_partition([1, 3, 100, 4])))
#
#
# main()
