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
        if key in self.mapper:
            self.mapper[key] = val
        else:
            if len(self.mapper) == self.capacity:
                oldest_key = self.queue.pop()
                del self.mapper[oldest_key]
                print("removing", oldest_key)
                self.mapper[key] = val
            else:
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

