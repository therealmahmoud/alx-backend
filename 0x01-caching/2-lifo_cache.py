#!/usr/bin/env python3
""" LIFOCache class. """
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class."""
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
                cc = self.cache_data.popitem()
                print(f"DISCARD: {cc[0]}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Getting elments from cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
