import math
# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass

def compute_maximum_subarray(arr):
    running_max = 0
    running_min = 0
    max_sum = arr[0]
    min_sum = arr[0]
    total = 0

    running_sum = 0
    for a in arr:
        running_max = max(running_max+a, a)
        running_min = min(running_min+a, a)

        max_sum = max(max_sum, running_max)
        min_sum = min(min_sum, running_sum)
        total += a
    return max(max_sum, total-min_sum) if max_sum > 0 else max_sum

