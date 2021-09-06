def fruits_into_basket(fruits, k):
    import imports
    fruit_counter = imports.Counter()
    distinct = 0
    left = 0
    max_fruits = 0
    for i, f in enumerate(fruits):
        fruit_counter[f] += 1
        if fruit_counter[f] == 1:
            distinct += 1
        while distinct > k:
            left_fruit = fruits[left]
            fruit_counter[left_fruit] -= 1
            if fruit_counter[left_fruit] == 0:
                distinct -= 1
            left += 1
        max_fruits = max(i-left+1, max_fruits)

    return max_fruits
