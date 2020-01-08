/*]
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Analysis:
if the space between a and b can strap water, it must be a > x < b.
Then, it can use the two pointer(left and right pointer),
1.find the min height between left and right
2.along left and right, find it whic height < min, then add min - height

such as:
             ___
            |   |     ___
    ___     |   |    |   |
   |   ||||||   ||||||   |
___|                     |
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int len = height.size();
        int l = 0; 
        int r = len - 1;
        int total = 0;
        int min_height = 0;
        while (l < r) {
            min_height = min(height[r], height[l]);
            while (l < r && height[l] <= min_height) {
                l++;
                total += max(0, min_height - height[l]);
            }
            while(l < r && height[r] <= min_height) {
                r--;
                total += max(0, min_height - height[r]);
            }
        }
        return total;
    }
};

int main(int argc, char** argv)
{
    Solution a;
    int xx[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    vector<int> height (xx, xx+12);
    int res = a.trap(height);
    cout<<res<<endl;

    return 0;
}
