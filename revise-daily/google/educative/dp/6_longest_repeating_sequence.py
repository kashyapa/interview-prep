# Given a sequence, find the length of its longest repeating subsequence (LRS).
# A repeating subsequence will be the one that appears at least twice in the
# original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

def longest_repeating_subsequence(s1):

    def rec(i1, i2):

        if i1 == len(s1) or i2 == len(s1):
            return 0
        if i1 != i2 and s1[i1] == s1[i2]:
            return 1 + rec(i1+1, i2+1)
        return max(rec(i1, i2+1), rec(i1+1, i2))
    return rec(0, 0)


def longest_repeating_subsequence_dp(s1):

    dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s1)+1)]
    max_length = 0
    
    for i in range(1, len(s1)+1):
        for j in range(1, len(s1)+1):
            if i != j and s1[i-1] == s1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:   
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_length = max(dp[i][j], max_length)
    return max_length
