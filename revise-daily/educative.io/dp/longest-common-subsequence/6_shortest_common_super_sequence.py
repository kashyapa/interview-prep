# Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has
# ‘s1’ and ‘s2’ as subsequences.

def find_SCS_length(s1, s2):
    return find_SCS_rec(s1,s2, 0, 0)


def find_SCS_rec(s1, s2, i1, i2):
    # if we have reached the end of a string, return the remaining length of the
    # other string, as in this case we have to take all of the remaining other string
    n1, n2 = len(s1), len(s2)
    if i1 == n1:
        return n2 - i2
    if i2 == n2:
        return n1 - i1

    c1 = 0
    if s1[i1] == s2[i2]:
        return 1 + find_SCS_rec(s1, s2, i1+1, i2+1)
    c2 = 1 + find_SCS_rec(s1, s2, i1, i2+1)
    c3 = 1 + find_SCS_rec(s1, s2, i1+1, i2)

    return min(c2,c3)

def find_SCS_dp(s1, s2):
    n1, n2 = len(s1), len(s2)

    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1 + 1):
        dp[i][0] = i
    for j in range(n2 + 1):
        dp[0][j] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]

def main():
    print(find_SCS_length("abcf", "bdcf"))
    print(find_SCS_length("dynamic", "programming"))
    print(find_SCS_dp("abcf", "bdcf"))
    print(find_SCS_dp("dynamic", "programming"))


if __name__ == "__main__":
    main()
