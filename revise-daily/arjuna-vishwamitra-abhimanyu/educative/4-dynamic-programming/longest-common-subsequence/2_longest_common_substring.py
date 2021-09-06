def longest_common_substring(str1, str2):

    def rec(str1, str2, idx1, idx2, count):
        if idx1 == len(str1) or idx2 == len(str2):
            return count

        if str1[idx1] == str2[idx2]:
            count = rec(str1, str2, idx1+1, idx2+1, count+1)

        c1 = rec(str1, str2, idx1+1, idx2, 0)
        c2 = rec(str1, str2, idx1, idx2+1, 0)
        return max(count, max(c1, c2))


def longest_common_substring2(str1, str2):
    max_length = 0

    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])
    return max_length
