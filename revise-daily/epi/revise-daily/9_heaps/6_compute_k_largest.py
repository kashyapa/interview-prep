import heapq


def k_largest_elements_in_a_heap(arr, k):
    if k <= 0:
        return []

    candidate_max_heap = list()

    candidate_max_heap.append((-arr[0], 0))

    result = []

    for _ in range(k):
        val, idx = heapq.heappop(candidate_max_heap)

        result.append(val)

        left_child_idx = idx * 2 + 1
        if len(arr) > left_child_idx:
            heapq.heappush(candidate_max_heap, (-arr[left_child_idx], left_child_idx))

        right_child_idx = 2*idx + 2
        if len(arr) > right_child_idx:
            heapq.heappush(candidate_max_heap, (-arr[right_child_idx], right_child_idx))

    return result


if __name__ == '__main__':
    k_largest_elements_in_a_heap([], 6)
