# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS).
# In an increasing subsequence, all the elements are in increasing order (from lowest to highest).


# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LIS is {2,3,6,10,12}.

def find_LIS(arr):
    return find_LIS_rec(arr, 0, -1)

def find_LIS_rec(arr, current_index, prev_index):
    if current_index == len(arr):
        return 0
    c1 = 0
    if prev_index == -1 or arr[current_index] > arr[prev_index]:
        c1 = 1 + find_LIS_rec(arr, current_index+1, current_index)

    c2 = find_LIS_rec(arr, current_index+1, prev_index)

    return max(c1, c2)

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

def longest_increasing_subsequence(nums):
    dp = [1 for _ in range(len(nums))]
    max_length = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j])
                max_length = max(max_length, dp[i])
    return max_length

def main():
    print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_length([-4, 10, 3, 7, 15]))
    print(find_LIS([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS([-4, 10, 3, 7, 15]))
    print("********")
    print(longest_increasing_subsequence([4, 2, 3, 6, 10, 1, 12]))
    print(longest_increasing_subsequence([-4, 10, 3, 7, 15]))
    print(longest_increasing_subsequence([4, 2, 3, 6, 10, 1, 12]))
    print(longest_increasing_subsequence([-4, 10, 3, 7, 15]))

if __name__ == "__main__":
    main()
