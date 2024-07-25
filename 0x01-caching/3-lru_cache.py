#!/usr/bin/env python3
""" LRUCache class. """
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class."""
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Putting elments in cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lru_key = self.cache_data.popitem(True)
                print("DISCARD:", lru_key[0])
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Getting elments from cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
