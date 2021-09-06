def longest_palindromic_subsequence(s):

    def rec(i, j):
        if i < j:
            return -1
        if s[i] == s[j]:
            return 2 + rec(i+1, j-1)
        return max(rec(i, j-1), rec(i+1, j-1))
    return rec(0, len(s)-1)


def longest_palindromic_subsequence_dp(s):

    dp = [[0 for _ in range((len(s)+1))] for _ in range(len(s)+1)]
    n = len(s)
    max_length = 1
    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if j - i > 1 and s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            max_length = max(max_length, dp[i][j])
    return max_length