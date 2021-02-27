import heapq


def merge_sorted_lists():

    min_heap = []
    for i, one_d_list in enumerate(two_d_list):
        heapq.heappush(min_heap, (one_d_list[0], 0, one_d_list))

    result = []

    while min_heap:
        val, list_index, one_d_list = heapq.heappop(min_heap)
        result.append(val)

        if list_index+1 < len(one_d_list):
            heapq.heappush(min_heap, (one_d_list[list_index+1], list_index+1, one_d_list))
    return result


if __name__ == '__main__':
    two_d_list = [[3, 7, 23, 456, 653, 864], [23, 34, 567, 578, 678, 9832]]
    print(merge_sorted_lists())
