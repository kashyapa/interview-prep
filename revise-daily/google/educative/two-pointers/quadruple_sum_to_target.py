def quadruple_sum_to_target(nums, target):
    nums.sort()

    def search_pairs(first, second, left):
        right = len(nums)-1
        res = []
        while left < right:
            cur_sum = first + second + nums[left] + nums[right]
            if cur_sum == target:
                res.append((first, second, nums[left], nums[right]))
                left += 1
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
        return res

    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            first, second = nums[i], nums[j]
            res = search_pairs(first, second, j+1)
            if not res:
                return res
    return []
