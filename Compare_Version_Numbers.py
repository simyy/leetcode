"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

Analysis:
split in list, then compare from i in min(len(list)).
but must be be careful to compare 1.0 to 1, the last zero is no useful
"""

#!/usr/bin/env python
# encoding:utf-8

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        list1 = version1.split(".")
        list2 = version2.split(".")
        for i in range(min(len(list1), len(list2))):
            if int(list1[i]) > int(list2[i]):
                return 1 
            elif int(list1[i]) < int(list2[i]):
                return -1
        if len(list1) > len(list2) and filter(lambda x:int(x)!=0, list1[len(list2):]):
            return 1 
        elif len(list1) < len(list2) and filter(lambda x:int(x)!=0, list2[len(list1):]):
            return -1
        return 0 


if __name__ == "__main__":
    a = Solution()
    print a.compareVersion('1', '1.1')
