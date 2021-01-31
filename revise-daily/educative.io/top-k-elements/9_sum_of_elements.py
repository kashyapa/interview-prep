# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

# Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
# Output: 23
# Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
# between 5 and 15 is 23 (11+12).

from heapq import *


def find_sum_of_elements(nums, k1, k2):
    max_heap = []

    for i in range(k2):
        if i < k2 - 1:
            heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    sum = 0
    for i in range(k2 - k1 - 1):
        sum += -heappush(max_heap)

    return sum
