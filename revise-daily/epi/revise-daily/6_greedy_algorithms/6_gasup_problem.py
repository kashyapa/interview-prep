from math import inf


def find_best_city_to_gasup(gallons: list, distances: list):
    MPG = 5
    remaining_gas = 0
    min_gas = inf
    ample_city = 0
    for i in range(1, len(gallons)):
        remaining_gas += gallons[i-1] - distances[i-1] // MPG
        if remaining_gas < min_gas:
            min_gas = remaining_gas
            ample_city = i

    return ample_city
