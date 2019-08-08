"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

Analysis：

Because it contains search and find functions, we must use an index to implementation this.

So, tire tree can use to do that, 

1. tree node struct 

struct node:
  isWord or not: current path is a word or not 
  sub_dict: sub path 
  
2. build a tree using dict

  root = {'a': node<isWord, {'b': node<isWord, {}>}>}

"""

class Node(object):
    def __init__(self, isWord):
        self.isWord = isWord
        self.d = dict()

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        return self._insert(word, self.d)

    def _insert(self, word, d):
        if len(word) == 0:
            return
        if word[0] not in d:
            d[word[0]] = Node(True if len(word) == 1 else False)
        else:
            if len(word) == 1:
                d[word[0]].isWord = True
        self._insert(word[1:], d[word[0]].d)


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        i = 0
        isWord = False
        d = self.d
        while i < len(word):
            if word[i] not in d:
                return False
            isWord = d[word[i]].isWord
            d = d[word[i]].d
            i += 1
        return isWord


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        i = 0
        d = self.d
        while i < len(prefix):
            if prefix[i] not in d:
                return False
            d = d[prefix[i]].d
            i += 1
        return True


import json


# Your Tre object will be instantiated and called as such:
obj = Trie()
print obj.insert("apple")
print obj.search("apple")
print obj.search("app")
print obj.startsWith("app")
print obj.insert("app")
print obj.search("app")
