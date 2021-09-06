import imports

def maximum_sum_subarray(nums, k):
    rsum = 0
    max_sum = -imports.inf
    for i in range(len(nums)):
        rsum += nums[i]
        if k <= i+1:
            max_sum = max(max_sum, rsum)
            rsum -= nums[i - k + 1]
    return max_sum

