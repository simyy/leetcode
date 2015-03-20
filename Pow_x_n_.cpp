/*
Implement pow(x, n).
*/

#include<iostream>
using namespace std;

class Solution {
public:
    double pow(double x, int n)
    {
        if (x == 0) return 0;
        else if (x == 1)  return 1;
        else if (n == 0)  return 1;
        else if (n == 1)  return x;
        else if (x == -1) return (n%2)==0?1:-1;
        else if (n < 0)   return 1/pow(x, -n);
        else if (n == 2)  return x*x;
        //else              return pow(x, n-1)*pow(x, 1); 这个会重复运算相同的计算
        
        int tmp = n/2; //每次平均分为两部分进行计算

        double a = pow(pow(x, tmp), 2); //计算前2＊tmp次，由于前tmp和后tmp是相同的，直接计算一次即可
        double b = pow(x, n%2);    //计算剩余的 n - 2 * tmp，那么也可以通过n%2来计算结果

        return a*b;
    }
};

int main(int args, char** argv)
{
    Solution a;
    double x = a.pow(12.12, 2);

    cout<<x<<endl;

    return 0;
}
