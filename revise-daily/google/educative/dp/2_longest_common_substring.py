def longest_common_substring(s1, s2):

    def rec(i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            return count

        if s1[i1] == s2[i2]:
            count = rec(i1+1, i2+1, count+1)

        count2 = max(rec(i1, i2+1, 0), rec(i1+1, i2, 0))

        return max(count, count2)
    return rec(0, 0, 0)


def longest_common_substring_dp(s1, s2):

    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_length = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                # compute only when characters match, otherwise it is zero..
                # we do not use values obtained by comparing previous character on either string
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])
    return max_length
