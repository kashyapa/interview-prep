def quadruple_sum(nums, target):

    nums.sort()
    results = []

    for i in range(len(nums)-3):
        if i == 0 or nums[i] != nums[i-1]:
            for j in range(i+1, len(nums)-2):
                first, second = nums[i], nums[j]
                if j-i == 1 or nums[j] != nums[j-1]:
                    start = j+1
                    end = len(nums)-1
                    while start < end:
                        total = first + second + nums[start] + nums[end]
                        if total == target:
                            results.append((i, j, start, end))

                            start += 1
                            end -= 1
                            while start < end and nums[start] == nums[start-1]:
                                start += 1
                            while start < end and nums[start] == nums[end+1]:
                                end -= 1
                            
                        elif total > target:
                            end -= 1
                        else:
                            start += 1
