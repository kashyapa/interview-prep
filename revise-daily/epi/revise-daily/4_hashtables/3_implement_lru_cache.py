from collections import OrderedDict


class Lrucache:
    def __init__(self, capacity):
        self.lrucache = OrderedDict()
        self.capacity = capacity

    def insert(self, key, value):
        prev_value = value
        if key in self.lrucache:
            prev_value = self.lrucache.pop(key)
        elif len(self.lrucache) == self.capacity:
            self.lrucache.popitem()

        self.lrucache.setdefault(key, value)
        self.lrucache.move_to_end(key)

        return prev_value

    def get(self, key):
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
            return self.lrucache.pop(key)
        else:
            raise KeyError

    def remove(self, key):
        return self.lrucache.pop(key) is not None
