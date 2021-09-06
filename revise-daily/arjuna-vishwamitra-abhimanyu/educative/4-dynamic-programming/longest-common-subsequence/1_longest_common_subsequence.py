def longest_common_subsequence(str1, str2):

    def rec(str1, str2, idx1, idx2):

        if idx1 == len(str1) or idx2 == len(str2):
            return 0

        if str1[idx1] == str2[idx2]:
            return 1 + rec(str1, str2, idx1+1, idx2+1)

        return max(rec(str1, str2, idx1+1, idx2),
                   rec(str1, str2, idx1, idx2+1))

from imports import *

def longest_common_subsequence(str1, str2):
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

    longest_length = -inf
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        longest_length = max(longest_length, dp[i][j])

    return longest_length
