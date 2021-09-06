def triplet_sum_to_zero(nums, target):

    def find_target_pair_sum(t, left):
        first = left - 1
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] == t:
                res.append((nums[first], nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

            if nums[left] + nums[right] > t:
                right -= 1
            else:
                left+=1

    nums.sort()
    res = []
    for i in range(len(nums)-1):
        if i == 0 or nums[i] != nums[i-1]:
            find_target_pair_sum(target-nums[i], i+1)
