import math
def find_LCS_length(s1, s2):

    def rec(i1, i2, count):

        if i2 == len(s2) or i1 == len(s1):
            return 0

        if s1[i1] == s2[i2]:
            count = rec(i1+1, i2+1, count+1)

        count_without_match = max(rec(i1+1, i2, 0), rec(i1, i2+1, 0))

        return max(count, count_without_match)
    return rec(0, 0, 0)


def longest_common_substring_dp(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_length = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            max_length = max(max_length, dp[i][j])
    return max_length


def find_longest_common_subsequence(s1, s2):

    def rec(i1, i2):

        if i1 == len(s1) or i2 == len(s2):
            return 0

        if s1[i1] == s2[i2]:
            return 1 + rec(i1+1, i2+1)
        return max(rec(i1, i2+1), rec(i1+1, i2))


def find_longest_common_subsequence_dp(s1, s2):

    n1 = len(s1)
    n2 = len(s2)
    max_length = 0
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] == 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        max_length = max(max_length, dp[i][j])
    return max_length


def find_LIS_length(arr):

    def rec(prev_idx, cur_idx):
        if cur_idx == len(arr):
            return 0

        c1 = 0
        if prev_idx == -1 or arr[cur_idx] > arr[prev_idx]:
            c1 = 1 + rec(cur_idx, cur_idx+1)
        c2 = rec(prev_idx, cur_idx+1)
        return max(c1, c2)
    return rec(-1, 0)


def find_LIS(arr):
    max_length = 0
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
        max_length = max(max_length, dp[i])
    return max_length


def find_max_sum_in_increasing_subsequence(arr):

    def rec(prev_idx, cur_idx):

        if cur_idx == len(arr):
            return 0

        c1 = 0
        if prev_idx == -1 or arr[prev_idx] < arr[cur_idx]:
            c1 = arr[cur_idx] + rec(cur_idx, cur_idx+1)
        c2 = rec(prev_idx, cur_idx+1)
        return max(c1, c2)

def max_increasing_subsequence_dp(arr):
    dp = [[0] for _ in range(len(arr))]
    max_sum = -math.inf
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], arr[i] + dp[j])
            max_sum = max(dp[i], max_sum)

    return max_sum


def shortest_common_super_sequence(s1, s2):

    def rec(i1, i2):

        if i1 == len(s1):
            return len(s2) - i2
        if i2 == len(s2):
            return len(s1) - i1

        c1 = 0
        if s1[i1] == s2[i1]:
            return 1 + rec(i1+1, i2+1)
        return 1 + min(rec(i1+1, i2), rec(i1, i2+1))

def shortest_common_supersequence_dp(s1, s2):

    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    for i in range(len(s1)+1):
        dp[i][0] = i
    for j in range(len(s2)+1):
        dp[0][j] = j

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


def longest_repeating_subsequence(str):
    def rec(i1, i2):

        if i1 == len(str) or i2 == len(str):
            return 0

        c1 = 0
        if i1 != i2 and str[i1] == str[i2]:
            return 1 + rec(i1+1, i2+1)

        return max(rec(i1+1, i2), rec(i1, i2+1))


def subsequence_pattern_match(str, pattern):

    def rec(i1, i2):
        if i2 == len(pattern):
            return 1

        if i1 == len(str):
            return 0
        c1 = 0
        if str[i1] == pattern[i2]:
            c1 = rec(i1+1, i2+1)

        c2 = rec(i1+1, i2)
        return c1+c2


def longest_bitonic_subsequence(nums):
    max_length = 0
    def longest_inc_subsequence(prev_idx, cur_idx):

        if cur_idx == len(nums):
            return 0
        c1 = 0
        if prev_idx == -1 or nums[cur_idx] > nums[prev_idx]:
            c1 = longest_inc_subsequence(cur_idx, cur_idx+1)
        c2 = longest_inc_subsequence(prev_idx, cur_idx+1)
        return max(c1, c2)

    def longest_inc_subsequence_rev(prev_idx, cur_idx):

        if cur_idx < 0:
            return 0
        c1 = 0
        if prev_idx == -1 or nums[cur_idx] > nums[prev_idx]:
            c1 = longest_inc_subsequence(cur_idx, cur_idx-1)
        c2 = longest_inc_subsequence(prev_idx, cur_idx-1)
        return max(c1, c2)

    for i in range(len(nums)):
        l1 = longest_inc_subsequence(-1, i)
        l2 = longest_inc_subsequence_rev(-1, i)
        max_length = max(max_length, l1+l2-1)
    return max_length


def longest_alternating_sequence(nums):

    def rec(prev_idx, cur_idx, increasing):
        if cur_idx == len(nums):
            return 0
        c1 = 0
        if increasing:
            if prev_idx == -1 or nums[cur_idx] > nums[prev_idx]:
                c1 = 1 + rec(cur_idx, cur_idx+1, not increasing)

        else:
            if prev_idx == -1 or nums[cur_idx] < nums[prev_idx]:
                c1 = 1 + rec(cur_idx, cur_idx+1, not increasing)

        c2 = rec(prev_idx, cur_idx+1, increasing)

        return max(c1, c2)

