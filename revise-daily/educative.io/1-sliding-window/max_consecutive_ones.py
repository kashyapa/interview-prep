# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
# https://leetcode.com/problems/max-consecutive-ones-ii/


def findMaxConsecutiveOnes(nums):
    first_zero = True
    l = 0
    last_zero_seen = -1
    max_consecutive_ones = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            if first_zero:
                last_zero_seen = i
                first_zero = False
            else:
                l = last_zero_seen + 1
                last_zero_seen = i
        max_consecutive_ones = max(max_consecutive_ones, i - l + 1)

    return max_consecutive_ones

def max_consecutive_ones(self, nums: List[int]) -> int:
    max_ones = 0
    last_zero_seen = -1
    l = 0
    for i, n in enumerate(nums):
        if nums[i] == 0:
            if last_zero_seen >= l:
                l = last_zero_seen + 1
            last_zero_seen = i

        max_ones = max(max_ones, i - l + 1)
    return max_ones