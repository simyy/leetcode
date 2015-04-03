/*
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true




*/



#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;


class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        if (p[0] == '\0')
            return *s == '\0';
        if (p[1] == '*')
            return matchStr(p[0], s, p+2);
        if ((*s != '\0') && ((p[0] == '.') || (p[0] == *s)))
            return isMatch(s+1, p+1);
        return false;
    }


    bool matchStr(char c, const char* s, const char* p) {
        if (isMatch(s, p))
            return true;
        else {
            while((*s != '\0') && ((c == *s++)||(c == '.'))) { 
                if(isMatch(s, p))
                    return true;
            }
        }
    }

    bool isMatchd(const char* s, const char* p) {
        int s_len = strlen(s);
        int p_len = strlen(p);

        bool map[s_len+1][p_len+1];
        fill_n(*map, (s_len+1)*(p_len+1), false);
        map[0][0] = true;
        for (int i = 2; i < p_len+1; i+=2) {
            if ((p[i-1] == '*') && map[0][i-2])
                map[0][i] = true;
            else
                break;
        }

        for (int i = 1; i < s_len+1; ++i) {
            for (int j = 1; j < p_len+1; ++j) {
                if (p[j-1] == '*')
                    map[i][j] = map[i][j-2] || map[i-1][j] && ((s[i-1] == p[j-2]) || (p[j-2] == '.'));
                else
                    map[i][j] = map[i-1][j-1] && ((s[i-1] == p[j-1]) || (p[j-1] == '.'));
            }
        }

        return map[s_len][p_len];
    }
};


int main(int argc, char** argv)
{
    Solution a;

    if (a.isMatchd("aa", "a"))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    if (a.isMatchd("aa", "aa"))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    if (a.isMatchd("aaa", "aa"))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    if (a.isMatchd("aa", "a*"))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    if (a.isMatchd("aa", ".*"))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    if (a.isMatchd("ab", ".*"))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
    if (a.isMatchd("aab", "c*a*b"))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;

    return 0;
}
