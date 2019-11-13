"""
Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

This is not correct answer!!!! TODO!!!

"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.map = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if word is None:
            return
        if len(word) == 0:
            return
        char = word[:1]
        if char not in self.map:
            self.map[char] = {}
        node = WordDictionary()
        if len(word) > 1:
            node.addWord(word[1:])
        elif len(word) == 1:
            node.isWord = True
        self.map[char] = node

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word is None:
            return False
        if len(word) == 0:
            return self.isWord
        if len(self.map) == 0:
            return False

        char = word[0]
        if '.' == char:
            for (k, v) in self.map.items():
                if v.search(word[1:]):
                    return True
        else:
            if char in self.map:
                return self.map[char].search(word[1:])
        return False
