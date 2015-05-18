/*
Given two numbers represented as strings, return multiplication of the numbers as a string.
Note: The numbers can be arbitrarily large and are non-negative.

Analysis:
this is a arbitrarily multiply, result maybe beyond the limit, then use string to save it.
For calcuate, we must imitate the multiply, such 12 * 12,
    1   2
*   1   2
----------
    2   4
1   2
----------
1   4   4
so, it can be list as 12 * 2 = 24, 12 * 1 * 10 = 120
*/

class Solution {
public:
    string multiply(string num1, string num2) {
        string res(num1.size() + num2.size(), '0');

        for (int i = num1.size() - 1; i >= 0; --i) {
            int carry = 0; //last multiply carry
            for (int j = num2.size() - 1; j >= 0; --j) {
                int tmp = (res[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0') + carry; //current_num + muti_result + last_carry
                res[i + j + 1] = tmp%10 + '0'; //mod to calcuate the current point num
                carry  = tmp/10; // div to calcuate carry to next
            }
            res[i] += carry;
        }
        int x = res.find_first_not_of('0');
        if (x != string::npos)
            return res.substr(x);
        return "0";
    }
};
