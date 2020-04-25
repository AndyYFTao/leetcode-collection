# https://leetcode.com/problems/lru-cache/discuss/594885/Python-Simple-implementation-with-deque-(slow)-and-OrderedDict-(fast)
# https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)  # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion.
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict

        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)