def edit_distance(s1, s2):

    def rec(i1, i2):
        if i1 == len(s1):
            return len(s2) - i2
        if i2 == len(s2):
            return len(s1) - i1

        if s1[i1] == s2[i2]:
            return rec(i1+1, i2+1)

        add_character = 1+rec(i1, i2+1)
        delete_character = 1+rec(i1+1, i2)
        substitute = 1+rec(i1+1, i2+1)
        return min(add_character, delete_character, substitute)


def strings_interleaving(m, n, p):

    def rec(mi, ni, pi):

        if mi == len(m) and ni == len(n) and pi == len(p):
            return True

        if pi == len(p):
            return False

        c1, c2 = False, False
        if p[pi] == m[mi]:
            c1 = rec(mi+1, ni, pi+1)
        if p[pi] == n[ni]:
            c1 = rec(mi, ni+1, pi+1)
        return c1 or c2


def longest_palindromic_subsequence(str):

    def rec(l, r):
        if l > r:
            return 0
        if l == r:
            return 1

        c1 = 0
        if str[l] == str[r]:
            return 2 + rec(l+1, r-1)
        c1 = rec(l, r-1)
        c2 = rec(l+1, r)
        return max(c1, c2)


def longest_palindromic_subsequence_dp(str):
    dp = [[0 for _ in range(len(str))] for _ in range(len(str))]
    n = len(str)
    # every sequence with one element is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    for i in range(len(str)-1, -1, -1):
        for j in range(i+1, n):
            if str[i] == str[j]:
                dp[i][j] = 2 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            max_length = max(max_length, dp[i][j])

def longest_palindromic_substring(str):

    def rec(l, r):
        if l > r:
            return 0
        if l == r:
            return 1

        if str[l] == str[r]:
            remaining_length = r-l-1
            if remaining_length == rec(l+1, r-1):
                return remaining_length + 2

        c1 = rec(l+1, r)
        c2 = rec(l, r-1)
        return max(c1, c2)


def longest_palindromic_substring_dp(str):
    dp = [[0 for _ in range(len(str))] for _ in range(len(str))]
    for i in range(len(str)):
        dp[i][i] = 1
    max_len = 1
    for i in range(len(str)-1, -1, -1):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                dp[i][j] = 2 + dp[i+1][j-1]

    return dp[0][len(str)-1]


def longest_palindromic_substring(str):
    def count_length(l, r):

        while l >= 0 and r < len(str) and str[l] == str[r]:
            l -= 1
            r += 1
        return r-l-1

    for i in range(len(str)):
        odd_length = count_length(i, i)
        even_length = count_length(i, i + 1)
        max_length = max(max_length,  max(even_length, odd_length))



def count_palindromic_substrings(str):
    def count_palindrome(l, r):
        count = 0
        while l >= 0 and r < len(str) and str[l] == str[r]:
            count +=1
            l -= 1
            r += 1
        return count
    count = 0
    for i in range(len(str)):
        count += count_palindrome(i, i)
        count += count_palindrome(i, i+1)
    return count


def knapsack(profits, capacity, weights):

    def rec(idx, remaining_capacity):
        if idx == len(weights) or remaining_capacity < 0:
            return 0

        profit_with_item = 0
        if weights[idx] <= remaining_capacity:
            profit_with_item = profits[idx] + rec(idx+1, remaining_capacity-weights[idx])
        profit_without_item = rec(idx+1, remaining_capacity)
        return max(profit_with_item, profit_without_item)

def knapsack_dp(profits, weights, capacity):

    dp = [[0 for _ in range(capacity+1) ] for _ in range(len(profits))]

    for i in range(capacity+1):
        dp[0][i] = profits[0] if weights[0] < i else 0
    for i in range(len(weights)):
        for j in range(capacity+1):
            if weights[i] <= j:
                dp[i][j] = profits[i] + dp[i][j-weights[i]]
            dp[i][j] = max(dp[i][j], dp[i-1][j])

    return dp[-1][-1]


def subset_sum(nums):

    total = sum(nums) // 2

    def rec(idx, remaining_sum):
        if idx == len(nums):
            return False
        if remaining_sum == 0:
            return True

        if nums[idx] <= remaining_sum:
            if rec(idx+1, remaining_sum-nums[idx]):
                return True

        return rec(idx+1, remaining_sum)

    rec(0, total)

def minimum_subset_sum(nums):

    def rec(idx, sum1, sum2):
        if idx == len(nums):
            return abs(sum1-sum2)
        diff1 = rec(idx+1, nums[idx]+sum1, sum2)
        diff2 = rec(idx+1, sum1, sum2+nums[idx])

        return min(diff1, diff2)

def can_partition_dp(nums):
    s = sum(nums)
    n = len(nums)
    dp = [[False for _ in range(s/2 +1)]for y in range(n)]

    for i in range(n):
        dp[i][0] = True

    for j in range(1, s/2 + 1):
        dp[0][j] = nums[0] == j
    for i in range(1, n):
        for j in range(1, s/2 + 1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))
    print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_length([-4, 10, 3, 7, 15]))
    print(find_LIS([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS([-4, 10, 3, 7, 15]))
    print("********")
    # print(longest_increasing_subsequence([4, 2, 3, 6, 10, 1, 12]))
    # print(longest_increasing_subsequence([-4, 10, 3, 7, 15]))
    # print(longest_increasing_subsequence([4, 2, 3, 6, 10, 1, 12]))
    # print(longest_increasing_subsequence([-4, 10, 3, 7, 15]))

if __name__ == "__main__":
    main()
