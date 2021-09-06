def longest_common_substring(s1, s2):
    def lcs_rec(idx1, idx2, count):
        if idx1 == len(s1) or idx2 == len(s2):
            return count

        if s1[idx1] == s2[idx2]:
            count = lcs_rec(idx1+1, idx2+1, count+1)

        c2 = lcs_rec(idx1, idx2+1, 0)
        c3 = lcs_rec(idx1+1, idx2, 0)
        return max(count, max(c2, c3))

    def lcs_dp():
        max_len = 0
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    max_len = max(max_len, dp[i][j])
        return max_len
    print(lcs_dp())
    print(lcs_rec(0, 0, 0))


if __name__ == "__main__":
    # longest_common_substring("abaddwe", "addwe")
    # longest_common_substring("abaddwe", "aba")
    longest_common_substring("abdca", "cbda")
    longest_common_substring("passport", "ppsspt")
