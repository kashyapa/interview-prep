import math


def count_ribbon_pieces(ribbonLengths, total):
    maxPieces = count_ribbon_pieces_recursive(ribbonLengths, total, 0)
    return -1 if maxPieces == -math.inf else maxPieces


def count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex):
    # base check
    if total == 0:
        return 0

    n = len(ribbonLengths)
    if n == 0 or currentIndex >= n:
        return -math.inf

    # recursive call after selecting the ribbon length at the currentIndex
    # if the ribbon length at the currentIndex exceeds the total, we shouldn't process this
    c1 = -math.inf
    if ribbonLengths[currentIndex] <= total:
        result = count_ribbon_pieces_recursive(
            ribbonLengths, total - ribbonLengths[currentIndex], currentIndex)
        if result != -math.inf:
            c1 = result + 1

    # recursive call after excluding the ribbon length at the currentIndex
    c2 = count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex + 1)
    return max(c1, c2)


def count_ribbon_pieces_dp(ribbonLengths, total):
    n = len(ribbonLengths)
    dp = [[-math.inf for _ in range(total + 1)] for _ in range(n)]

    # populate the total=0 columns, as we don't need any ribbon to make zero total
    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for t in range(1, total + 1):
            if i > 0:  # exclude the ribbon
                dp[i][t] = dp[i - 1][t]
            # include the ribbon and check if the remaining length can be cut into available lengths
            if t >= ribbonLengths[i] and dp[i][t - ribbonLengths[i]] != -math.inf:
                dp[i][t] = max(dp[i][t], dp[i][t - ribbonLengths[i]] + 1)

    # total combinations will be at the bottom-right corner, return '-1' if cutting is not possible
    return -1 if dp[n - 1][total] == -math.inf else dp[n - 1][total]


def main():
    print(count_ribbon_pieces([2, 3, 5], 5))
    print(count_ribbon_pieces([2, 3], 7))
    print(count_ribbon_pieces([3, 5, 7], 13))
    print(count_ribbon_pieces([3, 5], 7))


if __name__ == "__main__":
    main()
