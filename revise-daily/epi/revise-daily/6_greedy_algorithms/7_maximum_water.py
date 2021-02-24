def maximum_water_trapped(heights):
    i, j = 0, len(heights) - 1
    max_water = 0
    while i < j:
        water_volume = (j - i + 1) * min(heights[i],heights[j])
        max_water = max(water_volume, max_water)
        if heights[j] > heights[i]:
            i += 1
        elif heights[i] > heights[j]:
            j -= 1
        else:
            i += 1
            j -= 1
    return max_water