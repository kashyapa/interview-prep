# Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal
# is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
#
# You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree
# until you cannot, i.e., you will stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both baskets.


def max_fruits_with_2_different_fruits(fruits, k):
    fruit_count = 0
    distinct_fruits = 0
    fruit_map = {}
    l = 0
    max_fruits = 0
    for i, f in enumerate(fruits):
        fruit_count += 1
        if f not in fruit_map:
            fruit_map[f] = 1
            distinct_fruits += 1
            while distinct_fruits > k:
                fruit_map[fruits[l]] -= 1
                if fruit_map[fruits[l]] == 0:
                    distinct_fruits -= 1
                l += 1
        else:
            fruit_map[f] += 1

        max_fruits = max(max_fruits, i - l + 1)
    return max_fruits
