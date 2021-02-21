# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’.
# The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once,
# as we don’t have multiple quantities of any item.


def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    # return solve_knapsack_rec(profits, weights, capacity, 0)
    return solve_knapsack_memo(dp, profits, weights, capacity, 0)


def solve_knapsack_rec(profits, weights, capacity, index):
    if index >= len(weights):
        return 0
    profit_with_item_at_index = 0
    if weights[index] <= capacity:
        profit_with_item_at_index = profits[index] + solve_knapsack_rec(profits, weights, capacity - weights[index],
                                                                        index + 1)

    profit_without_item_at_index = solve_knapsack_rec(profits, weights, capacity, index + 1)
    return max(profit_with_item_at_index, profit_without_item_at_index)


def solve_knapsack_memo(memo, profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0

    if memo[index][capacity] != -1:
        return memo[index][capacity]

    profit_with_item = 0
    if weights[index] <= capacity:
        profit_with_item = profits[index] + solve_knapsack_memo(memo, profits, weights, capacity - weights[index],
                                                                index + 1)

    profit_without_item = solve_knapsack_memo(memo, profits, weights, capacity, index + 1)

    memo[index][capacity] = max(profit_with_item, profit_without_item)

    return memo[index][capacity]


def solve_knapsack_dp(dp, profits, weights, capacity):
    if capacity == 0 or len(weights) != len(profits):
        return 0

    # if capacity is 0, profit is 0, since we can't add any weights
    for i in range(len(weights)):
        dp[i][0] = 0

    for capacity_i in range(capacity + 1):
        dp[0][capacity_i] = profits[capacity_i] if weights[0] < capacity else 0

    profit1, profit2 = 0, 0

    for i in range(len(weights)):
        for j in range(1, capacity + 1):
            if weights[i] <= j:
                profit1 = profits[i] + dp[i - 1][j - weights[i]]
            profit2 = dp[i - 1][j]

            dp[i][j] = max(profit1, profit2)

    return dp[len(profits) - 1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


if __name__ == "__main__":
    main()
