/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Analysis:
此题可以通过堆栈和DP两种方式来计算。
问题：获取最长合法子串的长度
解析：
0.标记上一次位置prev=-1(为啥prev=-1? 当i=1时， i-prev=2，这样才符合实际情况)
1.遇到"("，压入堆栈push(i)
2.遇到")"，如果堆栈中存在"("，那么匹配，堆栈pop(),否则，prev=i，标记位置移动到最新位置
3.在匹配的同时，还需要记录当前长度变化，如果堆栈为空,只需要len=i-prev，否则，堆栈top()记录了上一个不匹配"("的位置，len=i-top()
4.每当获得新的len时，都需要比较大小max?len

dp:
主要考虑两种情况：()()和(())
1.如果是()()，当遇到最后一个")"且s[i-2]==')'时则dp[i]+=dp[i-dp[i]
2.如果是(())，当遇到最后一个")"且s[i-1]==')'时则dp[i]+=dp[i-1]
*/

#include <iostream>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> m_stack;
        int max = 0;
        int len = 0;
        int prev = -1;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(')
                m_stack.push(i);
            else {
                if (!m_stack.empty()) {
                    m_stack.pop();
                    if (!m_stack.empty())
                        len = i - m_stack.top();
                    else
                        len = i - prev; 

                    if (max < len)
                        max = len;
                }
                else 
                    prev = i;
            }
        }
        return max;
    }
    
    int dp_longestValidParentheses(string s) {
        int cnt = 0; // count of "("
        vector<int> dp(s.size()+1, 0);

        for (size_t i = 1; i <= s.size(); i++) {
            if (s[i-1] == '(') {
                cnt++;
            } else {
                if (cnt > 0) {
                    cnt--;
                    dp[i] = 2;
                    if (s[i-2] == ')')
                        dp[i] += dp[i-1];                        
                    dp[i] += dp[i-dp[i]];
                }
            }
        }

        return *max_element(dp.begin(), dp.end());
    }
};

int main(int argc, char** argv)
{
    Solution a;
    string s = "()(()";
    int res = a.longestValidParentheses(s);
    cout<<res<<endl;

    return 0;
}
