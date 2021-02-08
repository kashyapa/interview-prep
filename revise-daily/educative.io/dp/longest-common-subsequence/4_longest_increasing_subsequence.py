# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS).
# In an increasing subsequence, all the elements are in increasing order (from lowest to highest).


# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LIS is {2,3,6,10,12}.

def find_LIS_length(arr):
    n1 = len(arr)
    dp = [1 for _ in range(n1)]

    max_length = 0

    for i in range(1, n1):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j]+1:
                dp[i] = dp[j] + 1
                max_length = max(max_length, dp[i])
    return max_length


def main():
    print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_length([-4, 10, 3, 7, 15]))


if __name__ == "__main__":
    main()
