"""
Implement an LRU (Least Recently Used) Cache in Python with two operations:

get(key) – returns the value if it exists, otherwise -1.
put(key, value) – inserts/updates the key with the given value. If the cache is full, evict the least recently used item.

Use a capacity of 2 for the example. Show a short test demonstrating eviction and retrieval.
"""


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self._init_head_and_tail()

    def _init_head_and_tail(self):
        self.head = Entry(0,0)
        self.tail = Entry(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, entry):
        ...


