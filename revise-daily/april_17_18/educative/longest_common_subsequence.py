def longest_common_subsequence(s1, s2):

    def lcs_res(idx1, idx2):

        if idx1 == len(s1) or idx2 == len(s2):
            return 0

        if s1[idx1] == s2[idx2]:
            return 1 + lcs_res(idx1+1, idx2+1)

        c1 = lcs_res(idx1+1, idx2)
        c2 = lcs_res(idx1, idx2+1)
        return max(c1, c2)

    def lcs_dp():
        max_len = 0
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                max_len = max(max_len, dp[i][j])
        return max_len

    print(lcs_res(0, 0))
    print(lcs_dp())


if __name__ == "__main__":
    longest_common_subsequence("ABADAOEIFJ", "CIBSDICBESDC")
