def lps(s1):
    def rec(l, r):
        if l == r:
            return 1
        if l > r:
            return 0

        if s1[l] == s1[r]:
            return 2 + rec(l+1, r-1)

        c2 = rec(l+1, r)
        c3 = rec(l, r -1)
        return max(c2, c3)

    return rec(0, len(s1)-1)


def lps_dp(s1):
    dp = [[0 for _ in range(len(s1))] for _ in range(len(s1))]
    for i in range(len(s1)):
        dp[i][i] = 1

    for i in range(len(s1)-1, -1, -1):
        for j in range(i+1, len(s1)):
            if s1[i] == s1[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    # print(dp[1])
    return dp[0][len(s1)-1]


def main():
    print(lps("abdbca"))
    print(lps("cddpd"))
    print(lps("pqr"))

    print(lps_dp("abdbca"))
    print(lps_dp("cddpd"))
    print(lps_dp("pqr"))

main()
