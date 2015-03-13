/*
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*/

class Solution {
public:
    int singleNumber(int A[], int n) {
        int one, two, three;
        one = two = three = 0;
        for (int i = 0; i < n; ++i) {
            two = two | (A[i] & one);
            one = one ^ A[i];
            three = one & two;
            one = one ^ three;
            two = two ^ three;
        }
        
        return one;
    }
};
