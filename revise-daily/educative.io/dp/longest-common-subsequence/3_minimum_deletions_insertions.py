# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters.
# Write a function to calculate the count of the minimum number of deletion and insertion operations.

# Input: s1 = "abc"
#        s2 = "fbc"
# Output: 1 deletion and 1 insertion.
# Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.


def find_MDI(s1, s2):
    c1 = len(s1) - lcs_rec(s1, s2, 0, 0)
    c2 = len(s2) - lcs_rec(s1, s2, 0, 0)

    return c1, c2


def lcs_rec(s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if s1[i1] == s2[i2]:
        return 1 + lcs_rec(s1, s2, i1+1, i2+1)

    c1 = lcs_rec(s1, s2, i1+1, i2)
    c2 = lcs_rec(s1, s2, i1, i2+1)

    return max(c1, c2)


def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    max_length = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            max_length = max(max_length, dp[i][j])
    return max_length


def main():
    print(find_MDI("abc", "fbc"))
    print(find_MDI("abdca", "cbda"))
    print(find_MDI("passport", "ppsspt"))


if __name__ == "__main__":
    main()
