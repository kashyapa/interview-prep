import imports

def find_products_less_than_target(nums, target):

    result = []
    product = 1
    left = 0

    for r in range(len(nums)):
        product *= nums[r]

        while product >= target and left < len(nums):
            product /= nums[left]
            left += 1

        temp_list = imports.deque()

        for i in range(r, left-1, -1):
            temp_list.appendleft(nums[i])
            result.append(list(temp_list))

    return result
