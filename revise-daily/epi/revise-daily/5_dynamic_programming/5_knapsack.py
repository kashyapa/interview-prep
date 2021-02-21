def knapsack(profits, weights, capacity):

    def knapsack_rec(capacity, index):

        if index == len(weights):
            return 0

        with_item = 0
        if weights[index] <= capacity:
            with_item = profits[index]+ knapsack_rec(capacity-weights[index])

        skip_item = knapsack_rec(capacity)

        return max(with_item, skip_item)

    return knapsack_rec(capacity, 0)



if __name__ == '__main__':
