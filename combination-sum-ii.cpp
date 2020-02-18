/*
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

Analysis:
同样是回溯法，但是需要注意相同元素的问题，每次使用了一个元素，需要将其从备选元素列表中删除。
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
    	vector<vector<int> > res;
    	vector<int> tmp;
    	sort(candidates.begin(), candidates.end());
    	combinate(candidates, 0, target, tmp, res);
    	return res;
    }

    void combinate(vector<int>& c, int pos, int target, vector<int> &tmp, vector<vector<int> >& res) {
    	if (target == 0 && tmp.size() > 0) {
    		res.push_back(tmp);
    		return;
    	}

    	for (int i = pos; i < c.size(); ++i) {
    		int m = c[i];
    		if (target < m)
    			break;
    		if (i > 0 && c[i] == c[i-1] && i > pos) //jump beyond a common one
    			continue;
    		tmp.push_back(m);
    		c.erase(c.begin() + i);
    		combinate(c, i, target - m, tmp, res);
    		c.insert(c.begin() + i, m);
    		tmp.pop_back();
    	}
    }
};

int main(int argc, char* argv)
{
	Solution a;
	int s[] = {1};
	vector<int> candidates (s, s + sizeof(s)/sizeof(int));
	vector<vector<int> > res = a.combinationSum(candidates, 2);
	for (int i = 0; i < res.size(); ++i) {
		for (int j = 0; j < res[i].size(); ++j) {
			cout<<res[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}


