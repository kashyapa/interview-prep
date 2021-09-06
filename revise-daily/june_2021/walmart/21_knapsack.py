def knapsack(profits, weights, capacity):

    def kp_rec(idx, remaining_capacity):
        if idx >= len(profits):
            return 0
        profits_with_item = 0
        if weights[idx] <= remaining_capacity:
            profits_with_item = profits[idx] + kp_rec(idx+1, remaining_capacity-weights[idx])

        profits_without_item = kp_rec(idx+1, remaining_capacity)
        return max(profits_with_item, profits_without_item)
    return kp_rec(0, capacity)
