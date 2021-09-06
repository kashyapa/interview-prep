import math

def max_subarray_circular(nums):
    def maximum_subarray(nums):
        max_till = -math.inf
        max_sum = -math.inf

        for a in nums:
            max_till = max(a, a+max_till)
            max_sum = max(max_sum, max_till)
        return max_sum

    def circular_maximum_subarray(nums):
        def compute_running_maximum(nums):
            partial_sum = nums[0]
            running_sum = [partial_sum]

            for n in nums[1:]:
                partial_sum += n
                running_sum.append(max(running_sum[-1], partial_sum))

            return running_sum

        maximum_begin = compute_running_maximum(nums)
        maximum_end = compute_running_maximum(nums[::-1])[::-1][1:] + [0]
        return max(begin+end for begin, end in zip(maximum_begin, maximum_end))

    return max(maximum_subarray(nums), circular_maximum_subarray(nums))


if __name__ == "__main__":
    print(max_subarray_circular([1, -4, 5, -9, 23, -1]))