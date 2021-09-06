def dutch_flag(nums):
    pivot = nums[0]
    smaller, equal, larger = 0, 0, len(nums)-1
    while equal < larger:
        if nums[equal] < pivot:
            nums[equal], nums[smaller] = nums[smaller], nums[equal]
            equal += 1
            smaller += 1
        elif nums[equal] > pivot:
            nums[equal], nums[larger] = nums[larger], nums[equal]
            larger -= 1
        else:
            equal += 1
    return nums


print(dutch_flag([2, -1, 3,5,1,7,2,7,0, 4,-5]))