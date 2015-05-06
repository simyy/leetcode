/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"

Analysis:
此题主要考查组合问题，可以使用动态规划来解决。
1.需要记录左半符号"("的出现次数n1，和右半符号")"的出现次数n2，0 <= n1,n2 <= 3
2.还需要注意，符号的匹配条件可以转化为 n1-n2 >= 0
3.应用动态规划求解即可。
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        generateParenthesis(res, "",  0, n, n); 
        return res;
    }

    void generateParenthesis(vector<string>& res, string str, int n, int n1, int n2)
    {
        if (n1 == 0 && n2 == 0)
            res.push_back(str);
        else
        {
            if(n1 > 0)
                generateParenthesis(res, str + "(", n+1, n1 - 1, n2);
            if(n2 > 0 && n-1 >= 0) 
                generateParenthesis(res, str + ")", n-1,n1, n2 - 1); 
        }
    }
};

int main(int argc, char** argv)
{
    Solution a;
    int n = 3;
    vector<string> res = a.generateParenthesis(n);

    for (int i = 0; i < res.size(); ++i) 
        cout<<res[i]<<endl;

    return 0;
}
