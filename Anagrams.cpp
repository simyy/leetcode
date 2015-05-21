/*
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.

Analasis:
use map to save the unique sorted str, then compare every str in strs with the map. 
*/

class Solution {
public:
    vector<string> anagrams(vector<string>& strs) {
        vector<string> res;
        map<string, int> cmp;
        for (int i = 0; i < strs.size(); ++i) {
            string str = strs[i];
            sort(str.begin(), str.end());
            if (cmp.find(str) == cmp.end()) {
                cmp[str] = i;
            }
            else {
                res.push_back(strs[i]);
                if (cmp[str] != -1) {
                    res.push_back(strs[cmp[str]]);
                    cmp[str] = -1;
                }
            }
        }
        return res;
    }
};
