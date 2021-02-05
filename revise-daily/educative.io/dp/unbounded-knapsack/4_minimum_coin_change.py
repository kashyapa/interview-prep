import math


def count_change(denominations, total):
    dp = [[-1 for _ in range(total + 1)] for _ in range(len(denominations))]
    result = count_change_recursive(dp, denominations, total, 0)
    return -1 if result == math.inf else result


def count_change_recursive(dp, denominations, total, currentIndex):
    # base check
    if total == 0:
        return 0
    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return math.inf

    # check if we have not already processed a similar sub-problem
    if dp[currentIndex][total] == -1:
        # recursive call after selecting the coin at the currentIndex
        # if the coin at currentIndex exceeds the total, we shouldn't process this
        count1 = math.inf
        if denominations[currentIndex] <= total:
            res = count_change_recursive(
                dp, denominations, total - denominations[currentIndex], currentIndex)
            if res != math.inf:
                count1 = res + 1

        # recursive call after excluding the coin at the currentIndex
        count2 = count_change_recursive(
            dp, denominations, total, currentIndex + 1)
        dp[currentIndex][total] = min(count1, count2)

    return dp[currentIndex][total]


def count_ribbon_pieces_dp(ribbonLengths, total):
    n = len(ribbonLengths)
    dp = [[-math.inf for _ in range(total + 1)] for _ in range(n)]

    # populate the total=0 columns, as we don't need any ribbon to make zero total
    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for t in range(1, total + 1):
            if i > 0:  # exclude the ribbon
                dp[i][t] = dp[i - 1][t]
            # include the ribbon and check if the remaining length can be cut into available lengths
            if t >= ribbonLengths[i] and dp[i][t - ribbonLengths[i]] != -math.inf:
                dp[i][t] = max(dp[i][t], dp[i][t - ribbonLengths[i]] + 1)

    # total combinations will be at the bottom-right corner, return '-1' if cutting is not possible
    return -1 if dp[n - 1][total] == -math.inf else dp[n - 1][total]


def main():
    print(count_change([1, 2, 3], 5))
    print(count_change([1, 2, 3], 11))
    print(count_change([1, 2, 3], 7))
    print(count_change([3, 5], 7))


if __name__ == "__main__":
    main()
