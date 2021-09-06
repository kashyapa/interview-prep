def lp_subsequence(s):
    def rec(l, r):
        if l > r:
            return 0
        if l == r:
            return 1

        if s[l] == s[r]:
            return 2 + rec(l+1, r-1)
        c1 = rec(l+1, r)
        c2 = rec(l, r-1)
        return max(c1, c2)

    def dp_solution():
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        max_len = 0
        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                max_len = max(max_len, dp[i][j])
        return max_len

    print("lp subsequence recursive: ", rec(0, len(s)-1))
    print("lp subsequence dp:        ", dp_solution())


def lp_substring(s):

    def rec(l, r):
        if l > r:
            return 0
        if l == r:
            return 1

        if s[l] == s[r]:
            remaining_length = r - l - 1
            count = rec(l+1, r-1)
            if r - l == 1 or count == remaining_length:
                return 2 + remaining_length
        c2 = rec(l+1, r)
        c3 = rec(l, r-1)
        return max(c2, c3)

    def dp_solution():
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        max_len = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    max_len = max(max_len, dp[i][j])
        return max_len

    print("lp substring rec: ", rec(0, len(s)-1))
    print("lp substring  dp:  ", dp_solution())


def lc_substring(s1, s2):
    def rec(idx1, idx2, count):
        if idx1 == len(s1) or idx2 == len(s2):
            return count

        if s1[idx1] == s2[idx2]:
            count = rec(idx1+1, idx2+1, count+1)

        c2 = rec(idx1, idx2+1, 0)
        c3 = rec(idx1+1, idx2, 0)
        return max(count, max(c2, c3))

    def dp_solution():
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        max_len = 0
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    max_len = max(max_len, dp[i][j])
        return max_len

    print("lc substring rec :", rec(0, 0, 0))
    print("lc substring dp  :", dp_solution())


def lc_subsequence(s1, s2):
    def rec(i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0
        if s1[i1] == s2[i2]:
            return 1 + rec(i1+1, i2+1)

        c2 = rec(i1, i2+1)
        c3 = rec(i1+1, i2)
        return max(c2, c3)

    def dp_solution():
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        max_len = 0
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                max_len = max(max_len, dp[i][j])
        return max_len

    print("lc subsequence rec:", rec(0, 0))
    print("lc subsequence dp :", dp_solution())


def main():
    lp_subsequence("abdbca")
    lp_subsequence("cddpd")
    lp_subsequence("pqr")

    lp_substring("abdbca")
    lp_substring("cddpd")
    lp_substring("pqr")

    lc_substring("abdca", "cbda")
    lc_substring("passport", "ppsspt")

    lc_subsequence("abdca", "cbda")
    lc_subsequence("passport", "ppsspt")

if __name__ == "__main__":
    main()
