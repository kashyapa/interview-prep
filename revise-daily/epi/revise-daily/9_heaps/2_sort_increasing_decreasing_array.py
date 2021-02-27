def sort_increasing_decreasing_array(A):
    sorted_subarrays = []
    increasing_subarray_type = True
    start_idx = 0
    for i in range(1, len(A)+1):
        if i == len(A) or ((A[i-1] > A[i] and increasing_subarray_type) or
            (A[i-1] < A[i] and not increasing_subarray_type)):
            sorted_subarrays.append(A[start_idx:i] if increasing_subarray_type else
                                    A[i-1:start_idx-1:-1])
            start_idx = i
            increasing_subarray_type = not increasing_subarray_type

    return sorted_subarrays


if __name__ == '__main__':
    print(sort_increasing_decreasing_array([32, 35, 45, 67, 43, 32, 21, 10]))
