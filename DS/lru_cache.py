import collections


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(key)
        self.cache[key] = value

l = LRUCache(2)
l.set(1, 2)
l.set(3, 4)
l.set(4, 5)  # flushes out key 3
l.get(1)
l.get(3)
l.get(4)
l.get(1)
l.get(4)
l.set(5, 6)  # flushes out key 4
l.get(4)
l.get(1)