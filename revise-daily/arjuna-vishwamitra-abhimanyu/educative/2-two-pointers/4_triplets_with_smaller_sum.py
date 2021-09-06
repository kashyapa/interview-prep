def triplets_with_smaller_sum(nums, target):

    count = 0
    for i in range(len(nums)):

        start = i + 1
        end = len(nums)-1
        while start < end:
            total = nums[start] + nums[end]
            if total < target:
                count += (end-start)
                start += 1
            else:
                end -= 1
    return count
