/*
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Analysis:
1.peak element翻译为大数，其实就是找到一个极大值点。
2.题目中已经给定了边界条件，如果是单调的那么这个最大值也就是极大值了。
3.那么可以根据2分发来分析该问题

   假设只有三个点的话，可以有5种情况
   1.   B          2.  A            3.        C          4.   A - B - C         5.   A      C
      /   \              \                   /                                          \   /
    A       C              B               B                                             B
                             \            /
                               C         A
    1.B为结果，返回
    2.A>B>C，那么向左一定可以找到极大值
    3.A<B<C，那么向右一定可以找到极大值
    4.左右都是一样的情况
    5.左右都是一定样的情况
*/

class Solution {
public:
    int findPeakElement(const vector<int> &num){
        if (num.size() == 1)
            return 0;
        return findMaxOne(num, 0, num.size()-1);
    }

    int findMaxOne(const vector<int> &num, int i, int j){
        if (j - i == 1){
            if (num.at(j) > num.at(i))
                return j;
            else
                return i;
        }
        else if (i == j)
            return i;
        int x = (i + j)/2;
        if (num.at(x) > num.at(x-1)){
            if (num.at(x) > num.at(x+1)){
                return x;
            }
            else {
                return findMaxOne(num, x+1, j);
            }
        }
        else {
            return findMaxOne(num, i, x-1);
        }
    }
};
