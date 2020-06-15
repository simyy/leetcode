# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-192/problems/design-browser-history/
"""


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.index = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[:self.index+1]
        self.history.append(url)
        self.index += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.index - steps < 0:
            self.index = 0
        else:
            self.index -= steps
        return self.history[self.index]

    def forward(self, steps):
        """
        :type steps: int
        :rtype:
        """
        if self.index + steps >= len(self.history):
            self.index = len(self.history) - 1
        else:
            self.index += steps
        return self.history[self.index]


if __name__ == '__main__':
    obj = BrowserHistory("leetcode.com")
    print obj.visit("google.com")
    print obj.visit("facebook.com")
    print obj.visit("youtube.com")
    print obj.back(1)
    print obj.back(1)
    print obj.forward(1)
    print obj.visit("linkedin.com")
    print obj.forward(2)
    print obj.back(2)
    print obj.back(7)
