def shortest_common_super_sequence(s1, s2):
    def rec(s1, s2, i1, i2):
        n1, n2 = len(s1), len(s2)
        if i1 == len(s1):
            return n1 - i1
        if i2 == len(s2):
            return n2 - i2
        if s1[i1] == s2[i2]:
            return 1 + rec(s1, s2, i1+1, i2+1)
        
        c1 = 1 + rec(s1, s2, i1, i2+1)
        c2 = 1 + rec(s1, s2, i1, i2+1)
        return min(c1, c2)


def shortest_common_supersequence_dp(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    n1, n2 = len(s1), len(s2)

    for i in range(len(s1)+1):
        dp[i][0] = i

    for i in range(len(s2)+1):
        dp[0][i] = i

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]
