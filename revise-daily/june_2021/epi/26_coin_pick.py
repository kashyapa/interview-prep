def coin_pick_for_max_gain(coins):

    def rec(a, b):
        if a > b:
            return 0

        picks_a = coins[a] + min(rec(a-2, b), rec(a-1, b-1))

        picks_b = coins[b] + min(rec(a, b-2), rec(a-1, b-1))
        return max(picks_a, picks_b)

    return rec(0, len(coins)-1)
