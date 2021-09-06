"""
## Prompt
Given a restaurant geolocation ( longitude / latitude).
Find at least 3 closest drivers near the restaurant who can be assigned for delivery.
### Input
Restaurant Coordinates -> [x,y]
GetDashers() - >returns a list of dasher objects.
Each dasher object has 3 properties.
 * Dasher ID
 * Last location [x,y]
 * Rating (0 - 100) higher the better.

 ### Assumptions
GetDashers() when called will give you a list of all active dashers.
Use any distance function you want. Preferably euclidean distance / manhattan distance function.
In case of a tie, use dasher rating as tie breaker.
"""
# input is a list of driver
from collections import namedtuple
import heapq


class Restaurant:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label


class Driver:

    def __init__(self, x, y, rating, label):
        self.x = x
        self.y = y
        self.rating = rating
        self.label = label

    def __lt__(self, other):
        other_distance = distance(other.x, other.y)
        this_distance = distance(self.x, self.y)
        return this_distance < other_distance if this_distance != other_distance else other.rating - self.rating

    @staticmethod
    def distance(x, y, p):
        return (abs(p.x * p.x - x * x)) + abs((p.y * p.y - y * y))


def find_best_drivers(drivers_list, rest, k):
    max_heap = []
    for driver in drivers_list:
        heapq.heappush(max_heap, (-Driver.distance(driver.x, driver.y, rest), driver))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
        for item in max_heap:
            print(item[1].label, abs(item[0]))
    res = []
    for d in max_heap:
        res.append(d[1].label)
    print(res)
    return res


if __name__ == "__main__":
    rest = Restaurant(3, 4, 98234)
    drivers = [Driver(4, 6, 4, 2000), Driver(2, 6, 3, 9832), Driver(9, 7, 2, 34534), Driver(7, 2, 3, 2342),
               Driver(3, 4, 4, 1000), Driver(3, 4, 2, 343400),  Driver(3, 4, 1, 32000),  Driver(3, 4, 0, 34500)]
    find_best_drivers(drivers, rest, 3)