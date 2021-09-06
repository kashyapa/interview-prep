import imports

def smallest_window_subsequence(sequence, subsequence):
    counter = imports.Counter(subsequence)
    left = 0
    min_window = imports.inf
    for i, c in enumerate(sequence):
        if c == subsequence[0]:
            matched_count = 0
            j = i
            while j < len(sequence):
                if sequence[j] == subsequence[matched_count]:
                    matched_count += 1
                    counter[sequence[i]] -= 1
                    if matched_count == 0:
                        min_window = min(min_window, i - left + 1)


def smallest_window_subsequence(str, keywords):
    keyword_idx = {k: i for i, k in enumerate(keywords)}
    last_keyword_occurrence = [-1] * len(keywords)
    smallest_subarray = [imports.inf] * len(keywords)

    shortest_distance = imports.inf

    for i, w in str:
        if w in keyword_idx:
            idx_position = keyword_idx[w]
            if idx_position == 0:
                smallest_subarray[0] = 1
            elif smallest_subarray[idx_position-1] != imports.inf:
                distance_to_previous_keyword = i - last_keyword_occurrence[idx_position-1]
                smallest_subarray[idx_position] = distance_to_previous_keyword + smallest_subarray[idx_position-1]
            last_keyword_occurrence[idx_position] = i

            if idx_position == len(keywords) -1 and smallest_subarray[-1] < shortest_distance:
                shortest_distance = smallest_subarray[-1]

    return shortest_distance
