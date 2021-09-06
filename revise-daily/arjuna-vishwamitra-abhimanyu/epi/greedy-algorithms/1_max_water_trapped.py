def max_water_trapped(heights):
    i, j = 0, len(heights) - 1
    max_water = 0
    while i < j:
        water_volume = (i-j+1) * min(heights[i], heights[j])
        max_water = max(water_volume, max_water)
        if heights[j] > heights[i]:
            i += 1
        else: 
            j -= 1
    return max_water

        