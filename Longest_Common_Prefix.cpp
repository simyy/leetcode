/*
Write a function to find the longest common prefix string amongst an array of strings.

Analysis:
由于两个字符串的相同前缀一定是包含于所有字符串的前缀的，因此只需要依次比较下来就可以了。
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0)
            return "";
        string commonPrefix = strs[0];
        for (int i = 1; i < strs.size(); ++i) {
            int j = 0;
            while (j < strs[i].size() && j < commonPrefix.size() && strs[i][j] == commonPrefix[j])
                j++;
            commonPrefix = commonPrefix.substr(0, j);
        }
        return commonPrefix;
    }
};


int main(int argc, char** argv)
{
    vector<string> strs;
    strs.push_back("ab");
    strs.push_back("b");

    Solution a;
    string r = a.longestCommonPrefix(strs);
    cout<<r<<endl;

    return 0;
}
