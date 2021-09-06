import math

def maximum_circular_subarray(arr):
    def max_sum_normal(arr):
        local_max = 0
        global_max = -math.inf
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            local_max = max(arr[i], sum)
            global_max = max(global_max, local_max)
        return global_max

    def circular_sum(arr):
        def max_sum_circular(arr):
            partial_sum = arr[0]
            running_sum = [partial_sum]
            for i in range(1, len(arr)):
                partial_sum += arr[i]
                running_sum.append(max(running_sum[-1], partial_sum))

            return running_sum

        max_from_begin = max_sum_circular(arr)
        max_from_end = max_sum_circular(arr[:-1])[::-1][1:] + [0]

        return max(begin + end for begin, end in zip(max_from_begin, max_from_end))

    return max(max_sum_normal(arr), circular_sum(arr))

if __name__ == "__main__":
    print(maximum_circular_subarray([22, -23, 1, -25, 76, 94, 54]))