# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/simplify-path/

Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level.
For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /,
 and there must be only a single slash / between two directory names.

The last directory name (if it exists) must not end with a trailing /.
Also, the canonical path must be the shortest string representing the absolute path.


Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: "/a/./b/../../c/"
Output: "/c"

Example 5:
Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"


Analysis:
To get the answer, must be do below things:
1. split path by '/', then get a list of file name 
2. '.' is current, it is not useful, then throw away, '..' is superior, then throw away superior file name

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


if __name__ == '__main__':
    print Solution().simplifyPath("/home/")
    print Solution().simplifyPath("/a/../../b/../c//.//")
    print Solution().simplifyPath("/a//b////c/d//././/..")
