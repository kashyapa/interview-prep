
def knapsack(capacity, profits, weights):

    def rec(idx, remaining_capacity):
        if remaining_capacity <= 0 or idx >= len(profits):
            return 0

        c = 0
        if weights[idx] <= remaining_capacity:
            c = profits[idx] + rec(idx+1, remaining_capacity-weights[idx])

        c2 = rec(idx+1, remaining_capacity)
        return max(c, c2)


def knapsack_dp(capacity, profits, weights):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    for i in range(capacity+1):
        if weights[0] <= capacity:
            dp[i][0] = profits[0]
    n = len(profits)

    for i in range(1, len(weights)):
        for j in range(capacity+1):
            if weights[i] <= j:
                profit1 = profits[i] + dp[i-1][j-profits[i]]
            profit2 = dp[i-1][j]
            dp[i][j] = max(profit1, profit2)
    return dp[n-1][capacity]