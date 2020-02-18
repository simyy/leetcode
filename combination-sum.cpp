/*
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

Analysis:
回溯法解决组合问题，由于考虑到重复数据的问题，需要对数据进行排序。
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

    void combinate(vector<int>& c, int pos, int target, vector<int>& tmp, vector<vector<int> >& res) {
    	if (target == 0 && tmp.size() > 0) {
    		res.push_back(tmp);
    		return;
    	}

    	for (int i = pos; i < c.size(); ++i) {
    		if (target < c[i])
    			break;
    		if (i > 0 && c[i] == c[i] - 1)
    			continue;
    		tmp.push_back(c[i]);
    		combinate(c, i, target - c[i], tmp, res);
    		tmp.pop_back();
    	}
    }
};

int main(int argc, char* argv)
{
	Solution a;
	int s[] = {2, 3, 6, 7};
	vector<int> candidates (s, s + sizeof(s)/sizeof(int));
	vector<vector<int> > res = a.combinationSum(candidates, 7);
	for (int i = 0; i < res.size(); ++i) {
		for (int j = 0; j < res[i].size(); ++j) {
			cout<<res[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}


