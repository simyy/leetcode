/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
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
