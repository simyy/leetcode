/*
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.

Analysis:
1.当除数divisor为0，x/0是不合法的；
2.INT_MIN=-2147483648,INT_MAX=2147483647，因此-INT_MIN > INT_MAX 不合法；
3.考虑到n<<0=n*2**0,...,n<<1=n*2**1,每做移一位，n会增大一倍，也就是说b<<i=b*2**2，其实就是成倍变化；
3.因此，只需要不断减少divisor的倍数即可，每次都1次开始，直到a<(b<<n)，循环即可。
*/

#include <iostream>
#include <stdlib.h>
#include <limits.h>
using namespace std;


class Solution {
public:
    int divide(int dividend, int divisor)
    {
        int res = 0;

        long a = labs(dividend);
        long b = labs(divisor);

        long sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;

        if (b == 0 || dividend == INT_MIN && divisor == -1) 
            return INT_MAX;
        else if (b == -1)
            return sign * a;

        int i = 0;
        while (a >= b) {
            i = 0;
            while (a >= b<<i) {
                a -= b<<i;
                res += 1<<i;
                i++;
            }
        }
        
        return res*sign;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    int res = a.divide(5, 4);

    cout<<res<<endl;

    return 1;
}
