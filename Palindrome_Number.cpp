/*
Determine whether an integer is a palindrome. Do this without extra space.

判断整数是否为回文字
*/

#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;

        int t = x;
        int n = 0;
        while (t > 0) {
            n = n*10 + t%10;
            t = t/10;
        }
        return x==n?true:false;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    int x;
    cin>>x;

    bool r = a.isPalindrome(x);

    if (r)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;

    return 0;
}
