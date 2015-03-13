/*
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.

Analagy:
1.只有2和5相乘才会出现0，其中整十也可以看做是2和5相乘的结果，因此只需要找到2和5的数量
2.又发现2的数量一定多于5的个数，于是我们只看n前面有多少个5就行了
3.同样的情况2＊25或125或625都可以出现0，那么我们也需要找到25或125或。。。的数量

*/

#include<iostream>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int res = 0;
		while(n)
		{
			res += n/5;
			n /= 5;
		}
		return res;
    }
};

int main(int argc, char** argv)
{
    Solution* a = new Solution();

    int res;

    res = a->trailingZeroes(100);

    cout<<res<<endl;

    delete a;
}
