import math
def egg_drop(cases, floors):

    if cases == 1:
        return floors
    min_attempts = math.inf

    for i in range(floors+1):
        # worst case
        max_floors = max(egg_drop(cases-1, i-1), egg_drop(cases, floors-i))
        min_attempts = min(min_attempts, max_floors)

    return min_attempts
