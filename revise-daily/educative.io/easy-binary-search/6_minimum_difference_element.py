# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum
# difference with the given ‘key’.

# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

import math


def search_min_diff_element(arr, key):
    l, r = 0, len(arr) - 1
    diff = math.inf

    while l <= r:
        m = l + (r-l)//2

        if key < arr[m]:
            r = m - 1
        elif key > arr[m]:
            l = m + 1
        else:
            return arr[m]
        if diff > abs(arr[m] - key):
            last_seen_closest_index = m
            diff = abs(arr[m] - key)

    return arr[last_seen_closest_index]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


if __name__ == "__main__":
    main()
""" 
Given Problem statement:
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.

Example:

LRUCache cache = new LRUCache(2); // 2 is capacity of the cache. 

cache.put(1, 4);
cache.put(2, 5);
cache.get(1); // returns 4
cache.get(5); // returns -1
cache.put(3, 6); // removes key 2
cache.get(2); // retruns -1

"""

from collections import deque


class LRUCache:
    def __init__(self, capacity):
        capacity = capacity
        mapper = {}
        queue = deque()

    def get(self, key):
        val = -1
        if key in mapper:
            val = mapper[key]
            queue.remove(key)
            queue.insert(0, key)

        print("map:", mapper[key])
        print("queue:", queue)
        return val

    def put(self, key, val):
        if key in mapper:
            mapper[key] = val
        else:
            if len(self.mapper) == capacity:
                oldest_key = queue.pop()
                del mapper[oldest_key]
                print("removing", oldest_key)
                mapper[key] = val
        queue.insert(0, key)
        print("added ", key, val)
        print("map: ", mapper)
        print("queue: ", queue)
        return


if __name__ == "__main__":
    # cache = LRUCache(2)
    # cache.put(1, 4)
    # cache.put(2, 5)
    # print(cache.get(1)) #returns 4
    # print(cache.get(5)) # returns -1
    # print(cache.put(3, 6)) # removes key 2
    # print(cache.get(2)) # retruns -1

    mapper = {}
    mapper[2] = 3
    print(mapper)

