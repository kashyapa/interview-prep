def find_LCS_length(s1, s2):

# COMMON SUBSEQUENCE

    def rec(i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            return count
        if s1[i1] == s2[i2]:
            return rec(i1+1, i2+1, count+1)

        return max(rec(i1, i2+1, count), rec(i1+1, i2, count))

    return rec(0, 0, 0)


def longest_common_substring(s1, s2):

    def rec(i1, i2, count):

        if i1 == len(s1) or i2 == len(s2):
            return count
        if s1[i1] == s2[i2]:
            count = rec(i1+1, i2+1, count+1)
        non_matching_count = max(rec(i1, i2+1, 0), rec(i1+1, i2, 0))

        return max(count, non_matching_count)

    return rec(0, 0, 0)


def longest_palindromic_sequence(s):

    def rec(i1, i2):
        if i1 > i2:
            return 0
        if i1 == i2:
            return 1

        if s[i1] == s[i2]:
            return 2 + rec(i1+1, i2-1)
        return max(rec(i1+1, i2), rec(i1, i2-1))

def longest_palindromic_substring(s):

    def palindrome_length(s, l, r):

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        return s[l+1:r]

    max_length = 0

    for i in range(len(s)):
        even_length = palindrome_length(s, i, i)
        odd_length = palindrome_length(s, i, i+1)
        max_length = max(max_length, max(len(even_length), len(odd_length)))
    return max_length


def count_palindromic_substrings(s):

    def find_palindrome(s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return r - l + 1

    count = 0
    for i in range(len(s)):
        count += find_palindrome(s, i, i)
        count += find_palindrome(s, i, i+1)
    return count


def find_minimum_cuts(s):
    if not s:
        return 0

    def is_palindromic(s):
        return s == s[::-1]

    min_cuts = len(s)

    for i in range(len(s)):
        substr = s[:i+1]
        if is_palindromic(substr):
            min_cuts = 1 + find_minimum_cuts(s[i+1:])
    return min_cuts


def find_min_cuts(s):
    def is_palindromic(s, l, r):
        return s == s[::-1]

    def rec(s, start, end):
        if start>end:
            return 0

        min_cuts = end-start+1

        for i in range(start, end+1):
            if is_palindromic(s, start, i):
                min_cuts = min(min_cuts, 1 + rec(s, i, end))
        return min_cuts

    return rec(s, 0, len(s)-1)


def knapsack(weights, profits, capacity):

    def rec(idx, remaining_capacity):

        if idx == len(weights):
            return 0
        profit_with_item = 0
        if weights[idx] <= remaining_capacity:
            profit_with_item = profits[idx] + rec(idx+1, remaining_capacity-weights[i])
        profit_without_item = rec(idx+1, remaining_capacity)

        return max(profit_with_item, profit_without_item)
    return rec(0, capacity)


def subset_sum_partition(nums):

    def rec(idx, remaining_sum):
        if idx == len(nums):
            return False

        if remaining_sum == 0:
            return True

        if nums[idx] <= remaining_sum:
            if rec(idx+1, remaining_sum - nums[idx]):
                return True

        return rec(idx+1, remaining_sum)

    s = sum(nums)
    return rec(0, s//2)

def subset_sum(nums, s):

    def rec(idx, remaining_sum):
        if idx == len(nums):
            return False

        if remaining_sum == 0:
            return True

        if nums[idx] <= remaining_sum:
            if rec(idx+1, remaining_sum-nums[idx]):
                return True

        return rec(idx+1, remaining_sum)

    return rec(0, s)


def minimum_subset_difference(nums):

    def rec(i, sum1, sum2):

        if i == len(nums):
            return abs(sum1-sum2)

        diff1 = rec(i+1, sum1+nums[i], sum2)
        diff2 = rec(i+1, sum1, sum2+nums[i])

        return min(diff1, diff2)

    return rec(0, 0, 0)

import math

def count_subset_sum(nums, target):

    def rec(i, remaining_target):

        if i == len(nums):
            return 0

        if remaining_target == 0:
            return 1

        count = 0
        if nums[i] <= remaining_target:
            count = rec(i+1, remaining_target-nums[i])

        count += rec(i+1, remaining_target)
        return count

    return rec(0, target)



def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))


    print(longest_common_substring("abdca", "cbda"))
    print(longest_common_substring("passport", "ppsspt"))


if __name__ == "__main__":
    main()
