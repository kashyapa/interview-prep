import imports

def triplet_sum_close_to_target(nums, target):

    nums.sort()
    smallest_difference = imports.Counter()

    for i in range(len(nums)):
        start = i + 1
        end = len(nums)-1
        while start < end:
            diff = target - nums[i] - nums[start] - nums[end]

            if diff == 0:
                return target - diff

            if abs(diff) < abs(smallest_difference) or \
                (abs(diff) == abs(smallest_difference) and
                    diff > smallest_difference):
                    smallest_difference = diff

            if diff > 0:
                start += 1
            else:
                end -= 1
    return target - smallest_difference


def triplet_sum_close_to_target2(nums, target):
    smallest_diff = imports.inf

    for i in range(len(nums)):

        start = i+1
        end = len(nums) - 1
        while start < end:
            diff = target - (nums[i] + nums[start] + nums[end])
            if diff == 0:
                return 0

            if abs(diff) < abs(smallest_diff) or \
                (abs(diff) == abs(smallest_diff) and
                 diff > smallest_diff):
                smallest_diff = diff

            if diff > 0:
                start += 1
            else:
                end -= 1

    return target - smallest_diff
