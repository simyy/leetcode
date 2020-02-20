/*
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.

Analysis:
traverse 1~n：
asume i = 1 ~ n
1.if i==1, then "11 or one 1"
2.if i==2 and last result is 11, then "21 or two 1s"
3.if i==3 and last result is 21, thren "1211 or one 2, then one 1"
*/

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n <= 0) return string();
        string res = "1";
        for (int i = 1; i < n; ++i) {
            res = count(res);
        }
        return res;
    }

    string count(string num) {
        string res = "";
        char last = num[0];
        int c = 1;
        for (int i = 1; i < num.size(); ++i) {
            if (num[i] == last)
                c++;
            else{
                res += to_string(c);
                res.push_back(last);
                c = 1;
                last = num[i];
            }
        }
        res += to_string(c);
        res.push_back(last);
        
        return res;
    }
};

int main(int argc, char** argv)
{
    Solution a;
    string res = a.countAndSay(5);
    cout<<res<<endl;

    return 0;
}
