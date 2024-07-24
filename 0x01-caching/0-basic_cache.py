#!/usr/bin/env python3
""" BasicCache class. """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class."""
    def put(self, key, item):
        """ Putting elments in cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Getting elments from cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
