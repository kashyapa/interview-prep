MPG = 45

def gasup(gallons, distances):
    remaining_gas = 0
    for i in range(1, len(distances)):
        remaining_gas += gallons[i-1] - (distances[i-1]) // MPG
        if remaining_gas < min_gas:
            min_gas = remaining_gas
            ample_city = i
    return ample_city

