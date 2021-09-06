from collections import Counter

def fruits_into_basket(fruits):
    i = 0
    distinct_fruits = 0
    left = 0
    max_fruits = 0
    baskets = Counter()
    while i < len(fruits):
        f = fruits[i]
        if baskets[f] == 0:
            distinct_fruits += 1
        baskets[f] += 1
        while distinct_fruits > 2:
            baskets[left] -= 1
            if baskets[left] == 0:
                distinct_fruits -= 1
            left += 1
        max_fruits = max(max_fruits, i - left + 1)
    return max_fruits
