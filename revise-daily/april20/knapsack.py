# Given a set of positive numbers, find if we can partition it into two subsets such
# that the sum of elements in both the subsets is equal.


def knapsack(profits, weights, capacity):
    def rec(i, remaining_capacity):
        if i == len(weights):
            return True
        profit_with_item = 0
        if weights[i] <= remaining_capacity:
            profit_with_item = profits[i] + rec(i+1, remaining_capacity-weights[i])
        profit_without_item = rec(i+1, remaining_capacity)

        return max(profit_with_item, profit_without_item)

    return rec(0, capacity)


# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements
# in both the subsets is equal.

def subset_sum(num):
    def rec(i1, i2):

    return rec(0, 0)