def dutch_flag_partition(nums):

    smaller, equal, larger = 0,0, len(nums)-1
    pivot = nums[0]

    while equal < larger:
        if nums[equal] < pivot:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            smaller += 1
            equal += 1
        elif nums[equal] > pivot:
            nums[larger], nums[equal] = nums[equal], nums[larger]
            larger -= 1
        else:
            equal += 1
        
    return nums
