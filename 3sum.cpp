/*
https://leetcode.com/problems/3sum/
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

Analysis:
1.由于结果是正序排列的，因此需要对数据进行排序。
2.由于获取所有符合条件的3个元素，需要对数据进行遍历，
  那么需要在遍历过程中，以一个元素为基础元素a（避免重复数据的产生），不断寻找适合的其他元素b和c。
3.在2中需要寻找的其他元素应该满足a+b+c=0，这里采用快速排序的思想，
  取到a右侧的最左边的起点作为left（由于a左侧的数据已经遍历过了，不需再次考虑）, 最右侧的起点作为right，
  那么可以得到三种其概况
  * a+left+right>0 三元素之和大于0，那么，由于left只能向右移动，只能让结果更大，则right向左移动
  * a+left+right<0 三元素之和小于0，那么，由于right只能向左移动，只能让结果更小，则left向右移动
  * a+left+right=0 满足条件
4.这里需要考虑到，如果a值大于0，left和right肯定是大于0的；在left和right移动过程中，
  如果出现重复数据（由于已经排好序的，因此重复数据必然是相邻数据），可以直接跳过（避免重复）。
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution
{
public:
    vector< vector<int> > threeSum(vector<int> &num) {
        vector< vector<int> > res;
        int size = num.size();
        sort(num.begin(), num.end());
        for (int i = 0; i < size; i++) {
            if (num[i] > 0)
                break;
            if (i > 0 && num[i] == num[i-1]) 
                continue;
            int left = i + 1;
            int right = size -1;
            while (left < right) {
                int sum = num[i] + num[left] + num[right]; 
                if (sum > 0 ) {
                    right--;
                    while (num[right] == num[right+1] && left < right) right--;
                }
                else if (sum < 0 ) {
                    left++;
                    while (num[left] == num[left-1] && left < right) left++;
                }
                else {
                    vector<int> a;
                    a.push_back(num[i]);
                    a.push_back(num[left]);
                    a.push_back(num[right]);
                    res.push_back(a);
                    left++;
                    right--;
                    while (num[left] == num[left-1] && left < right) left++;
                    while (num[right] == num[right+1] && left < right) right--;
                }
            }
        }
        return res;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    int d[] = {-1, 0, 1, 2, -1, 4};
    vector<int> x (d, d+6);

    vector<vector<int> > r = a.threeSum(x);

    for (vector< vector<int> >::iterator i = r.begin(); i != r.end(); i++) {
        cout<<"( ";
        for (vector<int>::iterator j = i->begin(); j != i->end(); j++) {
            cout<<*j<<" "; 
        }
        cout<<")"<<endl;
    }

    return 0;
}

/*

#!/usr/bin/env python

def three_sum(input_list):
    result = list()

    if len(input_list) < 3:
        return result

    sorted_list = sorted(input_list)

    i = 0
    while i < len(sorted_list):
        if sorted_list[i] > 0:
            break

        if sorted_list[i] == sorted_list[i+1]:
            i += 1
            continue

        left = i
        right = len(sorted_list) - 1

        while left < right:
            _sum = sorted_list[i] + sorted_list[left] + sorted_list[right]
            if _sum > 0:
                right -= 1
            elif _sum < 0:
                left += 1
            else:
                result.append((
                    sorted_list[i],
                    sorted_list[left],
                    sorted_list[right]))
                while sorted_list[left] == sorted_list[left+1] \
                        and left < right:
                    left += 1
                while sorted_list[right] == sorted_list[right-1] \
                        and left < right:
                    right -= 1
                left += 1
                right -= 1
        i += 1

    return result


print three_sum([-1, 0, 1, 2, -1, 4])


*/
