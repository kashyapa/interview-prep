def find_LCS_length(s1, s2):
    return find_lcs_rec(s1, s2, 0, 0, 0)


def find_lcs_rec(s1, s2, i1, i2, count):

    if i1 == len(s1) or i2 == len(s2):
        return count
    if s1[i1] == s2[i2]:
        count = find_lcs_rec(s1, s2, i1+1, i2+1, count+1)

    c2 = find_lcs_rec(s1, s2, i1, i2+1, 0)
    c3 = find_lcs_rec(s1, s2, i1+1, i2, 0)

    return max(count, max(c2, c3))


def find_lcs_dp(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    max_length = 0

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])

    return max_length


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))


if __name__ == "__main__":
    main()
