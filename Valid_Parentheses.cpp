/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Analysis:
此题主要考察了堆栈的使用，但需要注意：
1.符号的左半部分可以无限叠加
2.符号的右半部分需要与左半部分对称，并且每一个符号都存在一个与之相对应的符号
那么，
1.采用堆栈的先进后出的原理，把左半符号全部压入堆栈，例如<{,(,[,{>
2.当遇到右半符号时，需要查看是否满足对称条件，也就是stack.top是否和有伴符号匹配，匹配statk.pop，否则return false
3.由于遇到有伴符号时，我们只会有两种操作，stack.pop和return false，因此，堆栈中应该只会存储左半符号
4.如果遍历结束后，堆栈中仍有符号，那么证明这些符号没有找到与之相对应的符号，return false，否则stack.empty返回 true
*/

#include <iostream>
#include <string.h>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> pattern;
        int i = 0;
        while (i < s.size()) {
            switch(s[i]) {
                case '(':
                    pattern.push(s[i]);break;
                case '{':
                    pattern.push(s[i]);break;
                case '[':
                    pattern.push(s[i]);break;
                case ')':
                    if (!pattern.empty() && pattern.top() == '(')
                        pattern.pop();
                    else
                        return false;
                    break;
                case '}':
                    if (!pattern.empty() && pattern.top() == '{')
                        pattern.pop();
                    else
                        return false;
                    break;
                case ']':
                    if (!pattern.empty() && pattern.top() == '[')
                        pattern.pop();
                    else
                        return false;
                    break;
                default:
                    ;
            }
            i++;
        }
        return pattern.empty();

    }
};

int main(int argc, char** argv)
{

    Solution a;
    string s = "{[()]}";
    bool r = a.isValid(s);

    if (r) 
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;

    return 0;
}
