import imports


def smallest_subarray_sum(nums, target):
    rsum = 0
    min_length = imports.inf
    left = 0
    for i in range(len(nums)):
        rsum += nums[i]

        while rsum >= target:
            min_length = min(min_length, i - left + 1)
            # not going to let it go from here
            rsum -= nums[left]
            left += 1
    return min_length
