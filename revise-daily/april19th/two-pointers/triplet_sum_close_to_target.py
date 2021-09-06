# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target
# number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

import math


def find_triplet_with_smallest_sum(nums, target):
    min_diff = math.inf

    def search_pair(first, sum, min_diff):
        i, j = first+1, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == sum:
                return nums[first], nums[i], nums[j]
            diff = sum - (nums[i] + nums[j])
            if (abs(diff) < abs(min_diff)) or (abs(diff) == abs(min_diff) and diff > min_diff):
                min_diff = diff

            if diff > 0:
                i += 1
            else:
                j -= 1
        return min_diff

    nums.sort()
    for i in range(len(nums)-2):
        min_diff = search_pair(i, target-nums[i], min_diff)
    return target - min_diff