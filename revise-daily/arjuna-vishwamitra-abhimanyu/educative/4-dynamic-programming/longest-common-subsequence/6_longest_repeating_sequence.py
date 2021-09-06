def longest_repeating_sequence(str):
    
    def rec(i1, i2):
        if i1 == len(str) or i2 == len(str):
            return 0
        count = 0
        if i1 != i2 and str[i1] == str[i2]:
            return 1 + rec(i1+1, i2+1)

        count2 = rec(i1, i2+1)
        count3 = rec(i1+1, i2)
        return max(count2, count3)
    return rec(0, 0)


def longest_repeating_sequence2(str):
    n = len(str)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    max_length = 0
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and str[i] == str[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_length = max(max_length, dp[i][j])
    return max_length
