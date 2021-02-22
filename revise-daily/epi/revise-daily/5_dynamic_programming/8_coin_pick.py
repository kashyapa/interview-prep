def maximum_coin_game(coins):

    def coin_game_rec(a, b):
        if a > b:
            return 0

        revenue_with_coin_at_a = coins[a] + min(coin_game_rec(a+2, b), coin_game_rec(a+1, b-1))

        revenue_with_coin_at_b = coins[b] + min(coin_game_rec(a, b-2), coin_game_rec(a+1, b-1))

        return max(revenue_with_coin_at_a, revenue_with_coin_at_b)

    return coin_game_rec(0, len(coins)-1)


if __name__ == '__main__':
    print(maximum_coin_game([1, 43, 23, 53, 24, 34]))