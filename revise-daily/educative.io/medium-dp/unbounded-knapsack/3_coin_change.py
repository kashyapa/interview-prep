# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number
# of distinct ways to make up that amount.


def count_change(coins, sum):
    return coin_change_rec(coins, sum, 0)


def coin_change_rec(coins, sum, index):
    if sum == 0:
        return 1
    n = len(coins)

    if index >= n:
        return 0
    num_of_ways_by_using_current_coin = 0

    if sum >= coins[index]:
        num_of_ways_by_using_current_coin = coin_change_rec(coins, sum - coins[index], index)
    num_of_ways_without_using_current_coin = coin_change_rec(coins, sum, index + 1)

    return num_of_ways_by_using_current_coin + num_of_ways_without_using_current_coin


def coin_change_dp(coins, sum):
    dp = [[-1 for _ in range(sum + 1)] for _ in range(len(coins))]
    n = len(coins)

    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for s in range(sum + 1):
            if i > 0:
                dp[i][s] = dp[i - 1][s]
            if s >= coins[i]:
                dp[i][s] += dp[i][s - coins[i]]

    return dp[n - 1][sum]


def main():
    print(count_change([1, 2, 3], 5))


if __name__ == "__main__":
    main()
