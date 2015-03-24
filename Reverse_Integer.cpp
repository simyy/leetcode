/*
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

对整数求余数，倒序排列即可，注意整数限制，正负号。
*/

#include <iostream>
#include <cstdlib>
#include <limits.h>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        long r = 0;
        long t = abs((long)x);
        while (t != 0) {
            r = r*10 + t%10;
            t = t/10;
        }

        if (r > INT_MAX)
            return 0;

        r = (x < 0 ? -1*r: r);
        return r;

    }

};

int main(int args, char** argc)
{
    Solution a;

    //int res = a.reverse(123);
    int res = a.reverse(1534236469);

    cout<<res<<endl;

    return 0;
}
