"""
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
        self.N = capacity
        self.Store = {}
        self.OrderList = []
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.Store:
            self.OrderList.remove(key)
            self.OrderList.append(key)
            return self.Store[key]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.Store:
            self.OrderList.remove(key)
            self.OrderList.append(key)
            self.Store[key] = value
        else:
            if len(self.OrderList) < self.N:
                self.Store[key] = value
                self.OrderList.append(key)
            else:
                del self.Store[self.OrderList[0]]
                self.OrderList = self.OrderList[1:]
                self.OrderList.append(key)
                self.Store[key] = value
            
        
