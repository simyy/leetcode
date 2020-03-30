# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Analysis:

LRU cache is a constant size store, must be satisfy:
1. update value, it will be refresh the newest;
2. set key value, it wiil be the newest;
3. if the store is full, then remove the oldest, otherwise set a new one to newest. 

In my solution, use a list to make a order of key, then the front one is oldest and the last is the newest.
For a high speed of get, it use a hash map to store key,value.

"""


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.store = {}
        self.order_list = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.store:
            self.order_list.remove(key)
            self.order_list.append(key)
            return self.store[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Had put in cache or not
        if key in self.store:
            self.store[key] = value
            self.order_list.remove(key)
            self.order_list.append(key)
        else:
            # Exceed capacity or not
            if len(self.order_list) < self.capacity:
                self.order_list.append(key)
                self.store[key] = value
            else:
                del self.store[self.order_list[0]]
                self.order_list = self.order_list[1:]
                self.order_list.append(key)
                self.store[key] = value


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
