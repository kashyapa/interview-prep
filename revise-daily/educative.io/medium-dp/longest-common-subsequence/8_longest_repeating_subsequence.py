def find_LRS_length(str):
    n = len(str)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LRS_length_recursive(dp, str, 0, 0)


def find_LRS_length_recursive(dp, str, i1, i2):
    n = len(str)
    if i1 == n or i2 == n:
        return 0

    if dp[i1][i2] == -1:
        if i1 != i2 and str[i1] == str[i2]:
            dp[i1][i2] = 1 + find_LRS_length_recursive(dp, str, i1 + 1, i2 + 1)
        else:
            c1 = find_LRS_length_recursive(dp, str, i1, i2 + 1)
            c2 = find_LRS_length_recursive(dp, str, i1 + 1, i2)
            dp[i1][i2] = max(c1, c2)

    return dp[i1][i2]


def main():
    print(find_LRS_length("tomorrow"))
    print(find_LRS_length("aabdbcec"))
    print(find_LRS_length("fmff"))


main()
