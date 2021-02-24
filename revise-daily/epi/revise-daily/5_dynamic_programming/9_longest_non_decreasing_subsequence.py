def longest_non_decreasing_sequence(arr):
    dp = [1] * (len(arr) + 1)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    print(longest_non_decreasing_sequence([1, 4, 2, 3, 6, 2]))
