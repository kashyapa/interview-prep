def staircase(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    ways_with_1 = staircase(n-1)
    ways_with_2 = staircase(n-2)
    ways_with_3 = staircase(n-3)

    return ways_with_1 + ways_with_2 + ways_with_3


def staircase_dp(n):
    dp = [1, 1, 2]
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    return dp[n]

