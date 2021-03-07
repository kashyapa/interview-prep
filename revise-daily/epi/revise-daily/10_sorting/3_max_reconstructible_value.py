def max_constructible_value(arr):
    max_construbtible_value = 0
    for a in sorted(arr):
        if a > max_constructible_value + 1:
            break
        max_construbtible_value += a
    return max_construbtible_value + 1
