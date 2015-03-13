/*
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
问题：给定两个长度分别为m和n的有序数组，找到两个数组的有序集合中的中间值。要求时间复杂度在Log(m+n)

分析：
考虑到只需要找到中间值，并且要求时间复杂度为Log(m+n)，那么这个问题和二分法查找数据的问题类似，从而可以参考该方法解决此问题。
那么这个问题可以转化为找到数组中位置k的数据：
1.首先，找到A和B的中间值mA, mB。
2.还需找到A和B数组集合的中间位置p。
  a.如果mA大于mB且k大于p（主要取决于k和p的大小），则p左边的数据都不在考虑玩范围内，那么把搜索边界向右移动到mB的位置，并k值减少mB-Bstart+1
  b.如果mA大于mB且k小于p，则只能将边界左移一位，Aend-=1,k不受影响
  c.如果mA小于mB且k大于p，则p左边的数据都不在考虑玩范围内，那么把搜索边界向右移动到mA的位置，并k值减少mA-Astart+1
  d.如果mA小于mB且k小于p，则只能将边界左移一位，Bend-=1,k不受影响
*/

#include<iostream>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        int k = (m + n + 1) / 2;
        if ((m + n) & 1)
            //odd
            return FindKthElm(A, 0, m - 1, B, 0, n - 1, k);
        else
            //even
            return (FindKthElm(A, 0, m-1, B, 0, n - 1, k) + FindKthElm(A, 0, m - 1, B, 0, n - 1, k + 1)) / 2.0;
    }

    double FindKthElm(int A[], int A_begin, int A_end, int B[], int B_begin, int B_end, int k)
    {
        if (A_begin > A_end)
            return B[B_begin + k -1];
        else if (B_begin > B_end)
            return A[A_begin + k -1];

        int A_middle = A_begin + (A_end - A_begin)/2;
        int B_middle = B_begin + (B_end - B_begin)/2;

        int len = A_end - A_begin + 1 + B_end - B_begin + 1;

        if (A[A_middle] > B[B_middle]) {
            if (k > len/2)
                return FindKthElm(A, A_begin, A_end, B, B_middle+1, B_end, k - (B_middle - B_begin + 1));
            else 
                return FindKthElm(A, A_begin, A_end-1, B, B_begin, B_end, k);
        }
        else {
            if (k > len/2) 
                return FindKthElm(A, A_middle+1, A_end, B, B_begin, B_end, k - (A_middle - A_begin + 1));
            else 
                return FindKthElm(A, A_begin, A_end, B, B_begin, B_end-1, k);
        }
    }

};

int main(int argc, char **argcv)
{
    int A[5]={2,5,9};
    int B[2] = {3,6};

    Solution a;

    double r = a.findMedianSortedArrays(A, 4, B, 2);

    cout<<r<<endl;

    return 0;
}
