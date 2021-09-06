import math

def trapping_rain_water(heights):

    def compute_water_volume_partial(wall_heights):
        last_highest = -math.inf
        partial_volume = 0
        for h in wall_heights:
            partial_volume += max(0, last_highest-h)
            last_highest = max(last_highest, h)
        return partial_volume

    max_height = max(heights)
    max_height_index = heights.index(max_height)
    volume = compute_water_volume_partial(heights[:max_height_index])
    volume += compute_water_volume_partial(reversed(heights[max_height_index:]))
    return volume


if __name__ == "__main__":
    print(trapping_rain_water([23,43,54,32,12,76,45]))