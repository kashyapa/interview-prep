def knapsack(profits, weights, capacity):
    def rec(idx, remaining_capacity):
        if idx >= len(weights) or remaining_capacity == 0:
            return 0

        profit_with_item = 0
        if weights[idx] <= remaining_capacity:
            profit_with_item = profits[idx] +\
                               rec(idx+1, remaining_capacity-weights[idx])
        profit_without_item = rec(idx+1, remaining_capacity)

        return max(profit_with_item, profit_without_item)
    return rec(0, capacity)


def knapsack_memo(profits, weights, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    def rec(idx, remaining_capacity):
        if idx >= len(profits) or remaining_capacity == 0:
            return 0

        if dp[idx][remaining_capacity]!=0:
            return dp[idx][remaining_capacity]
        profit_with_item = 0
        if weights[idx] <= remaining_capacity:
            profit_with_item = profits[idx] + \
                               rec(idx + 1, remaining_capacity - weights[idx])
        profit_without_item = rec(idx + 1, remaining_capacity)
        dp[idx][remaining_capacity] = max(profit_with_item, profit_without_item)

    return dp[-1][-1]


def knapsack_dp(profits, weights, capacity):

    dp = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    for i in range(len(weights)):
        dp[i][0] = 0

    for c in range(capacity+1):
        if weights[0] <= capacity:
            dp[0][c] = profits[c]

    profit1, profit2 = 0, 0
    for i in range(len(weights)):
        for j in range(1, capacity+1):
            if weights[i] <= j:
                dp[i][j] = profits[i] + dp[i-1][j-weights[i]]
            dp[i][j] = max(dp[i][j], dp[i-1][j])
    return dp[-1][-1]
