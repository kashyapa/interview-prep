# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# https://leetcode.com/problems/max-consecutive-ones-iii/


def longestOnes(A, K):
    ones = 0
    zeroes = 0
    i = 0
    l = 0
    max_consecutive_ones = 0
    while i < len(A):
        if A[i] == 1:
            ones += 1
        else:
            zeroes += 1
        while zeroes > K:
            if A[l] == 0:
                zeroes -= 1
            l += 1
        max_consecutive_ones = max(max_consecutive_ones, i - l + 1)
        i += 1
    return max_consecutive_ones


def longestOnes(self, A: List[int], K: int) -> int:
    ones = 0
    l = 0
    max_ones = 0
    for i, n in enumerate(A):
        if n == 1:
            ones += 1
        while i - l - ones >= K:
            if A[l] == 1:
                ones -= 1
            l += 1
        max_ones = max(i-l+1, max_ones)
    return max_ones