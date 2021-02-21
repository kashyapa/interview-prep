# Given a string, find the minimum number of characters that we can remove to make it a palindrome.


def find_minimum_deletions(st):
    #return len(st) - longest_palindrome_subsequence_recur(st, 0, len(st)-1)
    return len(st) - longest_palindrome_subsequence_dp(st)


def longest_palindrome_subsequence_recur(st, start_index, end_index):
    if start_index > end_index:
        return 0

    if start_index == end_index:
        return 1

    if st[start_index] == st[end_index]:
        return 2 + longest_palindrome_subsequence_recur(st, start_index + 1, end_index - 1)

    return max(
        longest_palindrome_subsequence_recur(st, start_index, end_index - 1),
        longest_palindrome_subsequence_recur(st, start_index + 1, end_index)
    )


def longest_palindrome_subsequence_dp(st):

    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for start_index in range(n-1, -1, -1):
        for end_index in range(start_index+1, n):
            if st[start_index] == st[end_index]:
                dp[start_index][end_index] = 2 + dp[start_index+1][end_index-1]
            else:
                dp[start_index][end_index] = max(dp[start_index+1][end_index], dp[start_index][end_index-1])

    return dp[0][n-1]

def main():
    print(find_minimum_deletions("abdbca"))
    print(find_minimum_deletions("cddpd"))
    print(find_minimum_deletions("pqr"))


if __name__ == "__main__":
    main()
