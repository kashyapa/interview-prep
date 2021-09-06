def mergeSortedArrays(lists):
    # Write your code here.
    if len(lists) == 1:
        return lists

    def merge_lists(l1, l2):
        i, j = 0, 0
        res = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        while i < len(l1):
            res.append(l1[i])
            i += 1

        while j < len(l2):
            res.append(l2[j])
            j += 1

        return res

    l = 0
    for r in range(1, len(lists)):
        lists[l] = merge_lists(lists[l], lists[r])

    return lists[l]


if __name__ == "__main__":
    print(mergeSortedArrays([ [1,3,5,9,12], [2,3,4,19,22], [-2,11] ]))