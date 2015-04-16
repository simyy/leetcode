/*
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.


Analysis:
此题的大概意思是存在n个高度为an的木板，各个木板之间的距离为单位距离（1m）,求出这n个木板之间的最多可以容纳的水的大小。
可以理解为一个水槽，在水槽中放入n个挡板，求其中哪两个挡板之间容纳的水的体积最大，该题可以应用快速排序的算法思想。
1.由于要求水的容纳量最大，那么需要遍历整个数组，最小的复杂度为O（n）
2.选取两个指针最left和最right，第一次求出体积作为默认值
3.由于只需要选择出最大的，那么可以考虑贪心策略，只需要按照挡板低的一方继续移动即可，因为只有这样才可能取到更大的面积
4.保证left<right，否则停止
*/

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        int left = 0;
        int right = height.size() - 1;

        while (left < right) {
            if (height[left] >= height[right]) 
                int area = (right - left) * (height[right--]);
            else 
                int area = (right - left) * (height[left++]);
            max = area > max ? area: max;
        }

        return max;
    }
};

int main(int argc, char** argv)
{
    Solution a;
    int z[] = {6,5,3,4,2};
    vector<int> height (z, z+5);

    int r = a.maxArea(height);
    cout<<r<<endl;


    return 0;
}
