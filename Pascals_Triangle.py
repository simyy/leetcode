/*
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

*/

#!/usr/bin/env python
# encoding:utf-8


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
    	if numRows == 0:
    		return []
    	result = [[1]]
    	if numRows == 1:
    		return result
    	for i in range(1, numRows):
    		item = [1]
    		for j in range(len(result[i-1]) - 1):
    			item.append(result[i-1][j] + result[i-1][j+1])
    		item.append(1)
    		result.append(item)
    	return result


if __name__ == "__main__":
	a = Solution()
	print a.generate(5)
