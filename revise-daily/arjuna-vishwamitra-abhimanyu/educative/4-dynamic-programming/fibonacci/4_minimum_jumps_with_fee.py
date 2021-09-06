def minimum_jumps_with_fee(fee):
    dp = [0 for _ in range(len(fee))]
    return find_min_fee_recursive(dp, fee, 0)


def find_min_fee_recursive(dp, fee, cur_index):
    n = len(fee)
    if cur_index > n - 1:
        return 0
    ways_with_step = [-1, -1, -1]
    if dp[cur_index] == 0:
        ways_with_step[0] = find_min_fee_recursive(dp, fee, cur_index+1)
        ways_with_step[1] = find_min_fee_recursive(dp, fee, cur_index+2)
        ways_with_step[2] = find_min_fee_recursive(dp, fee, cur_index+3)

        dp[cur_index] = fee[cur_index] + min(ways_with_step)

    return dp[cur_index]
