/*
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
*/

#!/usr/bin/env python
# encoding:utf-8


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def getRow(self, rowIndex):
        rowIndex += 1
    	if rowIndex == 0:
    		return []
    	result = [[1]]
    	if rowIndex == 1:
    		return result[-1]
    	for i in range(1, rowIndex):
    		item = [1]
    		for j in range(len(result[i-1]) - 1):
    			item.append(result[i-1][j] + result[i-1][j+1])
    		item.append(1)
    		result.append(item)
    	return result[-1]


if __name__ == "__main__":
	a = Solution()
	print a.getRow(0)
