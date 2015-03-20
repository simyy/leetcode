/*
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

找出字符串中最长的回文字，例如, abcbaaa中最长的回文字为abcba，对称形式的。
此外，需要考虑到aa，应该输出aa；bbb，应该输出bbb。

思路：
1.遍历字符串，从0开始；
2.如果s[i-1] == s[i+1]，则s[i-1:i+1]是一个回文字，则继续向左右移动，重复步骤2，比较s[i-2]与s[i+2]；
3.如果s[i]=1 != s[i+1]，则比较s[i-1]与s[i]，相同的话，跳转到步骤2即可；否则，比较s[i]与s[i+1]，相同的话，跳转步骤2即可。但需要注意此时的回文字的边界已经发生改变。
/*

#include<iostream>
using namespace std;

class Solution {
 public:
    string longestPalindrome(string s) {
        int max = 1;
        int start = 0;
        for (int i = 0; i < s.size(); ++i) {
            int len = 1; 
            int left = 0;
            int right = 0;
            int flag = 0;
            for (int j = 1; j <= i-left;) {
                if ((s[i-left-j] == s[i+right+j])) {
                    len += 2;
                    flag = 1;
                    j++;
                }
                else if (flag != 1) { 
                    if((i-1-left>= 0) && (s[i-left]==s[i-1-left])) {
                        len += 1;
                        left += 1;
                    }
                    else if ((i+1+right < s.size()) && (s[i+right] == s[i+right+1])) {
                        len += 1;
                        right += 1;
                    }
                    else
                        break;
                }
                else {
                    j++;
                    break;
                }
                if (max < len) {
                    max = len;
                    start = i - left - (len-left-right)/2;
                }
            }
        }
        return s.substr(start, max);
    }
};

int main(int argc, char** argv)
{
    //string s = "bcacbaabb";
    string s = "ccc";

    Solution a;

    string res = a.longestPalindrome(s);

    cout<<res<<endl;

    return 0;
}
