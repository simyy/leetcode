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
};

int main(int argc, char** argv)
{
    Solution a;
    string s = "()(()";
    int res = a.longestValidParentheses(s);
    cout<<res<<endl;

    return 0;
}
