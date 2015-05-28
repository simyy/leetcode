/*
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

Analysis:
this problem is to get a cycle of numbers in a matrix, then we can use solve it by cycle.
1. push the outer sphere numbers in result
2. ignore last pushed numbers, retry agian
3. there is a condition that after some cycles it will be left a (m - n) rows or (n - m) columns, then add them to result.

*/

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int> >& matrix) {
        vector<int> result;
    	if (matrix.size() == 0)
    		return result;
    	int m = matrix.size();
    	int n = matrix[0].size();

    	int mid = min(m, n)/2;
    	int i = 0;
    	while (i < mid) {
    		for (int j = i; j < n - i - 1; ++j)
    			result.push_back(matrix[i][j]);
    		for (int j = i; j < m - i - 1; ++j)
    			result.push_back(matrix[j][n - i - 1]);
    		for (int j = n - i - 1; j > i; --j)
    			result.push_back(matrix[m - i - 1][j]);
    		for (int j = m - i - 1; j > i; --j)
    			result.push_back(matrix[j][i]);
    		i++;
    	}

    	if(min(m,n) % 2 == 1) {
    		if (m > n) {
    			for (int i = n/2; i < m - n/2; ++i)
    				result.push_back(matrix[i][n/2]);
    		}
    		else {
    			for (int i = m/2; i < n - m/2; ++i)
    				result.push_back(matrix[m/2][i]);
    		}
    	}
    	return result;
    }
};
