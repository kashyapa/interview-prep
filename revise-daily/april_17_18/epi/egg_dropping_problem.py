def egg_drop(cases, drops):
    if cases == 0 or drops == 0:
        return 0
    elif cases == 1:
        return drops
    if dp[cases][drops] == -1:
        with_case_break = egg_drop(cases-1, drops-1)
        without_case_break = egg_drop(cases, drops-1) + 1
        dp[cases][drops] = without_case_break + with_case_break
    return dp[cases][drops]


if __name__ == "__main__":
    cases = 5
    drops = 10
    dp = [[-1 for _ in range(drops + 1)] for _ in range(cases+1)]
    print(egg_drop(cases, drops))
    print(dp)
