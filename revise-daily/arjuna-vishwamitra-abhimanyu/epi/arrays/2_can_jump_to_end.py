def can_jump_to_end(nums):
    max_reach = 0
    
    for i in range(len(nums)):
        if i <= max_reach:
            max_reach = max(max_reach, i + nums[i])
    return max_reach >= len(nums)