def buy_and_sell_stock_once(arr):
    smallest, max_profit = arr[0], 0

    for i in range(len(arr)):
        smallest = min(arr[i], smallest)
        max_profit = max(max_profit, arr[i]-smallest)
    return max_profit


def buy_and_sell_stock_twice(arr):
    first_sell_profits = []
    smallest = arr[0]
    max_first_sell_profit = 0

    for i in range(len(arr)):
        smallest = min(smallest, arr[i])
        max_first_sell_profit = max(arr[i]-smallest, max_first_sell_profit)
        first_sell_profits.append(max_first_sell_profit)

    max_price = arr[-1]
    max_profit = 0
    for i in reversed(range(len(arr))):
        max_price = max(arr[i], max_price)
        max_profit = max(first_sell_profits[i] + max_price - arr[i], max_profit)

    return max_profit
