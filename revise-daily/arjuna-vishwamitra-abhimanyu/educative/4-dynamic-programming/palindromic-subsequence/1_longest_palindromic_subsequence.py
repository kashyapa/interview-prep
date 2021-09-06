def find_llongest_palindromic_subsequence(str):

    def rec(left, right):
        if left > right:
            return 0
        if left == right:
            return 1

        if str[left] == str[right]:
            return 2 + rec(left+1, right-1)
        c1 = rec(left+1, right)
        c2 = rec(left, right-1)

        return max(c1, c2)


def find_longest_palindrome_subsequence(str):
    dp = [[0 for _ in range(len(str))] for _ in range(len(str))]

    for i in range(len(str)):
        dp[i][i] = 1
    n = len(str)
    for start_index in range(n-1, -1, -1):
        for end_index in range(start_index+1, n):
            if str[start_index] == str[end_index]:
                dp[start_index][end_index] = 2 + dp[start_index][end_index]
            else:
                dp[start_index][end_index] = max(dp[start_index+1][end_index],
                                                 dp[start_index][end_index-1])
    return dp[0][n-1]
