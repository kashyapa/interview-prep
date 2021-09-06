def maximum_coin_gain(coins):

    def rec(a, b):

        if a > b:
            return 0

        pick_a = coins[a] + min(rec(a+1, b-1), rec(a+2, b))
        pick_b  = coins[b] + min(rec(a+1, b-1), rec(a, b-2))

        return max(pick_a, pick_b)

    return rec(0, len(coins)-1)
