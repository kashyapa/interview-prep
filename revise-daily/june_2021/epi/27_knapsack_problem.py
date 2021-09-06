def knapsack_problem(weights, profits, capacity):

    def rec(i, remaining_capacity):

        if i == len(weights):
            return 0
        profit_pick_item = 0
        if weights[i] <= remaining_capacity:
            profit_pick_item = profits[i] + rec(i+1, remaining_capacity-weights[i])

        profit_without_pic = rec(i+1, remaining_capacity)
        return max(profit_pick_item, profit_without_pic)

    return rec(0, capacity)