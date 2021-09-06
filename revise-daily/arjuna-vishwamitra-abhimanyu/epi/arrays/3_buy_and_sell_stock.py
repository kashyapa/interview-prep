def buy_and_sell_at_profit(nums):
    
    max_profit = 0
    lowest_price = nums[0]
    for i in range(1, len(nums)):
        lowest_price = min(nums[0], lowest_price)
        max_profit = max(nums[i]-lowest_price)
    return max_profit


def buy_and_sell_twice(nums):

    trades = [0] * len(nums)
    min_so_far = nums[0]
    max_profit = 0
    for i in range(1, len(nums)):
        min_so_far = min(min_so_far, nums[i])
        max_profit = max(nums[i] - min_so_far, max_profit)
        trades[i] = max_profit

    max_price_so_far = nums[len(nums)-1]
    max_profit = 0
    for i in range(len(nums)-2, -1, -1):
        max_price_so_far = max(max_price_so_far, nums[i])
        max_profit = max(max_profit, trades[i] + max_price_so_far - nums[i])
        
    return max_profit
