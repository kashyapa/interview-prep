def count_inversions(nums):

    def count_inversions(nums, start, end):

        def merge_and_count_inversions(nums, start, mid, end):

            left = mid
            inversion_count = 0
            res = []
            while start < mid and left < end:
                if nums[start] > nums[left]:
                    res.append(nums[left])
                    left += 1
                    inversion_count += mid - start
                else:
                    res.append(nums[start])
                    start += 1
            nums[start:end] = res + nums[start:mid] + nums[left:end]

            return inversion_count

        mid = start + (end - start) // 2

        lcount = count_inversions(nums, start, mid)
        rcount = count_inversions(nums, mid+1, end)
        return lcount + rcount + merge_and_count_inversions(nums, start, mid ,end)

    return count_inversions(nums, 0, len(nums)-1)


def maximal_square(matrix):
    dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]

    # for i in range(len(matrix[0])):
    #     dp[0][i] = 1 if matrix[0][i] == 1 else dp[0][i]
    #
    # for i in range(len(matrix[0])):
    #     dp[i][0] = 1 if matrix[i][0] == 1 else dp[i][0]
    
    max_len = 0

    for i in range(1, len(matrix)+1):
        for j in range(1, len(matrix[0])+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                max_len = max(max_len, dp[i][j])
    return dp[len(matrix)][len(matrix[0])]


def longestPalindromicSubstring(string):
    # Write your code here.
    def rec(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        
        if string[i] == string[j]:
            remaining_length = j - i - 1
            if j - i == 1 or rec(i+1, j-1) == remaining_length:
                return remaining_length + 2
        c1 = rec(i, j-1)
        c2 = rec(i+1, j)
        return max(c1, c2)
    return rec(0, len(string)-1)

def merge_sort(nums):

    def divide_and_conquer(nums):
        def sorted_merge(l1, l2):

            i, j = 0, 0
            res = []
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1

            return res

        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left_arr = divide_and_conquer(nums[:mid])
        right_arr = divide_and_conquer(nums[mid:])

        return sorted_merge(left_arr, right_arr)
    return divide_and_conquer(nums, 0, len(nums)-1)


def main():
    print(longestPalindromicSubstring("abdbca"))
    print(longestPalindromicSubstring("cddpd"))
    print(longestPalindromicSubstring("pqr"))


if __name__ == "__main__":
    main()
