"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".


Analysis:
To get the answer, must be do below things:
1. split path by '/', then get a list of file name 
2. '.' is current, it is unusefull, then throw away, '..' is superior, then throw away superior file name

In this sulution, the split result of '//'  is None, then it is doesn't mater
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        items = path.split("/")
        vector = []
        for i in range(len(items)):
            if items[i] == "..":
                vector = vector[:-1]
            elif items[i] == "":
                 pass
            elif items[i] == ".":
                 pass
            else:
                 vector.append(items[i])
        return "/" + "/".join(vector)
