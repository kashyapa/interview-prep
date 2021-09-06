def lps(s):

    def rec(l, r):
        if l == r:
            return 1
        if l > r:
            return 0

        if s[l] == s[r]:
            remaining_length = r - l - 1
            if rec(l+1, r-1) == remaining_length:
                return 2+remaining_length
        c1 = rec(l+1, r)
        c2 = rec(l, r-1)
        return max(c1, c2)

    return rec(0, len(s)-1)


def lps_dp(s):

    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    max_len = 1
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
                max_len = max(max_len, dp[i][j])
    return max_len


def main():
    # print(lps("abdbca"))
    # print(lps("cddpd"))
    # print(lps("pqr"))
    #
    # print(lps_dp("abdbca"))
    # print(lps_dp("cddpd"))
    # print(lps_dp("pqr"))

    print(lps_dp("dfdihhi"))

main()
