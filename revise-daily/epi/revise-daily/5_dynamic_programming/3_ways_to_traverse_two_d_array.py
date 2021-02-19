def traverse_2_d_array(m, n):
    def traverse_2d_dp(x, y):
        if x == 0 and y == 0:
            return 1

        if dp[x][y] == 0:
            ways_top = 0 if x == 0 else traverse_2d_dp(x - 1, y)
            ways_right = 0 if y == 0 else traverse_2d_dp(x, y - 1)
            dp[x][y] = ways_right + ways_top
        return dp[x][y]

    dp = [[0] * (n) for _ in range(m)]
    return traverse_2d_dp(m-1, n-1)


if __name__ == '__main__':
    print(traverse_2_d_array(5, 4))
