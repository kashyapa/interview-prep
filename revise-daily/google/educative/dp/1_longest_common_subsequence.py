def longest_common_subsequence(s1, s2):

    def rec(i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0

        if s1[i1] == s2[i2]:
            return 1 + rec(i1+1, i2+1)
        return max(rec(i1+1, i2), rec(i1, i2+1))
    return rec(0,0)

def longest_common_subsequence_dp(s1, s2):

    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_length = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j]= 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_length = max(dp[i][j], max_length)
    return max_length