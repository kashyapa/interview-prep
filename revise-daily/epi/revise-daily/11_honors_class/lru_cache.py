from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.mapper = dict()
        self.queue = deque()

    def get(self, key):
        val = -1
        if key in self.mapper:
            val = self.mapper[key]
            self.queue.remove(key)
            self.queue.insert(0, key)

            print("map:", self.mapper[key])
            print("queue:", self.queue)
        return val

    def put(self, key, val):
        self.mapper[key] = val

        if len(self.mapper) == self.capacity:
            oldest_key = self.queue.pop()
            del self.mapper[oldest_key]
            print("removing", oldest_key)
            self.mapper[key] = val

        self.queue.insert(0, key)
        print("added ", key, val)
        print("map: ", self.mapper)
        print("queue: ", self.queue)
        return


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 4)
    cache.put(2, 5)
    print(cache.get(1)) #returns 4
    print(cache.get(5)) # returns -1
    print(cache.put(3, 6)) # removes key 2
    print(cache.get(2)) # retruns -1
    #
    # mapper = {}
    # mapper[2] = 3
    # print(mapper)



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

