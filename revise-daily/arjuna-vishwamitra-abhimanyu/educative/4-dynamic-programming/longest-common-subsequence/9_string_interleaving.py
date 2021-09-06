def string_interleaving(s1, s2, pattern):

    def rec(s1, i1, s2, i2, pattern, p):

        if i1 == len(s1) and i2 == len(s2) and p == len(pattern):
            return True

        if p == len(pattern):
            return False

        b1, b2 = False, False

        if i1 < len(s1) and s1[i1] == pattern[p]:
            b1 = rec(s1, i1+1, s2, i2, pattern, p+1)

        if i2 < len(s2) and s2[i2] == pattern[p]:
            b2 = rec(s1, i1, s2, i2+1, pattern, p+1)

        return b1 or b2


def string_interleaving(m, n , p):

    dp = [[False for _ in range(len(n)+1)] for _ in range(len(m)+1)]

    for m_index in range(len(m)+1):
        for n_index in range(len(n)+1):
            if m_index == 0 and n_index ==0:
                dp[m_index][n_index] = True
            elif m_index == 0 and n[n_index-1] == p[m_index+n_index-1]:
                dp[m_index][n_index] = dp[m_index][n_index-1]
            elif n_index == 0 and m[m_index-1] == p[m_index+n_index-1]:
                dp[m_index][n_index] = dp[m_index-1][n_index]
            else:
                if m_index > 0 and m[m_index-1] == p[m_index+n_index-1]:
                    dp[m_index][n_index] = dp[m_index-1][n_index]
                elif n_index > 0 and n[n_index-1] == p[m_index+n_index-1]:
                    dp[m_index][n_index] = dp[m_index][n_index-1]

    return dp[len(m)][len(n)]
