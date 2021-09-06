def find_products_less_than_target(nums, target):
    product = 1
    l = 0
    result = []

    for i in range(len(nums)):
        product *= nums[i]
        while product >= target:
            product = product // nums[l]
            l += 1

        temp_list = []
        for j in range(i, l-1, -1):
            temp_list.append(nums[j])
            result.append(temp_list)
    return result
