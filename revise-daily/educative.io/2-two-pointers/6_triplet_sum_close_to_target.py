import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # we've found a triplet with an exact sum
                return target_sum - target_diff  # return sum of all the numbers

            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_difference) or \
                (abs(target_diff) == abs(smallest_difference) and
                 target_diff > smallest_difference):
                smallest_difference = target_diff  # save the closest and the biggest difference

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - smallest_difference


def triplet_sum_close_to_target2(nums, target):
    triplets = []
    nums.sort()
    closest_target = math.inf
    for i in range(len(nums)-2):
        if i == 0 or nums[i] != nums[i-1]:
            l = i+1
            r = len(nums)-1
            while l < r:
                delta = target - (nums[i] + nums[l] + nums[r])
                if delta == 0:
                    return target - delta
                if abs(delta) < abs(closest_target) or abs(delta) == abs(closest_target) and delta > closest_target:
                    closest_target = delta

                if delta > 0:
                    l += 1
                else:
                    r -= 1

    return target - closest_target



def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
    print(triplet_sum_close_to_target2([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target2([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target2([1, 0, 1, 1], 100))


if __name__ == '__main__':
    main()
