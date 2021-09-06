def find_k_closest_elements(arr, k, target):

    def find_closest_index(arr, target):

        lo, hi = 0, len(arr)-1

        while lo <= hi:
            mid = lo + (hi -lo) // 2
            if arr[mid] == target:
                return mid

            if arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid+1
        return lo


    index = find_closest_index(arr, target)
    l = index-1
    r = index
    res= []
    for _ in range(k):
        if l >= 0 and r < len(arr):
            if abs(arr[l]-target) > abs(arr[r]-target):
                res.append(arr[r])
                r += 1
            else:
                res.append(arr[l])
                l -=1
        elif l >= 0:
            res.append(arr[l])
            l-=1
        else:
            res.append(arr[r])
            r+=1
    return res



