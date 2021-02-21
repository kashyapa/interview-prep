# Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number
# of substrings and not subsequences.

def count_PS(st):

    return count_PS_dp(st)


def count_PS_dp(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]

    count = 0
    for i in range(n):
        dp[i][i] = True
        count += 1

    for start_index in range(n-1, -1, -1):
        for end_index in range(start_index+1, n):

            if st[start_index] == st[end_index]:
                if end_index - start_index == 1 or dp[start_index+1][end_index-1] is True:
                    dp[start_index][end_index] = True
                    count += 1

    return count


def main():
    print(count_PS("abdbca"))
    print(count_PS("cddpd"))
    print(count_PS("pqr"))
    print(count_PS("qqq"))


if __name__ == "__main__":
    main()
