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


def merge_sorted_arrays(lists):

    if len(lists) == 1:
        return lists
    l = 0
    r = len(lists) - 1

    intermediate_lists = []
    while l < r:
        merged_res = merge_lists(lists[l], lists[r])
        intermediate_lists.append(merged_res)
        l += 1
        r -= 1

    res2 = merge_sorted_arrays(intermediate_lists)
    return res2


if __name__ == "__main__":
    lists = [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]
    res = merge_sorted_arrays(lists)
    res3 = [x for n in res for x in list(n)]
    print(res3)