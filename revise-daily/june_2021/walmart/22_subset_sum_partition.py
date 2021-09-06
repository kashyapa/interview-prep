def subset_sum_partition(nums):

    def rec(idx, remaining_sum):
        if idx >= len(nums):
            return False
        if remaining_sum == 0:
            return True

        pick_item = False
        if nums[idx] <= remaining_sum:
            pick_item = rec(idx+1, remaining_sum-nums[idx])
        skip_item = rec(idx+1, remaining_sum)

        return pick_item or skip_item

    s = sum(nums)
    return rec(0, s//2)