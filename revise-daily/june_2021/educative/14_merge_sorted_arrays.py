def merge_sorted_arrays(lists):

    def merge_lists(new_lists):

        def merge_sorted_lists(i, j):
            pass

        if len(new_lists) == 1:
            return new_lists
        l, r = 0, len(new_lists) - 1

        new_merged_list = []
        while l < r:
            intermediate_list = merge_sorted_lists(l, r)
            new_merged_list.append(intermediate_list)
            l += 1
            r -= 1
            if l == r:
                new_merged_list.append(lists[l])
        return merge_lists(new_merged_list)

    return merge_lists(lists)

