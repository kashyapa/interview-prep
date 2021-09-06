def merge_k_sorted_arrays(lists):
    if len(lists) == 1:
        return lists

    def merge(l1, l2):
        i, j = 0, 0
        merged = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                merged.append(l1[i])
            else:
                merged.append(l2[j])

        merged.extend(l1[i:])
        merged.extend(l2[j:])
        return merged

    start, end = 0, len(lists)-1

    new_list = []
    while start < end:
        l1, l2 = lists[start], lists[end]
        merged_sorted_list = merge(l1, l2)
        new_list.append(merged_sorted_list)
        start += 1
        end -= 1
    if start == end:
        new_list.append(lists[start])

    return merge_k_sorted_arrays(new_list)


# i'm taking Google by it's hair
# DONE and DUSTED
# Google locked

