def find_closest_elements(nums, target, K):
    
    def find_nearest_index(key):
        
        start, end = 0, len(nums)-1
        
        while start < end:
            m = start + (end-start) // 2
            if nums[m] == target:
                return m
            elif nums[m] > key:
                end = m - 1
            else:
                start = m + 1
        return start

    idx = find_nearest_index(target)
    l, r = idx-1, idx
    res = []

    for _ in range(K):
        if l >= 0 and r < len(nums):
            diff1 = abs(nums[l]-target)
            diff2 = abs(nums[r]-target)

            if diff1 < diff2:
                res.append(nums[l])
                l -= 1
            else:
                res.append(nums[r])
                r += 1
        elif l >= 0:
            res.append(nums[l])
            l -= 1
        else:
            res.append(nums[r])
            r += 1
    return res
