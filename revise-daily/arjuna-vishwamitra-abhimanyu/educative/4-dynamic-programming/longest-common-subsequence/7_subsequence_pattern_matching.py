def find_subsequence_pattern_match(str, pattern):
    def rec(i1, i2):
        if i2 == len(pattern):
            return 1
        if i1 == len(str):
            return 0

        c1 = 0
        if str[i1] == pattern[i2]:
            c1 = rec(i1+1, i2+1)
        c2 = rec(i1+1, i2)
        return c1 + c2


def subsequence_pattern_match(str, pattern):

    dp = [[0 for _ in range(len(pattern))] for _ in range(len(str)+1)]
    max_length = 0
    
    for i in range(len(str)):
        dp[i][0] = 1

    for i in range(1, len(str)+1):
        for j in range(len(pattern)):
            if str[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1]
            dp[i][j] += dp[i-1][j]
            max_length = max(max_length, dp[i][j])
    return max_length
