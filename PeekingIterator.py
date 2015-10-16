"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Analysis:

peek is a function which return double next result, but is can't affect next function.
Then, we must use a cache to store the value of next value.

1. if no cache, we will update it when call peek, cache will store next value.
2. when we call next function, fisrt thing is to detect the cache value. 
   if it exists, it will be the next value, then clear the cache.(cache only can be set when call peek)
3. if have cache, it means have next value, then hasNext will be return ture, otherwise return call hasNext fucntion.
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cache = None
        self.iter  = iterator
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.cache:
            self.cache = self.iter.next()
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        if not self.cache:
            self.cache = self.iter.next()
        r = self.cache
        self.cache = None
        return r
            
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cache:
            return True
        return self.iter.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
