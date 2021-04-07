def maximalSquare(matrix) -> int:
    dp = [[0  for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
    max_len = 0
    for i in range(1, len(matrix) + 1):
        for j in range(1, len(matrix[0]) + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                max_len = max(max_len, dp[i][j])
    return max_len * max_len


if __name__ == "__main__":
    print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))