/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Analysis:
题目的意思是找到下一组数据（要求仅大于当前的数据），
因此，需要从数据的个位（右侧）开始遍历，找到第一个a[i]>a[i-1]的，
这样我们通过替换a[i]和a[i-1]就可以得到一个大于当前数据的数据，
但是考虑到仅大于当前的，也就是没有其他组合在此数据和当前数据之间，
那么，需要在i的右侧找到一个比它大的数据,为了寻找到改变最小的，
还是需要从各位开始找起。
*/

#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution{
public:
    void nextPermutation(vector<int>& num)
    {
        if (num.size() < 2)
           return; 
        int i, j;
        for (i = num.size() - 1; i > 0; --i)
            if (num[i] > num[i-1])
                break;
        for (j = num.size() - 1; j > i; --j)
            if (num[i] < num[j])
                break;
        if (i >= 0) swap(num[i], num[j]);
        reverse(num.begin() + i + 1, num.end());
    }
};

int main(int argc, char** argv)
{
    Solution a;
    vector<int> x;
    x.push_back(1);
    x.push_back(2);
    x.push_back(3);
    a.nextPermutation(x);
    for(int i = 0; i < x.size(); ++i)
        cout<<x[i]<<" ";
    cout<<endl;
    x.clear();

    x.push_back(3);
    x.push_back(2);
    x.push_back(1);
    a.nextPermutation(x);
    for(int i = 0; i < x.size(); ++i)
        cout<<x[i]<<" ";
    cout<<endl;
    x.clear();

    x.push_back(1);
    x.push_back(5);
    x.push_back(1);
    a.nextPermutation(x);
    for(int i = 0; i < x.size(); ++i)
        cout<<x[i]<<" ";
    cout<<endl;
    x.clear();

    return 0;
}
