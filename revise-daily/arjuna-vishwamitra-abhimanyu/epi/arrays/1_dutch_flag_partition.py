def dutch_flag_partition(nums):
    pivot = nums[0]

    smaller, larger = 0, len(nums)-1
    equal = 0
    while equal < larger:
        if nums[equal] < pivot:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            equal += 1
            smaller += 1
        elif nums[equal] > pivot:
            nums[larger], nums[equal] = nums[equal], nums[larger]
            larger -= 1
        else:
            equal += 1
    return equal
