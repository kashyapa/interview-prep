import imports

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = imports.deque([])
        self.cache = {}

    def insert(self, k, v):
        if k in self.cache:
            self.queue.remove(k)
        elif len(self.queue) == self.capacity:
            self.queue.popleft()

        self.cache[k] = v
        self.queue.append(k)

    def get(self, k):
        if k not in self.cache:
            raise KeyError
        self.queue.remove(k)
        self.queue.append(k)
        return self.cache[k]
    