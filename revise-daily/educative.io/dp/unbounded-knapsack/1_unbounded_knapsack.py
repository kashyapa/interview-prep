# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.
#
# Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:
#
# Items: { Apple, Orange, Melon }
# Weights: { 1, 2, 3 }
# Profits: { 15, 20, 50 }
# Knapsack capacity: 5


def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_recursive(profits, weights, capacity, 0)


def solve_knapsack_recursive(profits, weights, capacity, currentIndex):
    n = len(profits)
    # base checks
    if capacity <= 0 or n == 0 or len(weights) != n or currentIndex >= n:
        return 0

    # recursive call after choosing the items at the currentIndex, note that we recursive call on all
    # items as we did not increment currentIndex
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + solve_knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex)

    # recursive call after excluding the element at the currentIndex
    profit2 = solve_knapsack_recursive(
        profits, weights, capacity, currentIndex + 1)

    return max(profit1, profit2)


def solve_knapsack_dp(profits, weights, capacity):
    n = len(profits)
    # base checks
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]

    # populate the capacity=0 columns
    for i in range(n):
        dp[i][0] = 0

    # process all sub-arrays for all capacities
    for i in range(n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i][c - weights[i]]
            if i > 0:
                profit2 = dp[i - 1][c]
            dp[i][c] = profit1 if profit1 > profit2 else profit2

    # maximum profit will be in the bottom-right corner.
    return dp[n - 1][capacity]


def main():
    print(solve_knapsack_dp([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack_dp([15, 50, 60, 90], [1, 3, 4, 5], 6))


if __name__ == "__main__":
    main()
