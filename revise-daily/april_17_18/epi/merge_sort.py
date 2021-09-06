def merge_sort(arr):
    def merge(arr1, arr2):
        i, j = 0, 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        res.extend(arr1[i:])
        res.extend(arr2[j:])
        return res

    if len(arr) == 1:
        return arr

    m = len(arr)// 2
    left = arr[:m]
    right = arr[m:]
    return merge(merge_sort(left), merge_sort(right))


if __name__ == "__main__":
    print(merge_sort([8, 5, 2, 9, 5, 6, 3]))
