#!/usr/bin/env python3
""" FIFOCache class. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class."""
    def __init__(self):
        """Initializes the cache."""
        super().__init__()

    def put(self, key, item):
        """ Putting elments in cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = list(self.cache_data.items())[0]
            key_to_remove = first_item[0]
            remove_val = self.cache_data.pop(key_to_remove)
            print(f"DISCARD: {key_to_remove}")

    def get(self, key):
        """ Getting elments from cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
