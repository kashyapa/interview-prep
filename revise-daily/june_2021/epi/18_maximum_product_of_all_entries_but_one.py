def maximum_product_of_elements(nums):

    products = [1 for _ in range(len(nums))]

    left_running_product = 1
    for i in range(len(nums)):
        products[i] = left_running_product
        left_running_product *= nums[i]

    right_running_product = 1
    for i in reversed(range(len(nums))):
        products[i] *= right_running_product
        right_running_product *= nums[i]

    return max(products)


if __name__ == "__main__":
    print(maximum_product_of_elements([2, 3, 5, 1, 9, 7]))